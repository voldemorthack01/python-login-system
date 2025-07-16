# Python Login System

This is a simple terminal-based login system built in Python.  
It allows users to create an account, log in securely, and manage their credentials (change username/password or delete the account).

## 🔒 Features
- User registration with input validation
- Secure password input using `getpass` (hidden typing)
- Minimum password length enforcement
- Change username and password
- Delete account with confirmation
- Stores account data in a text file (`accounts.txt`)

## 📂 File Structure
login.py         # Main script with all functionality  
accounts.txt     # Data file (created automatically)  
README.md        # Project documentation  
.gitignore       # Ignore Python cache files  
requirements.txt # Dependencies (none in this case)  

## 🧪 How to Run
1. Make sure Python 3 is installed.
2. Clone the repository:
  git clone https://github.com/voldemorthack01/python-login-system.git
  cd python-login-system
3. Run the script:
   python login.py
> The script will auto-generate `accounts.txt` to store user data locally.

## 🚨 Disclaimer
This is a learning project and **not secure for real-world use**.  
Passwords are stored in plain text. To improve it, you can add password hashing using libraries like `bcrypt`.

## 📄 License
This project is licensed under the [MIT License](LICENSE).
