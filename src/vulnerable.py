"""
Vulnerable Python module for SonarQube testing.
Contains intentional security vulnerabilities.
"""
import os
import subprocess
import pickle
import hashlib


# VULNERABILITY 1: SQL Injection
def get_user_by_id(user_id: str) -> dict:
    """Vulnerable to SQL injection - user input directly in query."""
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # BAD: Direct string concatenation with user input
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()


# VULNERABILITY 2: Command Injection
def run_system_command(user_input: str) -> str:
    """Vulnerable to command injection."""
    # BAD: User input passed directly to shell
    result = subprocess.run(f"echo {user_input}", shell=True, capture_output=True)
    return result.stdout.decode()


# VULNERABILITY 3: Hardcoded credentials
def connect_to_database() -> dict:
    """Contains hardcoded credentials."""
    # BAD: Hardcoded secrets
    db_config = {
        "host": "production-db.example.com",
        "username": "admin",
        "password": "SuperSecret123!",  # Hardcoded password
        "api_key": "sk-1234567890abcdef"  # Hardcoded API key
    }
    return db_config


# VULNERABILITY 4: Path Traversal
def read_file(filename: str) -> str:
    """Vulnerable to path traversal."""
    base_path = "/var/app/data/"
    # BAD: No validation of filename, allows ../../../etc/passwd
    file_path = os.path.join(base_path, filename)
    with open(file_path, "r") as f:
        return f.read()


# VULNERABILITY 5: Insecure Deserialization
def load_user_data(serialized_data: bytes) -> dict:
    """Vulnerable to insecure deserialization."""
    # BAD: pickle.loads on untrusted data can execute arbitrary code
    return pickle.loads(serialized_data)


# VULNERABILITY 6: Weak Cryptography
def hash_password(password: str) -> str:
    """Uses weak MD5 hashing algorithm."""
    # BAD: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()


# VULNERABILITY 7: Eval on user input
def calculate_expression(expression: str) -> float:
    """Vulnerable to code injection via eval."""
    # BAD: eval() on user input can execute arbitrary code
    return eval(expression)


# ============================================
# BUGS - These will be flagged as actual bugs
# ============================================

# BUG 1: Division by zero
def divide_numbers(a: int, b: int) -> float:
    """Contains potential division by zero."""
    divisor = 0
    return a / divisor  # BUG: Always divides by zero


# BUG 2: Unreachable code
def unreachable_code_example() -> str:
    """Contains unreachable code."""
    return "Hello"
    print("This will never execute")  # BUG: Unreachable code
    return "World"


# BUG 3: Constant condition (always true/false)
def constant_condition() -> str:
    """Contains constant condition that's always true."""
    x = 5
    if x == 5:  # BUG: Condition is always true
        return "Always"
    else:
        return "Never"  # BUG: Dead code


# BUG 4: Unused variable
def unused_variable_example() -> int:
    """Contains unused variables."""
    unused_var = "This is never used"  # BUG: Unused variable
    result = 42
    return result


# BUG 5: Identical branch conditions
def identical_branches(value: int) -> str:
    """Contains identical conditions in if/elif."""
    if value > 10:
        return "Greater"
    elif value > 10:  # BUG: Duplicate condition
        return "Also greater"
    else:
        return "Less or equal"


# BUG 6: Self-assignment
def self_assignment_bug() -> dict:
    """Contains self-assignment."""
    data = {"key": "value"}
    data = data  # BUG: Self-assignment has no effect
    return data


# BUG 7: Comparison with itself
def self_comparison(x: int) -> bool:
    """Contains comparison with itself."""
    return x == x  # BUG: Always true, comparing to itself


# BUG 8: Empty except clause
def empty_except_handler() -> None:
    """Contains empty except clause that silences errors."""
    try:
        risky_operation = 1 / 0
    except:  # BUG: Bare except catches everything including SystemExit
        pass  # BUG: Silently ignoring exception

