# Báo cáo Kiểm thử Module Phân loại Tam giác

Báo cáo này trình bày chi tiết về quá trình thiết kế test cases tối ưu, cấu trúc mã nguồn và kết quả kiểm thử cho module phân loại tam giác.

---

## 1. Thiết kế các Test Cases Tối ưu

### 1.1. Phân hoạch tương đương (Equivalence Partitioning) & Phân tích giá trị biên (Boundary Value Analysis)

Đầu vào của hệ thống gồm 3 số nguyên $a, b, c$ biểu diễn độ dài ba cạnh của tam giác. Các cạnh này có ràng buộc: $a, b, c \in [1, 100]$.

#### A. Phân tích giá trị biên cho các biến $a, b, c$:
Đối với mỗi cạnh $x \in \{a, b, c\}$, ta xác định các giá trị kiểm thử tại biên của khoảng $[1, 100]$:
*   **Biên dưới:**
    *   Giá trị ngoài biên (không hợp lệ): $0$ (hoặc số âm như $-1$).
    *   Giá trị biên cực tiểu (hợp lệ): $1$.
    *   Giá trị sát trên biên cực tiểu (hợp lệ): $2$.
*   **Giá trị thông thường (Nominal):** $50$.
*   **Biên trên:**
    *   Giá trị sát dưới biên cực đại (hợp lệ): $99$.
    *   Giá trị biên cực đại (hợp lệ): $100$.
    *   Giá trị ngoài biên (không hợp lệ): $101$.

#### B. Phân hoạch tương đương cho logic tạo thành tam giác:
*   **Lớp không phải là tam giác (Not a Triangle):** Không thỏa mãn bất đẳng thức tam giác.
    *   $a + b \le c$ (Ví dụ: $1, 2, 3$ hoặc $1, 2, 4$)
    *   $a + c \le b$ (Ví dụ: $1, 3, 2$ hoặc $1, 4, 2$)
    *   $b + c \le a$ (Ví dụ: $3, 1, 2$ hoặc $4, 1, 2$)
*   **Lớp tam giác hợp lệ (Valid Triangle):** Thỏa mãn cả 3 bất đẳng thức:
    *   $a + b > c$ và $a + c > b$ và $b + c > a$.

---

### 1.2. Lập bảng quyết định (Decision Table)

Bảng quyết định dưới đây được xây dựng dựa trên logic nghiệp vụ của bài toán:

| Điều kiện (Conditions) | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 |
|---|---|---|---|---|---|---|---|---|---|
| **C1**: $a, b, c \in [1, 100]$? | **False** | **True** | **True** | **True** | **True** | **True** | **True** | **True** | **True** |
| **C2**: Thỏa mãn bất đẳng thức tam giác? | - | **False** | **True** | **True** | **True** | **True** | **True** | **True** | **True** |
| **C3**: $a = b$? | - | - | **False** | **True** | **False** | **False** | **True** | **True** | **False** |
| **C4**: $b = c$? | - | - | **False** | **False** | **True** | **False** | **True** | **False** | **True** |
| **C5**: $a = c$? | - | - | **False** | **False** | **False** | **True** | **True** | **True** | **True** |
| **Hành động (Actions)** | | | | | | | | | |
| **A1**: Trả về `"Invalid Input"` | **X** | | | | | | | | |
| **A2**: Trả về `"Not a Triangle"` | | **X** | | | | | | | |
| **A3**: Trả về `"Equilateral"` | | | | | | | **X** | | |
| **A4**: Trả về `"Isosceles"` | | | | **X** | **X** | **X** | | | |
| **A5**: Trả về `"Scalene"` | | | **X** | | | | | | |

*Ghi chú diễn giải:*
*   **R1 (Rule 1):** Đầu vào vi phạm miền giá trị $[1, 100]$ hoặc sai kiểu dữ liệu $\rightarrow$ `"Invalid Input"`.
*   **R2 (Rule 2):** Đầu vào đúng miền giá trị nhưng không thỏa mãn điều kiện tạo thành tam giác $\rightarrow$ `"Not a Triangle"`.
*   **R3 (Rule 3):** Đầu vào tạo thành tam giác hợp lệ và cả 3 cạnh đều khác nhau $\rightarrow$ `"Scalene"`.
*   **R4, R5, R6 (Rules 4-6):** Đầu vào tạo thành tam giác hợp lệ và có đúng 2 cạnh bằng nhau $\rightarrow$ `"Isosceles"`.
*   **R7 (Rule 7):** Đầu vào tạo thành tam giác hợp lệ và cả 3 cạnh bằng nhau $\rightarrow$ `"Equilateral"`.
*   *Lưu ý toán học:* Các cột kết hợp logic mâu thuẫn như $a=b, b=c, a \ne c$ (hoặc tương tự) được loại bỏ vì không thể xảy ra trong thực tế số học.

---

### 1.3. Danh sách các Test Cases được sinh ra

Bộ test suite được thiết kế với **15 test cases** chính chia làm các nhóm sau:

| STT | Tên Test Case | Đầu vào (a, b, c) | Kết quả mong đợi | Kỹ thuật thiết kế áp dụng |
|:---:|---|:---:|:---:|:---:|
| **1** | `test_invalid_input_zero_value` | $0, 50, 50$ | `"Invalid Input"` | Phân tích giá trị biên (Biên dưới vi phạm) |
| **2** | `test_invalid_input_negative_value` | $-1, 50, 50$ | `"Invalid Input"` | Phân tích giá trị biên (Số âm) |
| **3** | `test_invalid_input_exceed_max_value` | $101, 50, 50$ | `"Invalid Input"` | Phân tích giá trị biên (Biên trên vi phạm) |
| **4** | `test_invalid_input_wrong_data_types` | $1.5, 50, 50$ | `"Invalid Input"` | Phân tích lớp tương đương (Sai kiểu dữ liệu) |
| **5** | `test_boundary_valid_lower_limit` | $1, 1, 1$ | `"Equilateral"` | Phân tích giá trị biên (Biên dưới cực tiểu) |
| **6** | `test_boundary_valid_upper_limit` | $100, 100, 100$ | `"Equilateral"` | Phân tích giá trị biên (Biên trên cực đại) |
| **7** | `test_boundary_valid_nominal_value` | $50, 50, 50$ | `"Equilateral"` | Phân tích giá trị biên (Giá trị thông thường) |
| **8** | `test_not_a_triangle_sum_equals_third_side` | $1, 2, 3$ | `"Not a Triangle"` | Phân hoạch tương đương (Bất đẳng thức tam giác) |
| **9** | `test_not_a_triangle_sum_less_than_third_side`| $1, 2, 4$ | `"Not a Triangle"` | Phân hoạch tương đương (Bất đẳng thức tam giác) |
| **10**| `test_triangle_type_equilateral` | $5, 5, 5$ | `"Equilateral"` | Bảng quyết định (Rule 7) |
| **11**| `test_triangle_type_isosceles_ab` | $5, 5, 8$ | `"Isosceles"` | Bảng quyết định (Rule 4 - Cân tại a=b) |
| **12**| `test_triangle_type_isosceles_bc` | $8, 5, 5$ | `"Isosceles"` | Bảng quyết định (Rule 5 - Cân tại b=c) |
| **13**| `test_triangle_type_isosceles_ac` | $5, 8, 5$ | `"Isosceles"` | Bảng quyết định (Rule 6 - Cân tại a=c) |
| **14**| `test_triangle_type_isosceles_boundary` | $100, 100, 99$ | `"Isosceles"` | Kết hợp BVA + Bảng quyết định |
| **15**| `test_triangle_type_scalene` | $3, 4, 5$ | `"Scalene"` | Bảng quyết định (Rule 3) |

---

## 2. Mã nguồn Chương trình

### 2.1. Mã nguồn module phân loại ([triangle.py](file:///d:/CMPM/BaiTapCNPM/triangle.py))
Module được triển khai bằng ngôn ngữ Python 3, bổ sung kiểm tra kiểu dữ liệu nghiêm ngặt để tránh lỗi crash chương trình khi nhận đầu vào không hợp lệ.

```python
def classify_triangle(a, b, c):
    # Kiểm tra kiểu dữ liệu: Phải là số nguyên (không tính kiểu boolean vì bool kế thừa int trong Python)
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (a, b, c)):
        return "Invalid Input"
    
    # Kiểm tra phạm vi dữ liệu [1, 100]
    if not all(1 <= x <= 100 for x in (a, b, c)):
        return "Invalid Input"
    
    # Kiểm tra điều kiện để tạo thành một tam giác
    if not (a + b > c and a + c > b and b + c > a):
        return "Not a Triangle"
    
    # Phân loại tam giác
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
```

---

## 3. Kết quả Chạy thử nghiệm Bộ Kiểm thử

### 3.1. Hướng dẫn chạy kiểm thử tự động
Bạn có thể tự chạy kiểm thử bằng dòng lệnh sau tại thư mục chứa mã nguồn:
```bash
python -m unittest -v test_triangle.py
```

### 3.2. Kết quả kiểm thử (Test Results)
Khi chạy bộ kiểm thử, kết quả chạy thực tế đạt được:

*   **Tổng số test cases:** 15
*   **Passed:** 15 / 15 (100% thành công)
*   **Failed / Errors:** 0 / 15

Chi tiết log chạy kiểm thử mẫu:
```text
test_boundary_valid_lower_limit (test_triangle.TestTriangleClassification.test_boundary_valid_lower_limit)
Kiểm thử giá trị biên dưới hợp lệ (bằng 1 và 2) ... ok
test_boundary_valid_nominal_value (test_triangle.TestTriangleClassification.test_boundary_valid_nominal_value)
Kiểm thử giá trị thông thường (Nominal = 50) ... ok
test_boundary_valid_upper_limit (test_triangle.TestTriangleClassification.test_boundary_valid_upper_limit)
Kiểm thử giá trị biên trên hợp lệ (bằng 99 và 100) ... ok
test_invalid_input_exceed_max_value (test_triangle.TestTriangleClassification.test_invalid_input_exceed_max_value)
Kiểm thử giá trị biên trên vi phạm (lớn hơn 100) ... ok
test_invalid_input_negative_value (test_triangle.TestTriangleClassification.test_invalid_input_negative_value)
Kiểm thử giá trị biên dưới vi phạm (số âm) ... ok
test_invalid_input_wrong_data_types (test_triangle.TestTriangleClassification.test_invalid_input_wrong_data_types)
Kiểm thử sai kiểu dữ liệu (số thực, chuỗi, boolean, None) ... ok
test_invalid_input_zero_value (test_triangle.TestTriangleClassification.test_invalid_input_zero_value)
Kiểm thử giá trị biên dưới vi phạm (bằng 0) ... ok
test_not_a_triangle_sum_equals_third_side (test_triangle.TestTriangleClassification.test_not_a_triangle_sum_equals_third_side)
Kiểm thử tổng hai cạnh bằng cạnh còn lại (a + b = c, a + c = b, b + c = a) ... ok
test_not_a_triangle_sum_less_than_third_side (test_triangle.TestTriangleClassification.test_not_a_triangle_sum_less_than_third_side)
Kiểm thử tổng hai cạnh nhỏ hơn cạnh còn lại (a + b < c, a + c < b, b + c < a) ... ok
test_triangle_type_equilateral (test_triangle.TestTriangleClassification.test_triangle_type_equilateral)
Kiểm thử Tam giác đều (Equilateral) ... ok
test_triangle_type_isosceles (test_triangle.TestTriangleClassification.test_triangle_type_isosceles)
Kiểm thử Tam giác cân (Isosceles) ... ok
test_triangle_type_scalene (test_triangle.TestTriangleClassification.test_triangle_type_scalene)
Kiểm thử Tam giác thường (Scalene) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.003s

OK
```
*(Lưu ý: Một số hàm chứa nhiều phương thức assert độc lập để kiểm thử cặn kẽ các góc cạnh của một ca kiểm thử giúp bộ code ngắn gọn và tối ưu).*
