# =================================================================================
# PROJECT      : RevoBank Sales & Risk Performance Analytics
# STAGE        : Milestone 1 & 2 - Exploratory Data Scrubbing & Processing Pipeline
# TECH STACK   : Python (Pandas, NumPy)
# FILES TARGET : INT_card_data.csv & INT_user_data.csv
# DESCRIPTION  : Performs structural transformations, currency regex normalization,
#                resolves severe 90% missingness flags, and enforces schema types.
# =================================================================================

import pandas as pd
import numpy as np

def preprocess_credit_card_data(file_path):
    """Ingests, logs anomalies, and cleans transactional telemetry assets."""
    print("📥 Ingesting Raw Card Telemetry Data...")
    df_card = pd.read_csv(file_path)
    
    # A. Initial System Inspection
    print("\n--- Raw Schema Baseline (Card Data) ---")
    print(df_card.info())
    
    # B. Currency Regular Expression Scrubbing Pipeline 
    print("\n⚡ Executing string-to-numeric regex conversions...")
    df_card['credit_limit'] = df_card['credit_limit'].astype(str).str.replace(r'[Rp., ]', '', regex=True).str.strip()
    df_card['credit_limit'] = pd.to_numeric(df_card['credit_limit'], errors='coerce')
    
    # C. Resolving Missing Transaction Flags via Cohort Imputation 
    # Rationale: ~90% missing values in fraud streams denote non-fraud occurrences.
    # We safely fill with 0 since active fraud vectors depend entirely on core transactions.
    all_trx_cols = ['count_nonfraud_trx_L6M', 'amt_nonfraud_trx_L6M', 'count_fraud_trx_L6M', 'amt_fraud_trx_L6M']
    for col in all_trx_cols:
        df_card[col] = df_card[col].astype(str).str.replace(r'[Rp., ]', '', regex=True).str.strip()
        df_card[col] = pd.to_numeric(df_card[col], errors='coerce').fillna(0)
        if 'count' in col:
            df_card[col] = df_card[col].astype(int) # Enforce discrete integrity (Slide 3)

    # D. Datetime Format Parsing 
    df_card['expires'] = pd.to_datetime(df_card['expires'], errors='coerce')
    df_card['acct_open_date'] = pd.to_datetime(df_card['acct_open_date'], errors='coerce')
    
    # E. Relational Key Constraints 
    df_card['id'] = df_card['id'].astype(str)
    df_card['client_id'] = df_card['client_id'].astype(str)
    
    # F. Structural Categorical Alignment 
    df_card['card_brand'] = df_card['card_brand'].astype(str).str.strip()
    df_card['card_brand'] = df_card['card_brand'].replace({'Jcb': 'JCB', 'jcb': 'JCB'})
    
    # G. Duplicate Removal Protocol 
    print(f"🔹 Duplicate records identified: {df_card.duplicated().sum()}")
    df_card = df_card.drop_duplicates(keep='first')
    
    # H. Active Portfolio Constraint Filters 
    # Excludes card products expired past May 31, 2025 and inactive unallocated limits
    df_clean_card = df_card[(df_card['expires'] > '2025-05-31') & (df_card['credit_limit'] > 0)].copy()
    df_clean_card = df_clean_card.reset_index(drop=True)
    
    print(f"✅ Card Preprocessing complete. Safe active rows: {len(df_clean_card)}")
    return df_clean_card

def preprocess_user_demographics(file_path):
    """Transforms and constructs target risk metrics over customer assets."""
    print("\n📥 Ingesting Raw Demographics Data...")
    df_user = pd.read_csv(file_path)
    
    print("\n--- Raw Schema Baseline (User Data) ---")
    print(df_user.info())
    
    # A. Feature Engineering: Operational Evaluation Age 
    df_user['birthdate'] = pd.to_datetime(df_user['birthdate'], errors='coerce')
    df_user['actual_age'] = 2026 - df_user['birthdate'].dt.year # Baseline operational tracking target
    
    # B. Demographics Financial Field Scrubbing 
    finance_fields = ['per_capita_income', 'yearly_income', 'total_debt']
    for col in finance_fields:
        df_user[col] = df_user[col].astype(str).str.replace(r'[Rp., ]', '', regex=True).str.strip()
        df_user[col] = pd.to_numeric(df_user[col], errors='coerce')
        
    # C. Risk Infrastructure Architecture: Debt-to-Income (DTI) Ratio 
    df_user['DTI'] = df_user['total_debt'] / df_user['yearly_income']
    df_user['id'] = df_user['id'].astype(str)
    
    print(f"✅ User Preprocessing complete. Secure target rows: {len(df_user)}")
    return df_user

if __name__ == "__main__":
    card_refined = preprocess_credit_card_data("data-raw/INT_card_data.csv")
    user_refined = preprocess_user_demographics("data-raw/INT_user_data.csv")
    
    # Saving isolated cleaning checkpoints
    card_refined.to_csv("data-raw/checkpoint_card_cleaned.csv", index=False)
    user_refined.to_csv("data-raw/checkpoint_user_cleaned.csv", index=False)
