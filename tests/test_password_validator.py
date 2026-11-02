import unittest
from src.password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):

    # Проходящие тесты
    def test_valid_latin_password(self):
        self.assertTrue(validate_password("SecurePass1!"))

    def test_valid_cyrillic_password(self):
        self.assertTrue(validate_password("ПарольТест9#"))

    # Граничные значения длины
    def test_length_7(self):
        #длина меньше 8
        self.assertFalse(validate_password("Abc123!"))

    def test_boundary_length_8(self):
        self.assertTrue(validate_password("Abcde12!"))

    def test_boundary_length_20(self):
        self.assertTrue(validate_password("Abcdefghij12345678!X"))

    def test_length_21(self):
        self.assertFalse(validate_password("Abcdefghij123456789!X"))

    #Классы эквивалентности
    def test_missing_uppercase(self):
        self.assertFalse(validate_password("securepass1!"))

    def test_missing_lowercase(self):
        self.assertFalse(validate_password("SECUREPASS1!"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("SecurePassword!"))

    def test_missing_special(self):
        self.assertFalse(validate_password("SecurePassword1"))

    def test_special_not_in_list_underscore(self):
        self.assertFalse(validate_password("SecurePass1_"))

    def test_special_not_in_list_question(self):
        self.assertFalse(validate_password("SecurePass1?"))

    # Исключения:(пробелы)
    def test_space_inside(self):
        with self.assertRaises(ValueError):
            validate_password("Pass 1234!")

    def test_space_at_start(self):
        with self.assertRaises(ValueError):
            validate_password(" Pass1234!")

    def test_space_at_end(self):
        with self.assertRaises(ValueError):
            validate_password("Pass1234! ")

    #Исключения:(типы)
    def test_type_none(self):
        with self.assertRaises(TypeError):
            validate_password(None)

    def test_type_int(self):
        with self.assertRaises(TypeError):
            validate_password(12345678)

    def test_type_list(self):
        with self.assertRaises(TypeError):
            validate_password(["P", "a", "s", "s", "1", "!"])


if __name__ == "__main__":
    unittest.main()