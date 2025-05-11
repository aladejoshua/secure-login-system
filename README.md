To-Do List
1. Plan the Project

 - List features: registration, login, 2FA, password hashing, session security.
 * Learn basics of secure passwords (bcrypt) and 2FA (pyotp).

2. Build User Registration

 * Set up SQLite database with a users table (username, hashed password, email, 2FA secret).
 * Create a registration form with Flask.
 * Hash passwords with bcrypt before saving.
 * Check for strong passwords (8+ characters, mixed case).

3. Create Login System

 * Build a login form with Flask.
 * Verify passwords using bcrypt.
 * Set up secure sessions with Flask (use HttpOnly cookies).

4. Add Two-Factor Authentication (2FA)

 * Use pyotp for TOTP-based 2FA.
 * Generate a QR code for users to scan with an authenticator app.
 * Verify 2FA codes during login.

5. Add Encryption

 * Encrypt 2FA secrets in the database using cryptography (Fernet).
 * Ensure no sensitive data is stored in plaintext.

6. Improve Security

 * Limit login attempts to prevent brute force (e.g., lock after 5 failed tries).
 * Add CSRF protection to forms using Flask-WTF.
 * Log failed logins to a file.

7. Test the System

 * Write tests with pytest for registration, login, and 2FA.
 * Test with wrong passwords and invalid 2FA codes.
 * Check for vulnerabilities using bandit -r ..

8. Document and Finish

 * Add comments to your code.
 * Update this README with how to run the project.
 * Write a short report on what you learned.