import streamlit as st
import time
import os
import pandas as pd
import base64
import requests
from streamlit_lottie import st_lottie
from pathlib import Path
# Hàm tải hoạt hình Lottie từ URL
def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Không thể tải hoạt hình từ URL")
        return None

# URL của hoạt hình Lottie
lottie_url1 = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
lottie_url2 = "https://assets2.lottiefiles.com/packages/lf20_x62chJ.json"

# Tải hoạt hình
lottie_json1 = load_lottieurl(lottie_url1)
lottie_json2 = load_lottieurl(lottie_url2)
def display_pomodoro():
    # Main title
    st.markdown(
                f"""
                <h1 style="text-align: center; font-size: 80px;">FOCUS ZONE</h1>
                """,
                unsafe_allow_html=True
            )
    # Timer countdown
    t1 = 1500  # 25 minutes for focus
    t2 = 300   # 5 minutes for break

    # Center the "Start" button using columns
    col1, col2, col3, cola, colb, colc, cold = st.columns([1, 1, 1, 1, 1, 1, 1])

    with cola:
        button_clicked = st.button("Start")

    if button_clicked:
        with st.empty():
            while t1:
                mins, secs = divmod(t1, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.markdown(
                    f"""
                    <h1 style="text-align: center; font-size: 200px;">{timer}</h1>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.01)  # Chạy đếm ngược với khoảng 1 giây mỗi lần
                t1 -= 1
            
            # Hiển thị hoạt hình Lottie khi hết 25 phút
            placeholder = st.empty()
            with placeholder:
                st_lottie(
                    lottie_json1,
                    height=300,
                    key="lottie_25min_complete",
                )
                st.toast("🔔 25 phút đã kết thúc! Nghỉ giải lao 5 phút nào!")
                time.sleep(2)  # Hiển thị trong 1 giây
            placeholder.empty()  # Ẩn Lottie sau 1 giây
            

        with st.empty():
            while t2:
                mins2, secs2 = divmod(t2, 60)
                timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
                st.markdown(
                    f"""
                    <h1 style="text-align: center; font-size: 200px;">{timer2}</h1>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.01)
                t2 -= 1

            # Hiển thị hoạt hình Lottie khi hết 5 phút
            placeholder = st.empty()
            with placeholder:
                st_lottie(
                    lottie_json2,
                    height=300,
                    key="lottie_5min_complete",
                )
                time.sleep(2)  # Hiển thị trong 1 giây
            placeholder.empty()  # Ẩn Lottie sau 1 giây

            st.error("⏰ 5 phút giải lao đã kết thúc!")


    # Load and play audio file
    # Lấy đường dẫn của file hiện tại
    current_dir = Path(__file__).parent
    # Xây dựng đường dẫn đến thư mục Assets
    assets_dir = current_dir.parent.parent / 'assets'
    # Xây dựng đường dẫn đến các file nhạc
    audio_file = assets_dir / 'lofi.mp3'
    if not audio_file.exists():
        st.error("File nhạc không tồn tại. Vui lòng kiểm tra lại đường dẫn!")
        return

    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False

    # Center the "Play/Pause Music" button
    col4, col5, col6, col7, col8 = st.columns([1, 1, 1, 1, 1])

    with col6:
        if st.button('Drop The Beat'):
            st.session_state.is_playing = not st.session_state.is_playing

    # Play or pause audio based on button state
    if st.session_state.is_playing:
        st.audio(str(audio_file), format="audio/mp3")
        