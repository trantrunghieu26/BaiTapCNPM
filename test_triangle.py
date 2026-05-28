import unittest
from triangle import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    
    # ==========================================
    # 1. KIỂM THỬ GIÁ TRỊ KHÔNG HỢP LỆ (INVALID INPUT)
    # ==========================================
    
    def test_invalid_input_zero_value(self):
        """Kiểm thử giá trị biên dưới vi phạm (bằng 0)"""
        self.assertEqual(classify_triangle(0, 50, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, 0, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, 50, 0), "Invalid Input")
        self.assertEqual(classify_triangle(0, 0, 0), "Invalid Input")

    def test_invalid_input_negative_value(self):
        """Kiểm thử giá trị biên dưới vi phạm (số âm)"""
        self.assertEqual(classify_triangle(-1, 50, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, -5, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, 50, -10), "Invalid Input")
        self.assertEqual(classify_triangle(-2, -3, -4), "Invalid Input")

    def test_invalid_input_exceed_max_value(self):
        """Kiểm thử giá trị biên trên vi phạm (lớn hơn 100)"""
        self.assertEqual(classify_triangle(101, 50, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, 105, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, 50, 150), "Invalid Input")
        self.assertEqual(classify_triangle(101, 101, 101), "Invalid Input")

    def test_invalid_input_wrong_data_types(self):
        """Kiểm thử sai kiểu dữ liệu (số thực, chuỗi, boolean, None)"""
        self.assertEqual(classify_triangle(1.5, 50, 50), "Invalid Input")
        self.assertEqual(classify_triangle("50", 50, 50), "Invalid Input")
        self.assertEqual(classify_triangle(50, True, 50), "Invalid Input")  # Boolean không hợp lệ
        self.assertEqual(classify_triangle(50, 50, None), "Invalid Input")

    # ==========================================
    # 2. KIỂM THỬ GIÁ TRỊ BIÊN TRONG KHOẢNG HỢP LỆ [1, 100]
    # ==========================================
    
    def test_boundary_valid_lower_limit(self):
        """Kiểm thử giá trị biên dưới hợp lệ (bằng 1 và 2)"""
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")  # Biên dưới cực tiểu
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral")  # Lân cận biên dưới

    def test_boundary_valid_upper_limit(self):
        """Kiểm thử giá trị biên trên hợp lệ (bằng 99 và 100)"""
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")  # Biên trên cực đại
        self.assertEqual(classify_triangle(99, 99, 99), "Equilateral")  # Lân cận biên trên

    def test_boundary_valid_nominal_value(self):
        """Kiểm thử giá trị thông thường (Nominal = 50)"""
        self.assertEqual(classify_triangle(50, 50, 50), "Equilateral")

    # ==========================================
    # 3. KIỂM THỬ KHÔNG PHẢI TAM GIÁC (NOT A TRIANGLE)
    # ==========================================
    
    def test_not_a_triangle_sum_equals_third_side(self):
        """Kiểm thử tổng hai cạnh bằng cạnh còn lại (a + b = c, a + c = b, b + c = a)"""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a Triangle")
        self.assertEqual(classify_triangle(1, 3, 2), "Not a Triangle")
        self.assertEqual(classify_triangle(3, 1, 2), "Not a Triangle")

    def test_not_a_triangle_sum_less_than_third_side(self):
        """Kiểm thử tổng hai cạnh nhỏ hơn cạnh còn lại (a + b < c, a + c < b, b + c < a)"""
        self.assertEqual(classify_triangle(1, 2, 4), "Not a Triangle")
        self.assertEqual(classify_triangle(1, 5, 2), "Not a Triangle")
        self.assertEqual(classify_triangle(6, 2, 3), "Not a Triangle")

    # ==========================================
    # 4. KIỂM THỬ PHÂN LOẠI TAM GIÁC HỢP LỆ (EQUILATERAL, ISOSCELES, SCALENE)
    # ==========================================

    def test_triangle_type_equilateral(self):
        """Kiểm thử Tam giác đều (Equilateral)"""
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")
        self.assertEqual(classify_triangle(88, 88, 88), "Equilateral")

    def test_triangle_type_isosceles(self):
        """Kiểm thử Tam giác cân (Isosceles)"""
        # Cân tại a = b
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
        # Cân tại b = c
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")
        # Cân tại a = c
        self.assertEqual(classify_triangle(5, 8, 5), "Isosceles")
        # Biên dưới tam giác cân
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
        # Biên trên tam giác cân
        self.assertEqual(classify_triangle(100, 100, 99), "Isosceles")

    def test_triangle_type_scalene(self):
        """Kiểm thử Tam giác thường (Scalene)"""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")
        self.assertEqual(classify_triangle(10, 11, 20), "Scalene")
        self.assertEqual(classify_triangle(90, 80, 70), "Scalene")

if __name__ == "__main__":
    unittest.main()
