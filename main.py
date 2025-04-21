import random
import string
import pyperclip
from datetime import datetime

def generate_password():
    username = input("Enter website or app name: ").strip()
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    all_chars = letters + digits + special
    
    password = ''.join(random.choice(all_chars) for _ in range(16))
    
    pyperclip.copy(password)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("password_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - Description: {username}, Password: {password}\n")

generate_password()
