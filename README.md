# 🏦 RevoBank: Sales Performance & Risk Analytics 2025
**Full-Stack Credit Card Portfolio Optimization: Ingesting Pipelines, Machine Learning Customer Segmentation, and C-Suite Risk Management Strategy**

---

## 📌 Executive Summary
RevoBank operates within a highly resilient operational climate, maintaining an exceptionally low **Fraud Rate of 0.22%**, significantly beating global banking risk exposure thresholds. However, asset optimization metrics revealed a severe efficiency leak: out of **IDR 138.18 Billion** in total credit limit capacity, only **IDR 36.64 Billion** is utilized (Assets Under Management / AUM). 

This project delivers an end-to-end data processing pipeline and an **Unsupervised Machine Learning model (K-Means Clustering, k=3)** to segment **4,772 active credit card accounts** into distinct behavioral personas. The final framework transforms raw demographic friction into targeted marketing strategies to unlock **IDR 102 Billion in idle credit capacity** without compromising portfolio security.

---

## 🏗️ Analytics Pipeline & Architecture

### 1. Data Source Ingestion
The data layer processes two decoupled operational structures via Python:
- `INT_card_data.csv`: Transaction logs, active limits, fraud flags, and account lifecycle timestamps.
- `INT_user_data.csv`: Demographics, annual income declarations, and legacy macro leverage profiles.

### 2. Exploratory Data Scrubbing & Pipeline 
- **Currency Data Normalization:** Developed custom regex functions to strip local currency formatting (`Rp`, `.`, `,`) and convert string values to numeric metrics.
- **Missing Value Resolution:** Investigated a 90% missingness rate inside fraud flag structures. Applied logical imputation to `0` since fraud nodes depend entirely on standard transactions.
- **Data Integrity Constraints:** Cleared multi-character trailing typos in categorical fields (`Jcb` ➔ `JCB`), resolved 31 exact data duplicates, and filtered out expired card portfolios.
- **Relational Integration Layer:** Aggregated daily transactional frequency blocks at the client level before mapping a master compilation layer via SQL-equivalent `Inner Join`.

---

## 📊 Multivariate Customer Segmentation Validation 

To ensure the clustering structure was scientifically resilient, variables like `yearly_income`, `credit_limit`, `total_debt`, `DTI`, and `transaction volumes` were processed through two statistical checkpoints:
- **Elbow Method (Inertia Plot):** Evaluated cost functions across \(k \in [1, 10]\), identifying a definitive mathematical bend ("elbow") at exactly k=3.
- **Silhouette Coefficient Verification:** Calculated cluster density splits across \(k \in [2, 7]\). Testing mathematically proved that **k=3 generated the highest local score (0.2503)**, providing clean empirical boundary definition.

---

## 🔍 Master Behavioral Persona Interpretation

### 1. Cluster 1: VIP Loyalists (The Revenue Engine)
- **Financial Profile:** High Average Capital Income (~IDR 70M), robust assigned limits, and exceptionally healthy leverage.
- **Behavioral Footprint:** Highest transaction intensity (232 purchases over 6 months) and a dominant transaction volume (~IDR 155M).
- **Corporate Action Mandate:** **Retention & Premium Network Tiering.** Partner with luxury payment gateways (e.g., American Express) to maximize Merchant Discount Rate (MDR) fee extraction.

### 2. Cluster 2: Stable Potentials (The Mass Growth Base)
- **Financial Profile:** Moderate income levels (~IDR 53M) paired with the cleanest financial records (Lowest Debt-to-Income / DTI ratio: 0.11).
- **Behavioral Footprint:** Stable spending velocity (58 transactions) with an average volume of ~IDR 33M.
- **Corporate Action Mandate:** **Up-selling & Transaction Accelerators.** Trigger tactical credit limit increase campaigns paired with everyday essential cashback bonuses (groceries, utilities) to convert them into top-of-wallet daily drivers.

### 3. Cluster 3: Risky Low Spenders (The Liquidity Trap)
- **Behavioral Footprint:** Most passive user segment. Extremely low spending frequency (34 transactions) and lowest transaction volume (~IDR 21M).
- **Financial Profile:** Highest overall average income (~IDR 71M) but critically over-leveraged with a dangerous **0.38 DTI ratio**.
- **Corporate Action Mandate:** **Risk Control & Debt Consolidation.** Tighten risk thresholds by halting aggressive limit extensions. Offer structured low-interest Balance Transfer pipelines to safely manage cash flow blockages.

---

## 💡 Strategic Executive C-Level Takeaways
1. **The Income Paradox:** High income profiles do not automatically generate credit card transaction volume, as shown by the *Risky Low Spenders*. Portfolio growth models must shift target weights from static demographic variables to live behavioral transactional frequency indicators.
2. **Age-Based Capital Allocation:** Analytical cross-examinations confirm that older age demographics hold significant unutilized limits. Brand teams must engineer targeted financial wealth protection and lifestyle insurance add-on structures to capitalize on this stable capital base.

---

## 📁 Repository Directory Structure

```text
├── notebooks/
│   ├── data_cleaning_and_preprocessing.py   # Ingestion and Regex Scrubbing Pipeline
│   ├── data_merging_and_financial_kpis.py   # Inner Joins and Core Bank KPI Formulas
│   └── customer_behavioral_segmentation.py  # Outlier Check, Scaling, and K-Means Clustering
├── presentation/
├── LICENSE                                  # MIT License open-source terms
└── README.md                                # Master Documentation Profile
```

### 📑 Project Deliverable & Visual Slide
- **[Download RevoBank Executive Presentation (PDF)](https://github.com/rifahya17/revobank-performance-risk-analytics/blob/main/presentation/reVobank%20analysis%20sales%20performance%202025.pdf)**
