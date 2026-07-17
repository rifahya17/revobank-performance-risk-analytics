# =================================================================================
# PROJECT      : RevoBank Sales & Risk Performance Analytics
# STAGE        : Milestone 2 - Relational Data Merging & Executive Financial KPIs
# TECH STACK   : Python (Pandas)
# DESCRIPTION  : Consolidates client transaction frequencies, maps master relational 
#                joins, and extracts critical credit exposure analytics (AUM & Risk).
# =================================================================================

import pandas as pd

def compute_executive_banking_kpis(df_final):
    """Calculates operational and risk thresholds required for C-level presentation."""
    print("\n📊 EXTRACTING MASTER FINANCIAL PERFORMANCES & KPI METRICS...")
    
    # Merchant Discount Rate (MDR) operational fee threshold assignment
    mdr_rate = 0.015 
    
    # 1. Credit Limit Allocation vs Utilization Loop
    total_credit_capacity = df_final['credit_limit'].sum()
    total_debt_managed = df_final['total_debt'].sum() # Assets Under Management (AUM)
    
    # 2. Net Profit Loop Calculation Framework
    total_sales = df_final['amt_nonfraud_trx_L6M'].sum()
    mdr_gross_fee_profit = total_sales * mdr_rate
    total_fraud_loss = df_final['amt_fraud_trx_L6M'].sum()
    net_profit = mdr_gross_fee_profit - total_fraud_loss
    
    # 3. Security Portfolio Integrity Check: Fraud Rate Loop 
    total_all_transactions = total_sales + total_fraud_loss
    fraud_rate_pct = (total_fraud_loss / total_all_transactions) * 100
    
    # Executive System Output Delivery Terminal
    print(f"• Total Assigned Capital Capacity (Limit) : Rp {total_credit_capacity:,.2f}")
    print(f"• Total Active Capital Utilization (AUM)  : Rp {total_debt_managed:,.2f}")
    print(f"• Gross Transaction Volume (Non-Fraud)    : Rp {total_sales:,.2f}")
    print(f"• Generated MDR Gross Revenues            : Rp {mdr_gross_fee_profit:,.2f}")
    print(f"• Absorbed Risk Demolition Loss (Fraud)   : Rp {total_fraud_loss:,.2f}")
    print(f"• Consolidated Net Operational Profit     : Rp {net_profit:,.2f}")
    print(f"• Fraud Velocity Risk Index Status        : {fraud_rate_pct:.4f}%")
    
    # Standard compliance warning check (Industry benchmark alert loop)
    if fraud_rate_pct < 0.1:
        print("🛡️ Risk Assessment Status: EXTREMELY SECURE (Within green standard bounds).")
    else:
        print("⚠️ Risk Assessment Status: MONITOR VELOCITY (Slight upward anomaly detected).")

if __name__ == "__main__":
    # Load clean preprocessing assets
    card_agg_source = pd.read_csv("data-raw/checkpoint_card_cleaned.csv")
    user_source = pd.read_csv("data-raw/checkpoint_user_cleaned.csv")
    
    # Multi-row transaction token aggregation per unique client channel
    card_group = card_agg_source.groupby('client_id').agg({
        'amt_nonfraud_trx_L6M': 'mean',
        'count_nonfraud_trx_L6M': 'sum',
        'amt_fraud_trx_L6M': 'sum',
        'count_fraud_trx_L6M': 'sum',
        'days_since_last_trx': 'min',
        'credit_limit': 'sum'
    }).reset_index()
    
    # Master Relational Compilation Layer via Inner Join mapping 
    df_master_analytical = pd.merge(card_group, user_source, left_on='client_id', right_on='id', how='inner')
    
    # Enforce index alignment structures
    df_master_analytical = df_master_analytical.reset_index(drop=True)
    
    # Execute KPI Metrics Engine
    compute_executive_banking_kpis(df_master_analytical)
    
    # Export clean analytical matrix for machine learning ingestion
    df_master_analytical.to_csv("data-raw/final_cleaned_user_data.csv", index=False)
    print("\n✅ Master compiled matrix exported successfully to 'data-raw/final_cleaned_user_data.csv'")
