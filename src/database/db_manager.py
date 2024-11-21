import json
import os


# Đường dẫn đầy đủ tới file users.json trong thư mục database
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), 'users.json')


def load_users():
    """
    Load danh sách người dùng từ file JSON.
    """
    if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) > 0:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_user(username, hashed_password):
    """
    Lưu thông tin người dùng mới vào file JSON.
    """
    users = load_users()
    username = username.strip()


    if username in users:
        return "Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác."


    # Lưu thông tin người dùng với mật khẩu đã hash
    users[username] = {
        'password': hashed_password
    }
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)
    return "Đăng ký thành công!"



