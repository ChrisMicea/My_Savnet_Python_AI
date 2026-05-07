#!/usr/bin/env python3
import sys
import getpass
from password_checker import PasswordData, validate_password

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}")
    print("PASSWORD STRENGTH CHECKER")
    print(f"{'='*60}{Colors.END}")

def print_colored(text, color):
    print(f"{color}{text}{Colors.END}")

def get_user_input():
    print(f"\n{Colors.BOLD}Please enter your information:{Colors.END}")
    username = input(f"{Colors.BLUE}Username: {Colors.END}")
    email = input(f"{Colors.BLUE}Email: {Colors.END}")
    
    while True:
        try:
            password = getpass.getpass(f"{Colors.BLUE}Password: {Colors.END}")
            if password:
                break
            print_colored("Password cannot be empty!", Colors.RED)
        except (KeyboardInterrupt, EOFError):
            print_colored("\nOperation cancelled.", Colors.YELLOW)
            sys.exit(0)
    
    return username, email, password

def display_results(password_data):
    print(f"\n{Colors.BOLD}{'='*60}")
    print("PASSWORD ANALYSIS RESULTS")
    print(f"{'='*60}{Colors.END}")
    
    # Score and overall status
    if password_data.meets_minimum_requirements:
        print_colored(f"✓ Status: ACCEPTED", Colors.GREEN)
    else:
        print_colored(f"✗ Status: REJECTED", Colors.RED)
    
    print(f"Score: {password_data.score}/100")
    print(f"Feedback: {password_data.feedback}")
    
    # Critical issues (red) - use existing weaknesses from password_checker
    critical_issues = []
    for weakness in password_data.weaknesses:
        if any(keyword in weakness.lower() for keyword in ["too short", "must contain", "rejected"]):
            critical_issues.append(weakness)
    
    if password_data.score < 20 and not critical_issues: # Too many small weaknesses, no critical ones
        critical_issues.append("Too many weaknesses - password rejected")
    
    if critical_issues:
        print(f"\n{Colors.BOLD}{Colors.RED}CRITICAL ISSUES:{Colors.END}")
        for issue in critical_issues:
            print_colored(f"  ✗ {issue}", Colors.RED)
    
    # Warnings (yellow) - use existing weaknesses from password_checker
    warnings = [w for w in password_data.weaknesses 
                if not any(keyword in w.lower() for keyword in ["too short", "must contain", "rejected"])]
    
    if warnings:
        print(f"\n{Colors.BOLD}{Colors.YELLOW}WARNINGS:{Colors.END}")
        for warning in warnings:
            print_colored(f"  ⚠ {warning}", Colors.YELLOW)
    
    # Strengths (green) - use existing strengths from password_checker
    if password_data.strengths:
        print(f"\n{Colors.BOLD}{Colors.GREEN}STRENGTHS:{Colors.END}")
        for strength in password_data.strengths:
            print_colored(f"  ✓ {strength}", Colors.GREEN)
    
    # Character breakdown - use existing character_types from password_checker
    print(f"\n{Colors.BOLD}CHARACTER BREAKDOWN:{Colors.END}")
    for char_type, count in password_data.character_types.items():
        print(f"  {char_type.replace('_', ' ').title()}: {count}")

def main():
    print_header()
    
    while True:
        try:
            username, email, password = get_user_input()
            
            password_data = PasswordData(password)
            validate_password(password_data, username, email, "rockyou-60.txt")
            
            display_results(password_data)
            
            # Ask if user wants to check another password
            choice = input(f"\n{Colors.BLUE}Check another password? (y/n): {Colors.END}").lower()
            if choice not in ['y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print_colored("\nGoodbye!", Colors.BLUE)
            break
        except Exception as e:
            print_colored(f"An error occurred: {e}", Colors.RED)

if __name__ == "__main__":
    main()
