import bcrypt


# Hash mật khẩu
def bcrypt_hash_password(password: str) -> str:
    """
    Hash mật khẩu bằng bcrypt.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


# Xác thực mật khẩu
def bcrypt_verify_password(password: str, hashed_password: str) -> bool:
    """
    Kiểm tra mật khẩu so với hash đã lưu.
    """
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)



