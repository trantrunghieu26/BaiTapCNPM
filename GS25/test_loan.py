import unittest
from loan import loan_decision

class TestLoanDecision(unittest.TestCase):

    # =====================================================================
    # NHÓM 1: KIỂM THỬ INVALID INPUT - THAM SỐ age
    # =====================================================================

    def test_age_below_min_boundary(self):
        """BVA: age = 17 (dưới biên tối thiểu 18) -> Invalid Input"""
        self.assertEqual(loan_decision(17, 100.0, 750, "C"), "Invalid Input")

    def test_age_at_min_boundary(self):
        """BVA: age = 18 (biên tối thiểu hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(18, 100.0, 750, "C"), "Invalid Input")

    def test_age_above_max_boundary(self):
        """BVA: age = 66 (trên biên tối đa 65) -> Invalid Input"""
        self.assertEqual(loan_decision(66, 100.0, 750, "C"), "Invalid Input")

    def test_age_at_max_boundary(self):
        """BVA: age = 65 (biên tối đa hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(65, 100.0, 750, "C"), "Invalid Input")

    def test_age_zero(self):
        """BVA: age = 0 (ngoài biên dưới) -> Invalid Input"""
        self.assertEqual(loan_decision(0, 100.0, 750, "C"), "Invalid Input")

    def test_age_negative(self):
        """EP: age âm (-5) -> Invalid Input"""
        self.assertEqual(loan_decision(-5, 100.0, 750, "C"), "Invalid Input")

    def test_age_wrong_type_float(self):
        """EP: age là số thực (sai kiểu) -> Invalid Input"""
        self.assertEqual(loan_decision(25.5, 100.0, 750, "C"), "Invalid Input")

    def test_age_wrong_type_string(self):
        """EP: age là chuỗi (sai kiểu) -> Invalid Input"""
        self.assertEqual(loan_decision("30", 100.0, 750, "C"), "Invalid Input")

    def test_age_wrong_type_bool(self):
        """EP: age là bool (sai kiểu, bool kế thừa int) -> Invalid Input"""
        self.assertEqual(loan_decision(True, 100.0, 750, "C"), "Invalid Input")

    # =====================================================================
    # NHÓM 2: KIỂM THỬ INVALID INPUT - THAM SỐ income
    # =====================================================================

    def test_income_below_min_boundary(self):
        """BVA: income = 4.9 (dưới biên tối thiểu 5.0) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 4.9, 750, "C"), "Invalid Input")

    def test_income_at_min_boundary(self):
        """BVA: income = 5.0 (biên tối thiểu hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(30, 5.0, 750, "C"), "Invalid Input")

    def test_income_above_max_boundary(self):
        """BVA: income = 500.1 (trên biên tối đa 500.0) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 500.1, 750, "C"), "Invalid Input")

    def test_income_at_max_boundary(self):
        """BVA: income = 500.0 (biên tối đa hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(30, 500.0, 750, "C"), "Invalid Input")

    def test_income_negative(self):
        """EP: income âm -> Invalid Input"""
        self.assertEqual(loan_decision(30, -10.0, 750, "C"), "Invalid Input")

    def test_income_wrong_type_string(self):
        """EP: income là chuỗi (sai kiểu) -> Invalid Input"""
        self.assertEqual(loan_decision(30, "100", 750, "C"), "Invalid Input")

    def test_income_wrong_type_bool(self):
        """EP: income là bool -> Invalid Input"""
        self.assertEqual(loan_decision(30, True, 750, "C"), "Invalid Input")

    # =====================================================================
    # NHÓM 3: KIỂM THỬ INVALID INPUT - THAM SỐ credit_score
    # =====================================================================

    def test_credit_score_below_min_boundary(self):
        """BVA: credit_score = 299 (dưới biên tối thiểu 300) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 299, "C"), "Invalid Input")

    def test_credit_score_at_min_boundary(self):
        """BVA: credit_score = 300 (biên tối thiểu hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(30, 100.0, 300, "C"), "Invalid Input")

    def test_credit_score_above_max_boundary(self):
        """BVA: credit_score = 851 (trên biên tối đa 850) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 851, "C"), "Invalid Input")

    def test_credit_score_at_max_boundary(self):
        """BVA: credit_score = 850 (biên tối đa hợp lệ) -> không phải Invalid"""
        self.assertNotEqual(loan_decision(30, 100.0, 850, "C"), "Invalid Input")

    def test_credit_score_wrong_type_float(self):
        """EP: credit_score là số thực (sai kiểu) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 650.5, "C"), "Invalid Input")

    def test_credit_score_wrong_type_bool(self):
        """EP: credit_score là bool -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, True, "C"), "Invalid Input")

    # =====================================================================
    # NHÓM 4: KIỂM THỬ INVALID INPUT - THAM SỐ employment
    # =====================================================================

    def test_employment_invalid_value(self):
        """EP: employment = 'A' (giá trị không hợp lệ) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 750, "A"), "Invalid Input")

    def test_employment_lowercase(self):
        """EP: employment = 'c' (chữ thường, phân biệt hoa/thường) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 750, "c"), "Invalid Input")

    def test_employment_empty_string(self):
        """EP: employment = '' (rỗng) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 750, ""), "Invalid Input")

    def test_employment_wrong_type_int(self):
        """EP: employment là số nguyên (sai kiểu) -> Invalid Input"""
        self.assertEqual(loan_decision(30, 100.0, 750, 1), "Invalid Input")

    # =====================================================================
    # NHÓM 5: KIỂM THỬ LOGIC NGHIỆP VỤ - BẢNG QUYẾT ĐỊNH
    # Quy tắc R1: High Risk -> REJECT (bất kể income, employment)
    # =====================================================================

    def test_rule_R1_high_risk_contract_low_income(self):
        """R1: High Risk + income < 15 + Contract -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 400, "C"), "REJECT")

    def test_rule_R1_high_risk_freelance_low_income(self):
        """R1: High Risk + income < 15 + Freelance -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 400, "F"), "REJECT")

    def test_rule_R1_high_risk_contract_high_income(self):
        """R1: High Risk + income >= 15 + Contract -> REJECT"""
        self.assertEqual(loan_decision(30, 200.0, 400, "C"), "REJECT")

    def test_rule_R1_high_risk_freelance_high_income(self):
        """R1: High Risk + income >= 15 + Freelance -> REJECT"""
        self.assertEqual(loan_decision(30, 200.0, 400, "F"), "REJECT")

    def test_rule_R1_credit_score_at_high_boundary_500(self):
        """BVA + R1: credit_score = 500 (biên trên của High) -> REJECT"""
        self.assertEqual(loan_decision(30, 200.0, 500, "C"), "REJECT")

    # =====================================================================
    # NHÓM 6: KIỂM THỬ LOGIC NGHIỆP VỤ
    # Quy tắc R2: Medium Risk + income < 15 -> REJECT
    # =====================================================================

    def test_rule_R2_medium_risk_contract_low_income(self):
        """R2: Medium Risk + income < 15 + Contract -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 600, "C"), "REJECT")

    def test_rule_R2_medium_risk_freelance_low_income(self):
        """R2: Medium Risk + income < 15 + Freelance -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 600, "F"), "REJECT")

    def test_rule_R2_credit_score_at_medium_lower_boundary_501(self):
        """BVA + R2: credit_score = 501 (biên dưới Medium) + income < 15 -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 501, "C"), "REJECT")

    # =====================================================================
    # NHÓM 7: KIỂM THỬ LOGIC NGHIỆP VỤ
    # Quy tắc R3: Low Risk + income < 15 + Freelance -> REJECT
    # =====================================================================

    def test_rule_R3_low_risk_freelance_low_income(self):
        """R3: Low Risk + income < 15 + Freelance -> REJECT"""
        self.assertEqual(loan_decision(30, 10.0, 750, "F"), "REJECT")

    def test_rule_R3_income_at_boundary_14_9(self):
        """BVA + R3: income = 14.9 (sát dưới biên 15) + Low Risk + Freelance -> REJECT"""
        self.assertEqual(loan_decision(30, 14.9, 750, "F"), "REJECT")

    # =====================================================================
    # NHÓM 8: KIỂM THỬ LOGIC NGHIỆP VỤ
    # Quy tắc R4: Low Risk + income < 15 + Contract -> MANUAL REVIEW
    # =====================================================================

    def test_rule_R4_low_risk_contract_low_income(self):
        """R4: Low Risk + income < 15 + Contract -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 10.0, 750, "C"), "MANUAL REVIEW")

    def test_rule_R4_income_at_boundary_5_0(self):
        """BVA + R4: income = 5.0 (biên dưới hợp lệ) + Low Risk + Contract -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 5.0, 750, "C"), "MANUAL REVIEW")

    def test_rule_R4_income_at_boundary_14_9(self):
        """BVA + R4: income = 14.9 (sát dưới biên 15) + Low Risk + Contract -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 14.9, 750, "C"), "MANUAL REVIEW")

    def test_rule_R4_credit_score_at_low_boundary_701(self):
        """BVA + R4: credit_score = 701 (biên dưới Low Risk) + income < 15 + Contract -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 10.0, 701, "C"), "MANUAL REVIEW")

    # =====================================================================
    # NHÓM 9: KIỂM THỬ LOGIC NGHIỆP VỤ
    # Quy tắc R5: (Medium/Low) Risk + income >= 15 + Contract -> APPROVE
    # =====================================================================

    def test_rule_R5_medium_risk_contract_high_income(self):
        """R5: Medium Risk + income >= 15 + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 50.0, 600, "C"), "APPROVE")

    def test_rule_R5_low_risk_contract_high_income(self):
        """R5: Low Risk + income >= 15 + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 50.0, 750, "C"), "APPROVE")

    def test_rule_R5_income_at_boundary_15_0(self):
        """BVA + R5: income = 15.0 (biên dưới hợp lệ >= 15) + Low Risk + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 15.0, 750, "C"), "APPROVE")

    def test_rule_R5_income_at_boundary_15_1(self):
        """BVA + R5: income = 15.1 (sát trên biên 15) + Medium Risk + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 15.1, 600, "C"), "APPROVE")

    def test_rule_R5_income_at_max_500(self):
        """BVA + R5: income = 500.0 (biên trên hợp lệ) + Low Risk + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 500.0, 750, "C"), "APPROVE")

    def test_rule_R5_credit_score_at_medium_upper_boundary_700(self):
        """BVA + R5: credit_score = 700 (biên trên Medium) + income >= 15 + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 50.0, 700, "C"), "APPROVE")

    def test_rule_R5_credit_score_at_low_upper_boundary_850(self):
        """BVA + R5: credit_score = 850 (biên trên Low) + income >= 15 + Contract -> APPROVE"""
        self.assertEqual(loan_decision(30, 50.0, 850, "C"), "APPROVE")

    # =====================================================================
    # NHÓM 10: KIỂM THỬ LOGIC NGHIỆP VỤ
    # Quy tắc R6: (Medium/Low) Risk + income >= 15 + Freelance -> MANUAL REVIEW
    # =====================================================================

    def test_rule_R6_medium_risk_freelance_high_income(self):
        """R6: Medium Risk + income >= 15 + Freelance -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 50.0, 600, "F"), "MANUAL REVIEW")

    def test_rule_R6_low_risk_freelance_high_income(self):
        """R6: Low Risk + income >= 15 + Freelance -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 50.0, 750, "F"), "MANUAL REVIEW")

    def test_rule_R6_income_at_boundary_15_0(self):
        """BVA + R6: income = 15.0 (biên) + Low Risk + Freelance -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 15.0, 750, "F"), "MANUAL REVIEW")

    def test_rule_R6_credit_score_at_medium_lower_boundary_501(self):
        """BVA + R6: credit_score = 501 (biên dưới Medium) + income >= 15 + Freelance -> MANUAL REVIEW"""
        self.assertEqual(loan_decision(30, 50.0, 501, "F"), "MANUAL REVIEW")


if __name__ == "__main__":
    unittest.main(verbosity=2)
