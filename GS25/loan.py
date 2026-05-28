def loan_decision(age, income, credit_score, employment):
    """
    Phê duyệt khoản vay cá nhân của Ngân hàng CS2045.

    Tham số:
    - age (int): Tuổi khách hàng, hợp lệ trong [18, 65].
    - income (float): Thu nhập (triệu VNĐ), làm tròn 1 chữ số thập phân, hợp lệ trong [5.0, 500.0].
    - credit_score (int): Điểm tín dụng, hợp lệ trong [300, 850].
    - employment (str): Loại việc làm, chỉ nhận "C" (Contract) hoặc "F" (Freelance).

    Trả về:
    - "Invalid Input"  nếu bất kỳ tham số nào vi phạm ràng buộc.
    - "REJECT"         nếu khoản vay bị từ chối.
    - "MANUAL REVIEW"  nếu hồ sơ cần thẩm định thủ công.
    - "APPROVE"        nếu khoản vay được phê duyệt.
    """

    # --- 1. Kiểm tra ràng buộc dữ liệu ---

    # age: phải là số nguyên (không phải bool), trong [18, 65]
    if not isinstance(age, int) or isinstance(age, bool):
        return "Invalid Input"
    if not (18 <= age <= 65):
        return "Invalid Input"

    # income: phải là số thực hoặc nguyên (không phải bool), trong [5.0, 500.0]
    if isinstance(income, bool) or not isinstance(income, (int, float)):
        return "Invalid Input"
    income_rounded = round(float(income), 1)
    if not (5.0 <= income_rounded <= 500.0):
        return "Invalid Input"

    # credit_score: phải là số nguyên (không phải bool), trong [300, 850]
    if not isinstance(credit_score, int) or isinstance(credit_score, bool):
        return "Invalid Input"
    if not (300 <= credit_score <= 850):
        return "Invalid Input"

    # employment: chỉ nhận "C" hoặc "F"
    if employment not in ("C", "F"):
        return "Invalid Input"

    # --- 2. Phân loại rủi ro tín dụng dựa trên credit_score ---
    if credit_score <= 500:
        risk = "High"
    elif credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # --- 3. Áp dụng quy tắc nghiệp vụ ---

    # Quy tắc 1: High Risk luôn bị REJECT
    if risk == "High":
        return "REJECT"

    # Quy tắc 2 & 3: income < 15.0
    if income_rounded < 15.0:
        # Chỉ MANUAL REVIEW khi: Contract VÀ Low Risk
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"
        # Còn lại (Freelance bất kỳ risk, hoặc Medium Risk bất kỳ employment) -> REJECT
        return "REJECT"

    # Quy tắc 4 & 5: income >= 15.0, risk là Medium hoặc Low
    if employment == "C":
        return "APPROVE"
    else:  # employment == "F"
        return "MANUAL REVIEW"
