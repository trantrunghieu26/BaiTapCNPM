Một module phần mềm nhận đầu vào là 3 số nguyên a, b, c đại diện cho chiều dài 3 cạnh của một tam giác. Hệ thống sẽ phân tích và trả về loại tam giác tương ứng.
- Ràng buộc dữ liệu đầu vào: a, b, c phải là các số nguyên dương nằm trong khoảng từ 1 đến 100. Nếu bất kỳ giá trị nào vi phạm, hệ thống báo lỗi "Invalid Input".
- Logic nghiệp vụ:
+ Để tạo thành một tam giác, tổng độ dài 2 cạnh bất kỳ phải luôn lớn hơn cạnh còn lại (a+b>c và a+c>b và b+c>a). Nếu không thỏa mãn, trả về "Not a Triangle" (Không phải tam giác).
+ Nếu là một tam giác hợp lệ, phân loại như sau:
+ Nếu 3 cạnh bằng nhau (a=b và b=c): Trả về "Equilateral" (Tam giác đều).
+ Nếu chỉ có 2 cạnh bằng nhau (a=b hoặc b=c hoặc a=c): Trả về "Isosceles" (Tam giác cân).
+ Nếu 3 cạnh đều khác nhau: Trả về "Scalene" (Tam giác thường).
Yêu cầu: 
1. Thiết kế các test cases tối ưu để kiểm thử module này theo các bước sau:
+ Sử dụng phân hoạch tương đương và giá trị biên cho đầu vào
+ Lập bảng quyết định dựa trên logic nghiệp vụ
+ Tạo test cases dựa trên thông tin từ 2 ý trên
2. Viết code và chạy code với test suite trên để xem bao nhiêu cái passed?
3. Push code, test và report lên github cá nhân