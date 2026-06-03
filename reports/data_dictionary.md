**# Mutual Fund Analytics - Data Dictionary**



**## 01\_fund\_master.csv**



**| Column            | Data Type | Description              |**

**| ----------------- | --------- | ------------------------ |**

**| amfi\_code         | Integer   | Unique AMFI scheme code  |**

**| fund\_house        | Text      | Mutual fund company name |**

**| scheme\_name       | Text      | Scheme/Fund name         |**

**| category          | Text      | Fund category            |**

**| sub\_category      | Text      | Fund sub-category        |**

**| plan              | Text      | Direct/Regular plan      |**

**| launch\_date       | Date      | Scheme launch date       |**

**| benchmark         | Text      | Benchmark index          |**

**| expense\_ratio\_pct | Float     | Expense ratio percentage |**

**| risk\_category     | Text      | Risk classification      |**



**---**



**## 02\_nav\_history.csv**



**| Column    | Data Type | Description     |**

**| --------- | --------- | --------------- |**

**| amfi\_code | Integer   | Fund identifier |**

**| date      | Date      | NAV date        |**

**| nav       | Float     | Net Asset Value |**



**---**



**## 07\_scheme\_performance.csv**



**| Column         | Data Type | Description                      |**

**| -------------- | --------- | -------------------------------- |**

**| return\_1yr\_pct | Float     | 1-year return                    |**

**| return\_3yr\_pct | Float     | 3-year return                    |**

**| return\_5yr\_pct | Float     | 5-year return                    |**

**| alpha          | Float     | Excess return over benchmark     |**

**| beta           | Float     | Volatility compared to benchmark |**

**| sharpe\_ratio   | Float     | Risk-adjusted return             |**

**| sortino\_ratio  | Float     | Downside risk-adjusted return    |**



**---**



**## 08\_investor\_transactions.csv**



**| Column           | Data Type | Description             |**

**| ---------------- | --------- | ----------------------- |**

**| investor\_id      | Text      | Unique investor ID      |**

**| transaction\_date | Date      | Transaction date        |**

**| transaction\_type | Text      | SIP/Lumpsum/Redemption  |**

**| amount\_inr       | Integer   | Transaction amount      |**

**| state            | Text      | Investor state          |**

**| city             | Text      | Investor city           |**

**| kyc\_status       | Text      | KYC verification status |**



**---**



**## Source References**



**1. Bluestock Mutual Fund Analytics Dataset**

**2. MFAPI (https://api.mfapi.in)**

**3. AMFI Mutual Fund Scheme Data**



