"""
Configuration file with secrets for testing Talisman detection.
WARNING: These are INTENTIONAL test secrets for CI/CD testing.
"""

# AWS Credentials - Using AKIA prefix pattern that Talisman detects
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"
AWS_SECRET_KEY = "abcdefghijklmnopqrstuvwxyz1234567890ABCD"

# High entropy string that should trigger detection
HIGH_ENTROPY_SECRET = "Rz4Kp9Wq2XmL8YvB3NcT6UfA1DgH7JsE0IwO5PxC"

# Private key format that Talisman detects
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdz
-----END OPENSSH PRIVATE KEY-----"""

# RSA Private key format
RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MxszR7TESTKEYx
-----END RSA PRIVATE KEY-----"""

# Password variables
password = "VerySecretPassword123!"
secret_key = "mysupersecretekey_abcdef1634567891"

# Auth token with bearer pattern
auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
