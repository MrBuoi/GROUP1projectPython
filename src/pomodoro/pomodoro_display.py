import streamlit as st
import time
import os
import requests
from pathlib import Path
from streamlit_lottie import st_lottie
from style import pmdr_background
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
lottie_url2 = "https://lottie.host/fcc5c4c9-c08c-460e-b991-5ab983ca4ad1/wwJITddgjD.json"

# Tải hoạt hình
lottie_json1 = load_lottieurl(lottie_url1)
lottie_json2 = load_lottieurl(lottie_url2)

def display_pomodoro():
    # Main title
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>FOCUS ZONE</h1>",
        unsafe_allow_html=True
    )

    # Timer countdown
    t1 = 1500  # 25 minutes for focus
    t2 = 300   # 5 minutes for break

    # Start Button
    col1, col2, col3, cola, colb, colc, cold = st.columns([1, 1, 1, 1, 1, 1, 1])
    with cola:
        button_clicked = st.button("Start")

    # Countdown logic
    if button_clicked:
        with st.empty():
            while t1:
                mins, secs = divmod(t1, 60)
                st.markdown(
                    f"<h1 style='text-align: center; font-size: 200px;'>{mins:02d}:{secs:02d}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.01)
                t1 -= 1

            placeholder = st.empty()
            with placeholder:
                st_lottie(
                    lottie_json1,
                    height=300,
                    key="lottie_25min_complete",
                )
                st.toast("🔔Chúc mừng bạn đã hoàn thành 25 phút Hãy ghỉ giải lao 5 phút nhé!")
                time.sleep(4)  # Hiển thị trong 1 giây
            placeholder.empty()  # Ẩn Lottie sau 1 giây

        with st.empty():
            st.toast("Break Time!!!")
            while t2:
                mins, secs = divmod(t2, 60)
                st.markdown(
                    f"<h1 style='text-align: center; font-size: 200px;'>{mins:02d}:{secs:02d}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.01)
                t2 -= 1

            # Hiển thị hoạt hình Lottie khi hết 5 phút
            #placeholder = st.empty()
            #with placeholder:
                #st_lottie(
                    #lottie_json2,
                    #height=300,
                    #key="lottie_5min_complete",
                #)
                #time.sleep(2)  # Hiển thị trong 1 giây
            #placeholder.empty()  # Ẩn Lottie sau 1 giây

            st.error("⏰ 5 phút giải lao đã kết thúc!")

    # Music Section
    st.markdown("### 🎵 Select Your Rythm")

    # Lấy đường dẫn hiện tại
    current_dir = Path(__file__).parent
    assets_dir = current_dir / '../../assets'
    assets_dir = assets_dir.resolve()  # Chuyển thành đường dẫn tuyệt đối

    # File nhạc
    music_files = {
        "Lofi Beats": assets_dir / 'lofi.mp3',
        "Classical Music": assets_dir / 'classic.mp3',
        "Healing Music": assets_dir / 'healing.mp3',
        "Piano Music": assets_dir / 'piano.mp3',
        "Electronic Music": assets_dir / 'edm.mp3'
    }

    # Dropdown để chọn nhạc
    selected_music = st.selectbox("Select a music track:", list(music_files.keys()))
    audio_file_path = music_files[selected_music]

    # Kiểm tra file nhạc
    if not audio_file_path.exists():
        st.error(f"Tệp âm thanh không tồn tại: {audio_file_path}")
    else:
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

    
