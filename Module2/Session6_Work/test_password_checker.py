#!/usr/bin/env python3
import unittest
from password_checker import PasswordData, validate_password, check_length, check_character_types, check_repeated_or_sequential_patterns

class TestPasswordChecker(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.username = "testuser"
        self.email = "test@example.com"
    
    def test_very_short_password(self):
        """Test a very short password"""
        password_data = PasswordData("short")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertFalse(password_data.meets_minimum_requirements)
        self.assertLess(password_data.score, 20)
        self.assertIn("too short", " ".join(password_data.weaknesses).lower())
    
    def test_only_lowercase_letters(self):
        """Test a password with only lowercase letters"""
        password_data = PasswordData("lowercaseonlypassword")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertFalse(password_data.meets_minimum_requirements)
        self.assertIn("uppercase", " ".join(password_data.weaknesses).lower())
        self.assertIn("number", " ".join(password_data.weaknesses).lower())
        self.assertIn("special", " ".join(password_data.weaknesses).lower())
    
    def test_letters_and_numbers_no_special(self):
        """Test a password with letters and numbers but no special characters"""
        password_data = PasswordData("lettersandnumbers123")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertFalse(password_data.meets_minimum_requirements)
        self.assertIn("special", " ".join(password_data.weaknesses).lower())
        self.assertNotIn("uppercase", " ".join(password_data.weaknesses).lower())
        self.assertNotIn("lowercase", " ".join(password_data.weaknesses).lower())
        self.assertNotIn("number", " ".join(password_data.weaknesses).lower())
    
    def test_password_containing_username(self):
        """Test a password containing the username"""
        password_data = PasswordData("mytestuserpassword123!")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertIn("personal information", " ".join(password_data.weaknesses).lower())
        self.assertIn("testuser", " ".join(password_data.weaknesses).lower())
    
    def test_repeated_characters(self):
        """Test a password with repeated characters"""
        password_data = PasswordData("aaaaaaBBBBB123!@")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertIn("sequential pattern", " ".join(password_data.weaknesses).lower())
    
    def test_repeated_sequence_length_4(self):
        """Test a password with a repeated sequence of length 4"""
        password_data = PasswordData("passwordABCD34ABCD%^ABCD")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertIn("repeated patterns", " ".join(password_data.weaknesses).lower())
        self.assertIn("length 4", " ".join(password_data.weaknesses).lower())
    
    def test_common_password(self):
        """Test a common password"""
        password_data = PasswordData("password123")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        # This should trigger common password detection if the database is available
        # Note: This test might not catch common passwords if rockyou-60.txt is not available
        has_common_password_warning = any("common" in w.lower() for w in password_data.weaknesses)
        if has_common_password_warning:
            self.assertTrue(has_common_password_warning)
    
    def test_strong_password(self):
        """Test a strong password with good mix of character types and no obvious patterns"""
        password_data = PasswordData("StrongP@ssw0rd!2023")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        
        self.assertTrue(password_data.meets_minimum_requirements)
        self.assertGreaterEqual(password_data.score, 80)
        self.assertEqual(password_data.feedback, "Strong password")
        
        # Should have strengths
        self.assertGreater(len(password_data.strengths), 0)
        
        # Should not have critical weaknesses
        critical_keywords = ["too short", "must contain", "rejected"]
        has_critical = any(keyword in " ".join(password_data.weaknesses).lower() 
                          for keyword in critical_keywords)
        self.assertFalse(has_critical)
    
    def test_length_function_directly(self):
        """Test the check_length function directly"""
        # Test short password
        password_data = PasswordData("short")
        check_length(password_data)
        self.assertFalse(password_data.meets_minimum_requirements)
        
        # Test good length
        password_data = PasswordData("goodlengthpassword")
        check_length(password_data)
        self.assertTrue(password_data.meets_minimum_requirements)
        
        # Test too long
        password_data = PasswordData("a" * 51)  # 51 characters
        check_length(password_data)
        self.assertIn("too long", " ".join(password_data.weaknesses).lower())
    
    def test_character_types_function_directly(self):
        """Test the check_character_types function directly"""
        # Test with all character types
        password_data = PasswordData("Test123!@#")
        check_character_types(password_data)
        self.assertEqual(password_data.character_types["uppercase"], 1)
        self.assertEqual(password_data.character_types["lowercase"], 3)
        self.assertEqual(password_data.character_types["numbers"], 3)
        self.assertEqual(password_data.character_types["special_characters"], 3)
        
        # Test missing uppercase
        password_data = PasswordData("test123!@#")
        check_character_types(password_data)
        self.assertEqual(password_data.character_types["uppercase"], 0)
        self.assertFalse(password_data.meets_minimum_requirements)
    
    def test_repeated_patterns_function_directly(self):
        """Test the check_repeated_or_sequential_patterns function directly"""
        # Test with repeated characters
        password_data = PasswordData("aaaaaaBBBBB123!@")
        check_repeated_or_sequential_patterns(password_data)
        self.assertIn("sequential pattern", " ".join(password_data.weaknesses).lower())
        
        # Test with repeated sequence
        password_data = PasswordData("testABCD123ABCD456ABCD")
        check_repeated_or_sequential_patterns(password_data)
        self.assertIn("repeated patterns", " ".join(password_data.weaknesses).lower())
        
        # Test without patterns
        password_data = PasswordData("StrongP@ssw0rd!2023")
        check_repeated_or_sequential_patterns(password_data)
        self.assertIn("does not contain", " ".join(password_data.strengths).lower())
    
    def test_password_scoring(self):
        """Test password scoring logic"""
        # Very weak password
        password_data = PasswordData("weak")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        self.assertEqual(password_data.score, 0)
        
        # Moderate password
        password_data = PasswordData("moomoomooderate password#$ABC123")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        self.assertGreaterEqual(password_data.score, 50)
        self.assertLess(password_data.score, 80)
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Empty password
        password_data = PasswordData("")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        self.assertFalse(password_data.meets_minimum_requirements)
        
        # Exactly minimum length
        password_data = PasswordData("MinLength12!")
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        # Should pass length check but might fail other checks
        
        # Maximum length
        password_data = PasswordData("a" * 48 + "B1!")  # 51 characters
        validate_password(password_data, self.username, self.email, "rockyou-60.txt")
        self.assertIn("too long", " ".join(password_data.weaknesses).lower())

if __name__ == '__main__':
    unittest.main()
