from unittest import TestCase
from secure_all import AccessManager
from secure_all import AccessManagementException

class TestAccessManager(TestCase):
    def test_request_access_code_dni_ok(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94",res)

    def test_request_access_code_dni_wrong_letter(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678B", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI letter")

    def test_request_access_code_dni_eight_characters(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("1234567Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. Less than 9 characters found")

    def test_request_access_code_dni_ten_characters(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("123456789Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. More characters than needed")

    def test_request_access_code_dni_nine_numbers(self):
        a= AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. No letter found")

    def test_request_access_code_dni_float(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678.5V", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. Float numbers inserted")

    def test_request_access_code_dni_only_string(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("ABCDEFGHI", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. Only string inserted")

    def test_request_access_code_dni_bv_eight(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("1234567Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. Less than 9 characters found")

    def test_request_access_code_dni_bv_ten(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("123456789Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI. More characters than needed")

    def test_request_access_code_dni_bv_nine(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94", res)


    def test_request_access_type_guest(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94", res)

    def test_request_access_type_resident(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "RESIDENT", "JESUS GIL", "jesusgil2001@gmail.com", 0)
        self.assertEqual("f50a07c55ad384d009f6c9ccadb1cb0f", res)

    def test_request_access_type_another(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "FOREIGN", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI access type")

    def test_request_access_type_integer(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "12345", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid DNI access type")

    def test_request_full_name_ok(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94", res)


    def test_request_full_several_name(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JOSE JESUS GIL MARTIN", "jesusgil2001@gmail.com", 2)
        self.assertEqual("f89f309b00af0ad1d4735f87b1b82ae7", res)


    def test_request_invalid_name(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "J ", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid name. Less than 3 characters")

    def test_request_name_not_blank(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUSGIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid name. Blank space not found")

    def test_request_ok_email_address(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94", res)

    def test_request_without_email_address(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid email address")

    def test_request_invalid_email_address_without_gmail(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@", 2)
        self.assertEqual(cm.exception.message, "Invalid email address")

    def test_request_invalid_email_address_without_username(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "@gmail.com", 2)
        self.assertEqual(cm.exception.message, "Invalid email address")

    def test_request_ok_validity_guest(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 3)
        self.assertEqual("f828140c35fe087170bc9bd4b1714037", res)


    def test_request_ok_validity_resident(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "RESIDENT", "JESUS GIL", "jesusgil2001@gmail.com", 0)
        self.assertEqual("f50a07c55ad384d009f6c9ccadb1cb0f", res)

    def test_request_invalid_validity_guest_one(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 1)
        self.assertEqual(cm.exception.message, "Invalid validity for GUEST")

    def test_request_invalid_validity_guest_sixteen(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 16)
        self.assertEqual(cm.exception.message, "Invalid validity for GUEST")

    def test_request_invalid_validity_resident(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "RESIDENT", "JESUS GIL", "jesusgil2001@gmail.com", -1)
        self.assertEqual(cm.exception.message, "Invalid validity for RESIDENT")

    def test_request_invalid_validity_resident_one(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "RESIDENT", "JESUS GIL", "jesusgil2001@gmail.com", 1)
        self.assertEqual(cm.exception.message, "Invalid validity for RESIDENT")

    def test_request_invalid_validity_bv_1(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 1)
        self.assertEqual(cm.exception.message, "Invalid validity for GUEST")

    def test_request_validity_ok_bv_2(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 2)
        self.assertEqual("5e2b2d3ffa89598e8c2369eded71ed94", res)

    def test_request_validity_ok_bv_3(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 3)
        self.assertEqual("f828140c35fe087170bc9bd4b1714037", res)

    def test_request_validity_ok_bv_14(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 14)
        self.assertEqual("d9128738d742d00c8571da4f08bab5ff", res)

    def test_request_validity_ok_bv_15(self):
        a = AccessManager()
        res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 15)
        self.assertEqual("4294ef23b9aa90aeab881dfb773f0298", res)

    def test_request_invalid_validity_bv_16(self):
        a = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            res = a.request_access_code("12345678Z", "GUEST", "JESUS GIL", "jesusgil2001@gmail.com", 16)
        self.assertEqual(cm.exception.message, "Invalid validity for GUEST")



