import json
import os
import streamlit as st
from src.auth.encryption import rsa_encrypt
# Đường dẫn đầy đủ tới file users.json trong thư mục database
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

def load_users():
    # Kiểm tra nếu tệp tồn tại và không rỗng
    if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) > 0:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    # Nếu tệp không tồn tại hoặc rỗng, trả về dictionary trống
    return {}

def save_user(username, password, public_key, private_key):
    users = load_users()
    username = username.strip()

    if username in users:
        return "Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác."

    # Mã hóa và lưu thông tin người dùng
    encrypted_password = rsa_encrypt(password, public_key)
    users[username] = {
        'password': encrypted_password,
        'public_key': public_key,
        'private_key': private_key
    }
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)
    return "Đăng ký thành công!"