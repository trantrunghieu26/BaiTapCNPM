# Báo cáo Kiểm thử Module Phê duyệt Khoản vay Cá nhân – Ngân hàng CS2045

---

## 1. Phân hoạch tương đương (EP) & Phân tích giá trị biên (BVA)

### 1.1. Biến `age` – Số nguyên, hợp lệ trong [18, 65]

#### Phân hoạch tương đương:

| Lớp | Mô tả | Đại diện |
|:---:|---|:---:|
| **EP1** (Không hợp lệ) | Số nguyên nhỏ hơn 18 | `0`, `-5` |
| **EP2** (Hợp lệ) | Số nguyên trong [18, 65] | `40` |
| **EP3** (Không hợp lệ) | Số nguyên lớn hơn 65 | `100` |
| **EP4** (Không hợp lệ) | Sai kiểu dữ liệu (float, str, bool) | `25.5`, `"30"`, `True` |

#### Phân tích giá trị biên (5-point BVA):

| Vị trí biên | Giá trị | Loại | Kết quả mong đợi |
|---|:---:|:---:|:---:|
| Ngoài biên dưới | `17` | Không hợp lệ | `Invalid Input` |
| **Biên dưới tối thiểu** | **`18`** | **Hợp lệ** | không phải Invalid |
| Sát trên biên dưới | `19` | Hợp lệ | không phải Invalid |
| Nominal | `40` | Hợp lệ | không phải Invalid |
| Sát dưới biên trên | `64` | Hợp lệ | không phải Invalid |
| **Biên trên tối đa** | **`65`** | **Hợp lệ** | không phải Invalid |
| Ngoài biên trên | `66` | Không hợp lệ | `Invalid Input` |

---

### 1.2. Biến `income` – Số thực (1 chữ số thập phân), hợp lệ trong [5.0, 500.0]

> Có 2 điểm biên nghiệp vụ cần kiểm thử: **5.0** (biên miền giá trị) và **15.0** (biên phân tách quy tắc quyết định).

#### Phân hoạch tương đương:

| Lớp | Mô tả | Đại diện |
|:---:|---|:---:|
| **EP1** (Không hợp lệ) | Giá trị < 5.0 | `4.9`, `-10.0` |
| **EP2a** (Hợp lệ – Nhóm thấp) | Giá trị trong [5.0, 14.9] | `10.0` |
| **EP2b** (Hợp lệ – Nhóm cao) | Giá trị trong [15.0, 500.0] | `200.0` |
| **EP3** (Không hợp lệ) | Giá trị > 500.0 | `500.1` |
| **EP4** (Không hợp lệ) | Sai kiểu dữ liệu (str, bool) | `"100"`, `True` |

#### Phân tích giá trị biên:

| Vị trí biên | Giá trị | Loại | Ghi chú |
|---|:---:|:---:|---|
| Ngoài biên dưới | `4.9` | Không hợp lệ | Biên miền giá trị |
| **Biên dưới tối thiểu** | **`5.0`** | **Hợp lệ** | Biên miền giá trị |
| Sát trên biên dưới | `5.1` | Hợp lệ | |
| Sát dưới biên nghiệp vụ | `14.9` | Hợp lệ | **Biên quy tắc quyết định** |
| **Biên nghiệp vụ** | **`15.0`** | **Hợp lệ** | **Điểm phân tách quy tắc** |
| Sát trên biên nghiệp vụ | `15.1` | Hợp lệ | **Biên quy tắc quyết định** |
| Sát dưới biên trên | `499.9` | Hợp lệ | |
| **Biên trên tối đa** | **`500.0`** | **Hợp lệ** | Biên miền giá trị |
| Ngoài biên trên | `500.1` | Không hợp lệ | |

---

### 1.3. Biến `credit_score` – Số nguyên, hợp lệ trong [300, 850]

> Có 2 điểm biên phân loại rủi ro nội bộ: **500/501** (High→Medium) và **700/701** (Medium→Low).

#### Phân hoạch tương đương:

| Lớp | Mô tả | Đại diện |
|:---:|---|:---:|
| **EP1** (Không hợp lệ) | Số nguyên < 300 | `0`, `299` |
| **EP2** (Hợp lệ – High Risk) | Số nguyên trong [300, 500] | `400` |
| **EP3** (Hợp lệ – Medium Risk) | Số nguyên trong [501, 700] | `600` |
| **EP4** (Hợp lệ – Low Risk) | Số nguyên trong [701, 850] | `750` |
| **EP5** (Không hợp lệ) | Số nguyên > 850 | `851` |
| **EP6** (Không hợp lệ) | Sai kiểu dữ liệu (float, bool) | `650.5`, `True` |

#### Phân tích giá trị biên (các điểm biên quan trọng):

| Vị trí biên | Giá trị | Risk | Ghi chú |
|---|:---:|:---:|---|
| Ngoài biên dưới | `299` | – | Không hợp lệ |
| **Biên dưới tối thiểu** | **`300`** | High | Biên miền giá trị |
| Sát trên biên dưới | `301` | High | |
| Biên trên của High | `500` | High | **Biên phân loại rủi ro** |
| Biên dưới của Medium | `501` | Medium | **Biên phân loại rủi ro** |
| Biên trên của Medium | `700` | Medium | **Biên phân loại rủi ro** |
| Biên dưới của Low | `701` | Low | **Biên phân loại rủi ro** |
| Sát dưới biên trên | `849` | Low | |
| **Biên trên tối đa** | **`850`** | Low | Biên miền giá trị |
| Ngoài biên trên | `851` | – | Không hợp lệ |

---

## 2. Bảng Quyết định (Decision Table) & Rút gọn

### 2.1. Bảng quyết định đầy đủ (12 quy tắc)

Điều kiện gồm 3 chiều: **Risk** (3 mức) × **Income** (2 nhóm) × **Employment** (2 loại) = **12 kịch bản**.

| Điều kiện | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **C1**: Risk = High | ✓ | ✓ | ✓ | ✓ | – | – | – | – | – | – | – | – |
| **C2**: Risk = Medium | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | – | – | – |
| **C3**: Risk = Low | – | – | – | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ |
| **C4**: income < 15.0 | ✓ | ✓ | – | – | ✓ | ✓ | – | – | ✓ | ✓ | – | – |
| **C5**: Employment = Contract | ✓ | – | ✓ | – | ✓ | – | ✓ | – | ✓ | – | ✓ | – |
| **Kết quả** | ❌ REJECT | ❌ REJECT | ❌ REJECT | ❌ REJECT | ❌ REJECT | ❌ REJECT | ✅ APPROVE | 🔄 MANUAL | 🔄 MANUAL | ❌ REJECT | ✅ APPROVE | 🔄 MANUAL |

### 2.2. Bảng quyết định sau khi rút gọn (6 quy tắc)

Áp dụng kỹ thuật **gộp điều kiện "Don't Care" (–)** để rút gọn các quy tắc có cùng kết quả:

| Quy tắc rút gọn | C1: Risk | C2: Income | C3: Employment | Kết quả | Gộp từ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **R1** | **High** | **Bất kỳ** | **Bất kỳ** | ❌ **REJECT** | R1+R2+R3+R4 |
| **R2** | **Medium** | **< 15.0** | **Bất kỳ** | ❌ **REJECT** | R5+R6 |
| **R3** | **Low** | **< 15.0** | **Freelance** | ❌ **REJECT** | R10 |
| **R4** | **Low** | **< 15.0** | **Contract** | 🔄 **MANUAL REVIEW** | R9 |
| **R5** | **Medium/Low** | **≥ 15.0** | **Contract** | ✅ **APPROVE** | R7+R11 |
| **R6** | **Medium/Low** | **≥ 15.0** | **Freelance** | 🔄 **MANUAL REVIEW** | R8+R12 |

> **Kết quả rút gọn:** Từ **12 quy tắc → 6 quy tắc tối thiểu** cần kiểm thử.

---

## 3. Danh sách Test Cases hoàn chỉnh

Bộ test suite gồm **51 test cases** chia thành 10 nhóm:

### Nhóm 1–4: Kiểm thử Invalid Input (28 test cases)

| STT | Tên Test Case | Đầu vào | Kết quả mong đợi | Kỹ thuật |
|:---:|---|:---:|:---:|:---:|
| 1 | `test_age_below_min_boundary` | age=17 | `Invalid Input` | BVA |
| 2 | `test_age_at_min_boundary` | age=18 | ≠ Invalid | BVA |
| 3 | `test_age_above_max_boundary` | age=66 | `Invalid Input` | BVA |
| 4 | `test_age_at_max_boundary` | age=65 | ≠ Invalid | BVA |
| 5 | `test_age_zero` | age=0 | `Invalid Input` | BVA |
| 6 | `test_age_negative` | age=-5 | `Invalid Input` | EP |
| 7 | `test_age_wrong_type_float` | age=25.5 | `Invalid Input` | EP |
| 8 | `test_age_wrong_type_string` | age="30" | `Invalid Input` | EP |
| 9 | `test_age_wrong_type_bool` | age=True | `Invalid Input` | EP |
| 10 | `test_income_below_min_boundary` | income=4.9 | `Invalid Input` | BVA |
| 11 | `test_income_at_min_boundary` | income=5.0 | ≠ Invalid | BVA |
| 12 | `test_income_above_max_boundary` | income=500.1 | `Invalid Input` | BVA |
| 13 | `test_income_at_max_boundary` | income=500.0 | ≠ Invalid | BVA |
| 14 | `test_income_negative` | income=-10.0 | `Invalid Input` | EP |
| 15 | `test_income_wrong_type_string` | income="100" | `Invalid Input` | EP |
| 16 | `test_income_wrong_type_bool` | income=True | `Invalid Input` | EP |
| 17 | `test_credit_score_below_min_boundary` | cs=299 | `Invalid Input` | BVA |
| 18 | `test_credit_score_at_min_boundary` | cs=300 | ≠ Invalid | BVA |
| 19 | `test_credit_score_above_max_boundary` | cs=851 | `Invalid Input` | BVA |
| 20 | `test_credit_score_at_max_boundary` | cs=850 | ≠ Invalid | BVA |
| 21 | `test_credit_score_wrong_type_float` | cs=650.5 | `Invalid Input` | EP |
| 22 | `test_credit_score_wrong_type_bool` | cs=True | `Invalid Input` | EP |
| 23 | `test_employment_invalid_value` | emp="A" | `Invalid Input` | EP |
| 24 | `test_employment_lowercase` | emp="c" | `Invalid Input` | EP |
| 25 | `test_employment_empty_string` | emp="" | `Invalid Input` | EP |
| 26 | `test_employment_wrong_type_int` | emp=1 | `Invalid Input` | EP |

### Nhóm 5–10: Kiểm thử Logic Nghiệp vụ (25 test cases)

| STT | Tên Test Case | Đầu vào chính | Kết quả mong đợi | Quy tắc | Kỹ thuật |
|:---:|---|:---:|:---:|:---:|:---:|
| 27 | `test_rule_R1_high_risk_contract_low_income` | cs=400, inc=10.0, C | `REJECT` | R1 | DT |
| 28 | `test_rule_R1_high_risk_freelance_low_income` | cs=400, inc=10.0, F | `REJECT` | R1 | DT |
| 29 | `test_rule_R1_high_risk_contract_high_income` | cs=400, inc=200.0, C | `REJECT` | R1 | DT |
| 30 | `test_rule_R1_high_risk_freelance_high_income` | cs=400, inc=200.0, F | `REJECT` | R1 | DT |
| 31 | `test_rule_R1_credit_score_at_high_boundary_500` | cs=500, inc=200.0, C | `REJECT` | R1 | BVA+DT |
| 32 | `test_rule_R2_medium_risk_contract_low_income` | cs=600, inc=10.0, C | `REJECT` | R2 | DT |
| 33 | `test_rule_R2_medium_risk_freelance_low_income` | cs=600, inc=10.0, F | `REJECT` | R2 | DT |
| 34 | `test_rule_R2_credit_score_at_medium_lower_501` | cs=501, inc=10.0, C | `REJECT` | R2 | BVA+DT |
| 35 | `test_rule_R3_low_risk_freelance_low_income` | cs=750, inc=10.0, F | `REJECT` | R3 | DT |
| 36 | `test_rule_R3_income_at_boundary_14_9` | cs=750, inc=14.9, F | `REJECT` | R3 | BVA+DT |
| 37 | `test_rule_R4_low_risk_contract_low_income` | cs=750, inc=10.0, C | `MANUAL REVIEW` | R4 | DT |
| 38 | `test_rule_R4_income_at_boundary_5_0` | cs=750, inc=5.0, C | `MANUAL REVIEW` | R4 | BVA+DT |
| 39 | `test_rule_R4_income_at_boundary_14_9` | cs=750, inc=14.9, C | `MANUAL REVIEW` | R4 | BVA+DT |
| 40 | `test_rule_R4_credit_score_at_low_boundary_701` | cs=701, inc=10.0, C | `MANUAL REVIEW` | R4 | BVA+DT |
| 41 | `test_rule_R5_medium_risk_contract_high_income` | cs=600, inc=50.0, C | `APPROVE` | R5 | DT |
| 42 | `test_rule_R5_low_risk_contract_high_income` | cs=750, inc=50.0, C | `APPROVE` | R5 | DT |
| 43 | `test_rule_R5_income_at_boundary_15_0` | cs=750, inc=15.0, C | `APPROVE` | R5 | BVA+DT |
| 44 | `test_rule_R5_income_at_boundary_15_1` | cs=600, inc=15.1, C | `APPROVE` | R5 | BVA+DT |
| 45 | `test_rule_R5_income_at_max_500` | cs=750, inc=500.0, C | `APPROVE` | R5 | BVA+DT |
| 46 | `test_rule_R5_credit_score_at_medium_upper_700` | cs=700, inc=50.0, C | `APPROVE` | R5 | BVA+DT |
| 47 | `test_rule_R5_credit_score_at_low_upper_850` | cs=850, inc=50.0, C | `APPROVE` | R5 | BVA+DT |
| 48 | `test_rule_R6_medium_risk_freelance_high_income` | cs=600, inc=50.0, F | `MANUAL REVIEW` | R6 | DT |
| 49 | `test_rule_R6_low_risk_freelance_high_income` | cs=750, inc=50.0, F | `MANUAL REVIEW` | R6 | DT |
| 50 | `test_rule_R6_income_at_boundary_15_0` | cs=750, inc=15.0, F | `MANUAL REVIEW` | R6 | BVA+DT |
| 51 | `test_rule_R6_credit_score_at_medium_lower_501` | cs=501, inc=50.0, F | `MANUAL REVIEW` | R6 | BVA+DT |

---

## 4. Mã nguồn & Kết quả Kiểm thử

### 4.1. Mã nguồn module phân loại ([loan.py](file:///d:/CMPM/BaiTapCNPM/GS25/loan.py))

```python
def loan_decision(age, income, credit_score, employment):
    # --- 1. Kiểm tra ràng buộc dữ liệu ---
    if not isinstance(age, int) or isinstance(age, bool):
        return "Invalid Input"
    if not (18 <= age <= 65):
        return "Invalid Input"

    if isinstance(income, bool) or not isinstance(income, (int, float)):
        return "Invalid Input"
    income_rounded = round(float(income), 1)
    if not (5.0 <= income_rounded <= 500.0):
        return "Invalid Input"

    if not isinstance(credit_score, int) or isinstance(credit_score, bool):
        return "Invalid Input"
    if not (300 <= credit_score <= 850):
        return "Invalid Input"

    if employment not in ("C", "F"):
        return "Invalid Input"

    # --- 2. Phân loại rủi ro tín dụng ---
    if credit_score <= 500:
        risk = "High"
    elif credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # --- 3. Áp dụng quy tắc nghiệp vụ ---
    if risk == "High":                                     # R1
        return "REJECT"
    if income_rounded < 15.0:
        if employment == "C" and risk == "Low":            # R4
            return "MANUAL REVIEW"
        return "REJECT"                                    # R2, R3
    if employment == "C":                                  # R5
        return "APPROVE"
    return "MANUAL REVIEW"                                 # R6
```

### 4.2. Kết quả kiểm thử ([test_loan.py](file:///d:/CMPM/BaiTapCNPM/GS25/test_loan.py))

```
python -m unittest -v test_loan.py
```

```text
test_age_at_max_boundary ... ok
test_age_at_min_boundary ... ok
test_age_below_min_boundary ... ok
test_age_above_max_boundary ... ok
test_age_negative ... ok
test_age_wrong_type_bool ... ok
test_age_wrong_type_float ... ok
test_age_wrong_type_string ... ok
test_age_zero ... ok
test_credit_score_above_max_boundary ... ok
test_credit_score_at_max_boundary ... ok
test_credit_score_at_min_boundary ... ok
test_credit_score_below_min_boundary ... ok
test_credit_score_wrong_type_bool ... ok
test_credit_score_wrong_type_float ... ok
test_employment_empty_string ... ok
test_employment_invalid_value ... ok
test_employment_lowercase ... ok
test_employment_wrong_type_int ... ok
test_income_above_max_boundary ... ok
test_income_at_max_boundary ... ok
test_income_at_min_boundary ... ok
test_income_below_min_boundary ... ok
test_income_negative ... ok
test_income_wrong_type_bool ... ok
test_income_wrong_type_string ... ok
test_rule_R1_credit_score_at_high_boundary_500 ... ok
test_rule_R1_high_risk_contract_high_income ... ok
test_rule_R1_high_risk_contract_low_income ... ok
test_rule_R1_high_risk_freelance_high_income ... ok
test_rule_R1_high_risk_freelance_low_income ... ok
test_rule_R2_credit_score_at_medium_lower_boundary_501 ... ok
test_rule_R2_medium_risk_contract_low_income ... ok
test_rule_R2_medium_risk_freelance_low_income ... ok
test_rule_R3_income_at_boundary_14_9 ... ok
test_rule_R3_low_risk_freelance_low_income ... ok
test_rule_R4_credit_score_at_low_boundary_701 ... ok
test_rule_R4_income_at_boundary_14_9 ... ok
test_rule_R4_income_at_boundary_5_0 ... ok
test_rule_R4_low_risk_contract_low_income ... ok
test_rule_R5_credit_score_at_low_upper_boundary_850 ... ok
test_rule_R5_credit_score_at_medium_upper_boundary_700 ... ok
test_rule_R5_income_at_boundary_15_0 ... ok
test_rule_R5_income_at_boundary_15_1 ... ok
test_rule_R5_income_at_max_500 ... ok
test_rule_R5_low_risk_contract_high_income ... ok
test_rule_R5_medium_risk_contract_high_income ... ok
test_rule_R6_credit_score_at_medium_lower_boundary_501 ... ok
test_rule_R6_income_at_boundary_15_0 ... ok
test_rule_R6_low_risk_freelance_high_income ... ok
test_rule_R6_medium_risk_freelance_high_income ... ok
----------------------------------------------------------------------
Ran 51 tests in 0.006s

OK
```

### 4.3. Tổng kết kết quả

| Chỉ số | Giá trị |
|---|:---:|
| **Tổng số test cases** | **51** |
| **Passed** | **51 / 51** |
| **Failed / Errors** | **0** |
| **Tỷ lệ thành công** | **100%** |
| Thời gian chạy | 0.006s |

| Nhóm kiểm thử | Số test | Passed |
|---|:---:|:---:|
| Invalid Input – `age` | 9 | 9 ✅ |
| Invalid Input – `income` | 7 | 7 ✅ |
| Invalid Input – `credit_score` | 6 | 6 ✅ |
| Invalid Input – `employment` | 4 | 4 ✅ |
| R1 – High Risk → REJECT | 5 | 5 ✅ |
| R2 – Medium + income<15 → REJECT | 3 | 3 ✅ |
| R3 – Low + income<15 + Freelance → REJECT | 2 | 2 ✅ |
| R4 – Low + income<15 + Contract → MANUAL REVIEW | 4 | 4 ✅ |
| R5 – (Med/Low) + income≥15 + Contract → APPROVE | 7 | 7 ✅ |
| R6 – (Med/Low) + income≥15 + Freelance → MANUAL REVIEW | 4 | 4 ✅ |
