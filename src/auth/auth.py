import streamlit as st
from src.database.db_manager import load_users, save_user
from src.auth.encryption import bcrypt_hash_password, bcrypt_verify_password
import re


def login():
    """
    Xử lý chức năng đăng nhập.
    """
    st.subheader("Đăng Nhập")
    with st.form(key='login_form'):
        username = st.text_input("Tên đăng nhập", key="login_username").strip()
        password = st.text_input("Mật khẩu", type="password", key="login_password")
        submit_button = st.form_submit_button(label='Đăng Nhập')


    if submit_button:
        users = load_users()
        if username in users:
            stored_hashed_password = users[username]['password']


            # Xác thực mật khẩu
            if bcrypt_verify_password(password, stored_hashed_password):
                st.success("Đăng nhập thành công!")
                st.session_state['username'] = username  # Lưu tên người dùng vào session
                return True
            else:
                st.error("Sai mật khẩu.")
                return False
        else:
            st.error("Người dùng không tồn tại.")
            return False


def register():
    """
    Xử lý chức năng đăng ký.
    """
    st.subheader("Đăng Ký")
    with st.form(key='register_form'):
        username = st.text_input("Tên đăng nhập", key="register_username").strip()
        password = st.text_input("Mật khẩu", type="password", key="register_password")
        confirm_password = st.text_input("Xác nhận mật khẩu", type="password", key="confirm_password")
        submit_button = st.form_submit_button(label='Đăng Ký')


    if submit_button:
        # Kiểm tra mật khẩu
        if password != confirm_password:
            st.error("Mật khẩu xác nhận không khớp.")
            return
        if len(password) < 8:
            st.error("Mật khẩu phải chứa ít nhất 8 ký tự.")
            return
        if not re.search(r'[a-z]', password):
            st.error("Mật khẩu phải chứa ít nhất 1 chữ cái in thường")
        if not re.search(r'[0-9]', password):
            st.error("Mật khẩu phải chứa ít nhất 1 chữ số")
        if not re.search(r'[A-Z]', password):
            st.error("Mật khẩu phải chứa ít nhất 1 chữ cái in hoa")
        
        if not re.search(r'[^a-zA-Z0-9]', password):
            st.error("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt.")
            return


        # Kiểm tra tên người dùng
        users = load_users()
        if username in users:
            st.error("Tên người dùng đã tồn tại. Vui lòng chọn tên khác.")
            return


        # Hash mật khẩu và lưu thông tin
        hashed_password = bcrypt_hash_password(password)
        message = save_user(username, hashed_password)
        if "thành công" in message:
            st.snow()
            st.balloons()
        st.success(message)

