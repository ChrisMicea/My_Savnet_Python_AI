import unittest
from improved_IBAN_validator import validate_IBAN, load_country_codes, check_valid_iban_len, check_country_code_exists, check_iban_mod_97_algorithm

class TestIBANValidator(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures with country codes."""
        self.country_codes = load_country_codes("country_codes.json")
    
    # Test valid IBANs
    def test_valid_iban_netherlands(self):
        """Test valid Netherlands IBAN."""
        iban = "NL91ABNA0417164300"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_germany(self):
        """Test valid Germany IBAN."""
        iban = "DE89370400440532013000"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_uk(self):
        """Test valid United Kingdom IBAN."""
        iban = "GB82WEST12345698765432"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_france(self):
        """Test valid France IBAN."""
        iban = "FR1420041010050500013M02606"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_spain(self):
        """Test valid Spain IBAN."""
        iban = "ES9121000418450200051332"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_poland(self):
        """Test valid Poland IBAN."""
        iban = "PL61109010140000071219812874"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_valid_iban_italy(self):
        """Test valid Italy IBAN."""
        iban = "IT60X0542811101000000123456"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    # Test invalid IBANs - Too short
    def test_invalid_iban_too_short_netherlands(self):
        """Test Netherlands IBAN that's too short."""
        iban = "NL91ABNA04171643"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_iban_too_short_germany(self):
        """Test Germany IBAN that's too short."""
        iban = "DE893704004405320130"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_iban_too_short_uk(self):
        """Test UK IBAN that's too short."""
        iban = "GB82WEST123456987654"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    # Test invalid IBANs - Invalid country code
    def test_invalid_country_code_xx(self):
        """Test IBAN with invalid country code XX."""
        iban = "XX991234567890123456"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_country_code_zz(self):
        """Test IBAN with invalid country code ZZ."""
        iban = "ZZ991234567890123456"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    # Test invalid IBANs - Invalid check digits
    def test_invalid_check_digits_netherlands(self):
        """Test Netherlands IBAN with invalid check digits."""
        iban = "NL91ABNA0417164301"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_check_digits_germany(self):
        """Test Germany IBAN with invalid check digits."""
        iban = "DE89370400440532013100"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_check_digits_uk(self):
        """Test UK IBAN with invalid check digits."""
        iban = "GB82WEST12345698765433"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    # Test edge cases
    def test_invalid_check_digits_00_netherlands(self):
        """Test Netherlands IBAN with 00 check digits."""
        iban = "NL00ABNA0417164300"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_check_digits_99_germany(self):
        """Test Germany IBAN with 99 check digits."""
        iban = "DE99370400440532013000"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_characters_in_bank_code(self):
        """Test IBAN with invalid character in bank code."""
        iban = "GB82W3ST12345698765432"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_characters_in_account(self):
        """Test IBAN with invalid character in account number."""
        iban = "FR1420041010050500013M0Z606"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_characters_special_chars(self):
        """Test IBAN with special characters."""
        iban = "NL91ABNA041716430A"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_characters_at_symbol(self):
        """Test IBAN with @ symbol."""
        iban = "DE893704004405320130@0"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_invalid_characters_hash(self):
        """Test IBAN with # symbol."""
        iban = "GB82WEST123456987654#2"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    # Test individual functions
    def test_check_valid_iban_len_valid(self):
        """Test length validation with valid IBAN."""
        iban = "NL91ABNA0417164300"
        self.assertTrue(check_valid_iban_len(iban, self.country_codes))
    
    def test_check_valid_iban_len_invalid(self):
        """Test length validation with invalid IBAN length."""
        iban = "NL91ABNA04171643"
        self.assertFalse(check_valid_iban_len(iban, self.country_codes))
    
    def test_check_country_code_exists_valid(self):
        """Test country code validation with valid country."""
        iban = "NL91ABNA0417164300"
        self.assertTrue(check_country_code_exists(iban, self.country_codes))
    
    def test_check_country_code_exists_invalid(self):
        """Test country code validation with invalid country."""
        iban = "XX91ABNA0417164300"
        self.assertFalse(check_country_code_exists(iban, self.country_codes))
    
    def test_check_iban_mod_97_algorithm_valid(self):
        """Test mod-97 algorithm with valid IBAN."""
        iban = "NL91ABNA0417164300"
        self.assertTrue(check_iban_mod_97_algorithm(iban))
    
    def test_check_iban_mod_97_algorithm_invalid(self):
        """Test mod-97 algorithm with invalid IBAN."""
        iban = "NL91ABNA0417164301"
        self.assertFalse(check_iban_mod_97_algorithm(iban))
    
    # Test with spaces (should be handled by validation)
    def test_iban_with_spaces_valid(self):
        """Test valid IBAN with spaces."""
        iban = "NL91 ABNA 0417 1643 00"
        self.assertTrue(validate_IBAN(iban, self.country_codes))
    
    def test_iban_with_spaces_invalid(self):
        """Test invalid IBAN with spaces."""
        iban = "NL91 ABNA 0417 1643 01"
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    # Test edge cases
    def test_empty_iban(self):
        """Test empty IBAN."""
        iban = ""
        self.assertFalse(validate_IBAN(iban, self.country_codes))
    
    def test_only_spaces(self):
        """Test IBAN with only spaces."""
        iban = "   "
        self.assertFalse(validate_IBAN(iban, self.country_codes))

if __name__ == '__main__':
    unittest.main()
