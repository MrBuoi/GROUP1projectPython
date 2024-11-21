import streamlit as st
import time
import requests
from pathlib import Path
from streamlit_lottie import st_lottie
import datetime
import json


def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Không thể tải hoạt hình từ URL")
        return None


lottie_url1 = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
lottie_url2 = "https://lottie.host/fcc5c4c9-c08c-460e-b991-5ab983ca4ad1/wwJITddgjD.json"


# Tải hoạt hình
lottie_json1 = load_lottieurl(lottie_url1)
lottie_json2 = load_lottieurl(lottie_url2)


# Đường dẫn tới file JSON
database_path = Path("src/database/study_time.json")


# Hàm tải dữ liệu từ file JSON
def load_study_data():
    if database_path.exists():
        with open(database_path, "r") as file:
            return json.load(file)
    return {}


# Hàm lưu dữ liệu vào file JSON
def save_study_data(data):
    with open(database_path, "w") as file:
        json.dump(data, file, indent=4)


# Hàm ghi nhận thời gian học
def record_study_time(user, time_spent):
    data = load_study_data()
    today = datetime.date.today().strftime("%Y-%m-%d")
    if user not in data:
        data[user] = {}
    if today in data[user]:
        data[user][today] += time_spent
    else:
        data[user][today] = time_spent
    save_study_data(data)
    return data[user][today]




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
                time.sleep(1)
                t1 -= 1
            st.success("🔔 25 phút đã kết thúc! Nghỉ giải lao chút nào!")


            # Ghi nhận thời gian học vào file JSON
            user = st.session_state['username']
            total_today = record_study_time(user, 25)
            st.write(f"Thời gian học hôm nay: {total_today} phút")


            placeholder = st.empty()
            with placeholder:
                st_lottie(
                    lottie_json1,
                    height=300,
                    key="lottie_25min_complete",
                )
                st.toast("🔔Chúc mừng bạn đã hoàn thành 25 phút! Hãy nghỉ giải lao 5 phút nhé!")
                time.sleep(4)
            placeholder.empty()


        with st.empty():
            st.toast("Break Time!!!")
            while t2:
                mins, secs = divmod(t2, 60)
                st.markdown(
                    f"<h1 style='text-align: center; font-size: 200px;'>{mins:02d}:{secs:02d}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(1)
                t2 -= 1


            placeholder = st.empty()
            with placeholder:
                st_lottie(
                    lottie_json2,
                    height=300,
                    key="lottie_5min_complete",
                )
                time.sleep(2)
            placeholder.empty()
            st.error("⏰ 5 phút giải lao đã kết thúc!")


    # Music Section
    st.markdown("##  Select Your Rhythm")


    # Lấy đường dẫn hiện tại
    current_dir = Path(__file__).parent
    assets_dir = current_dir / '../../assets'
    assets_dir = assets_dir.resolve()   # Chuyển thành đường dẫn tuyệt đối


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