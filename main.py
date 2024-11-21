import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import hashlib
import os
from pathlib import Path
import base64
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components
from src.auth.auth import login, register
from src.schedule.schedule_display import display_schedule
from src.pomodoro.pomodoro_display import display_pomodoro
from src.Introduction import introduction
from src.Instruction_of_use import instruction_of_use
from src.schedule.Eisenhower import display_eisenhower_matrix  # Import hàm Eisenhower
from style import css_full_app
from style import hesen_background
from style import pmdr_background
from style import background3
from style import background4
from style import background5
from style import background11
from style import background7
from style import background62
from style import background63
from style import background64
from style import background65
from style import background66
# Thiết lập cấu hình trang (gọi một lần)
st.set_page_config(
    page_title="Quản Lý Thời Gian và Lịch Trình",
    page_icon="🕒",
    layout="wide",
)
def main():
    css_full_app()
    # Kiểm tra trạng thái đăng nhập trong session
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False
        st.session_state['username'] = ''
    # Menu lựa chọn giữa Đăng nhập và Đăng Ký
    menu = ["Đăng Nhập", "Đăng Ký"]
    option = st.sidebar.selectbox("User Account", menu)
    if not st.session_state['is_logged_in']:
        background11()
        if option == "Đăng Nhập":
            if login():
                st.session_state.is_logged_in = True
        elif option == "Đăng Ký":
            register()
    else:
        # Hiển thị menu chính khi đã đăng nhập
        st.sidebar.success(f"Đã đăng nhập: {st.session_state['username']}")
        # Tạo menu chính
        main_menu = st.sidebar.selectbox(
            "Menu",
            ["Giới Thiệu Ứng Dụng", "Hướng dẫn sử dụng", "Công Cụ Học Tập"]
        )
        if main_menu == "Giới Thiệu Ứng Dụng":
            background62()
            introduction()
        elif main_menu == "Hướng dẫn sử dụng":
            instruction_of_use()
        elif main_menu == "Công Cụ Học Tập":
            # Menu công cụ học tập
            sub_menu = st.sidebar.selectbox(
                "Các Công Cụ Chính",
                ["Phương Pháp Pomodoro", "Quản lý Thời gian biểu", "Ma trận Eisenhower"]
            )
            if sub_menu == "Phương Pháp Pomodoro":
                pmdr_background()
                display_pomodoro()
            elif sub_menu == "Quản lý Thời gian biểu":
                background5()
                display_schedule(st.session_state['username'])
            elif sub_menu == "Ma trận Eisenhower":
                hesen_background()
                display_eisenhower_matrix(st.session_state['username'])
        if st.sidebar.button("Đăng xuất"):
            st.session_state['is_logged_in'] = False
            st.session_state['username'] = ''
            st.toast('Đăng xuất thành công')
            st.rerun()
if __name__ == "__main__":
    main()



