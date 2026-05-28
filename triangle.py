def classify_triangle(a, b, c):
    """
    Phân loại tam giác dựa trên độ dài 3 cạnh a, b, c.
    
    Ràng buộc:
    - a, b, c phải là số nguyên dương trong khoảng [1, 100].
      Nếu vi phạm, trả về "Invalid Input".
      
    Logic nghiệp vụ:
    - Nếu không thỏa mãn bất đẳng thức tam giác, trả về "Not a Triangle".
    - Tam giác đều: a == b == c -> "Equilateral"
    - Tam giác cân: a == b hoặc b == c hoặc a == c -> "Isosceles"
    - Tam giác thường: a != b != c -> "Scalene"
    """
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
