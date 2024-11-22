import streamlit as st

from src.auth.auth import login, register
from src.schedule.schedule_display import display_schedule
from src.pomodoro.pomodoro_display import display_pomodoro
from src.Introduction import introduction
from src.Instruction_of_use import instruction_of_use
from src.schedule.Eisenhower import display_eisenhower_matrix  # Import hàm Eisenhower
from src.About_Us import render_about_us
from src.pomodoro.pomodoro_report import report_display
from src.Contact_Us import contact

from style import css_full_app
from style import hesen_background
from style import background5
from style import background11
from style import none
from style import A
from style import B
from style import sidebar

# Thiết lập cấu hình trang (gọi một lần)
st.set_page_config(
    page_title="Quản Lý Thời Gian và Lịch Trình",
    page_icon="🕒",
    layout="wide",
)
def main():
    css_full_app() #Ảnh side bar và hiệu ứng hover
    # Kiểm tra trạng thái đăng nhập trong session
    if 'is_logged_in' not in st.session_state: #to store and manage login state:
        st.session_state['is_logged_in'] = False  #Tracks whether the user is logged in.
        st.session_state['username'] = '' #Stores the logged-in user's name.
    # Menu lựa chọn giữa Đăng nhập và Đăng Ký
    menu = ["Sign In", "Sign Up", "Contact"]
    option = st.sidebar.selectbox("User Account", menu)
    if not st.session_state['is_logged_in']:
        background11()
        if option == "Sign In":
            if login():
                st.session_state['is_logged_in'] = True
        elif option == "Sign Up":
            register()
        elif option == "Contact":
            none() #ảnh background
            contact()
        sidebar()
    else:
        # Hiển thị menu chính khi đã đăng nhập
        st.sidebar.success(f"Welcome: {st.session_state['username']}!")
        # Tạo menu chính
        main_menu = st.sidebar.selectbox(
            "Menu",
            ["Introduction", "Instructions", "Tools", "About Us","Contact Us"]
        )
        if main_menu == "Introduction":
            none()
            introduction()
        elif main_menu == "Instructions":
            instruction_of_use()
        elif main_menu == "Tools":
            # Menu công cụ học tập
            sub_menu = st.sidebar.selectbox(
                "Tools",
                ["Pomodoro Method","Study Report", "Timetable Management", "Eisenhower Matrix"]
            )
            if sub_menu == "Pomodoro Method":
                B()
                display_pomodoro()
            elif sub_menu == "Study Report":
                A()
                report_display()
            elif sub_menu == "Timetable Management":
                background5()
                display_schedule(st.session_state['username'])
            elif sub_menu == "Eisenhower Matrix":
                hesen_background()
                display_eisenhower_matrix(st.session_state['username'])
        elif main_menu == "About Us":
            none()
            render_about_us()
        elif main_menu == "Contact Us":
            none()
            contact()
        sidebar()
        if st.sidebar.button("Log Out"):
            st.session_state['is_logged_in'] = False
            st.session_state['username'] = ''
            st.toast('Log Out Successfully')
            st.rerun()
if __name__ == "__main__":
    main()



