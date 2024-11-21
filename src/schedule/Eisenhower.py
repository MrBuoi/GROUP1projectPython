import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# Đường dẫn tuyệt đối đến file schedule.json
BASE_DIR = os.path.dirname(os.path.abspath("src/database/schedule.json"))
SCHEDULE_FILE = os.path.join(BASE_DIR, "schedule.json")
# Tải lịch từ file hoặc tạo mới nếu chưa tồn tại
def load_schedule(filename=SCHEDULE_FILE):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            return json.loads(data) if data else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
# Hàm để hiển thị ma trận Eisenhower
# Updated Function
def display_eisenhower_matrix(username):
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>MA TRẬN EISENHOWER</h1>",
        unsafe_allow_html=True
    )
    # Tải dữ liệu lịch trình
    schedule = load_schedule()
    if username not in schedule:
        st.write("Không có lịch trình cho người dùng này.")
        return 
    user_schedule = schedule[username]
    # Chuyển đổi dữ liệu thành DataFrame
    data = []
    for event_id, event in user_schedule.items():
        if "urgency" in event and "importance" in event:
            data.append({
                "ID": event_id,
                "title": event["title"],
                "urgency": event["urgency"],
                "importance": event["importance"],
            })
    if not data:
        st.write("Không có sự kiện nào với mức độ khẩn cấp và quan trọng.")
        return
    df = pd.DataFrame(data)
    # Tạo biểu đồ scatter
    plt.figure(figsize=(7, 3))
    # Tạo một danh sách để lưu thông tin cho legend
    legend_labels = []
    # Vẽ scatter plot
    for idx, row in df.iterrows():
        plt.scatter(
            row['urgency'],
            row['importance'],
            s=100,
            label=f"{row['ID']}: {row['title']}",
            cmap='viridis',
        )
    # Vẽ đường x=5 và y=5
    plt.axvline(x=500, color='red', linestyle='--')
    plt.axhline(y=500, color='red', linestyle='--')
    # Thêm title và labels
    plt.xlabel('Mức độ khẩn cấp')
    plt.ylabel('Mức độ quan trọng')
    plt.grid(False)
    plt.gca().set_xticks([])  # Tắt số trên trục x
    plt.gca().set_yticks([])  # Tắt số trên trục y
    # Đặt giới hạn trục x và y từ 0 đến 10
    plt.xlim(-50, 1050)
    plt.ylim(-50, 1050)
    # Thêm legend box
    plt.legend(title="Sự kiện", bbox_to_anchor=(0, -0.1), loc='upper left')
    # Hiển thị biểu đồ
    st.pyplot(plt)







