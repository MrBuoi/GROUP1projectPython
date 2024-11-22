import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path
import json
from datetime import datetime, timedelta
# Đường dẫn tới file JSON
database_path = Path("src/database/study_time.json")
def save_study_data(data):
    database_path.parent.mkdir(parents=True, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
    with open(database_path, "w") as file:
        json.dump(data, file, indent=4)
# Hàm tải dữ liệu từ file JSON
def load_study_data():
    if database_path.exists():
        try:
            with open(database_path, "r") as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            # Xử lý nếu file bị hỏng hoặc không hợp lệ
            save_study_data({})  # Khởi tạo lại dữ liệu rỗng
            return {}
    else:
        return {}
def filter_data_by_date_range(data, days=None):
    """
    Lọc dữ liệu theo khoảng thời gian và tự động điền ngày không có dữ liệu bằng 0.
    :param data: Dữ liệu study_time từ file JSON
    :param days: Số ngày để lọc dữ liệu. Nếu None, trả về toàn bộ dữ liệu.
    """
    if not data:
        return {}
    # Xác định min_date và max_date từ dữ liệu
    min_date = min(datetime.strptime(date, "%Y-%m-%d") for date in data.keys())
    max_date = max(datetime.strptime(date, "%Y-%m-%d") for date in data.keys())
    # Nếu days được cung cấp, điều chỉnh min_date
    if days:
        cutoff_date = datetime.now() - timedelta(days=days)
        min_date = max(min_date, cutoff_date)
    # Tạo danh sách ngày đầy đủ từ min_date đến max_date
    all_dates = [
        (min_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((max_date - min_date).days + 1)
    ]
    # Điền dữ liệu cho các ngày không có
    filtered_data = {date: data.get(date, 0) for date in all_dates}
    return filtered_data
def report_display():
    # Tải dữ liệu từ file JSON
    data = load_study_data()
    user = st.session_state['username'] 
    # Lấy dữ liệu của người dùng
    study_data = data.get(user, {})
    if study_data:
        # Tùy chọn khoảng thời gian
        st.markdown(
        "<h1 style='color: #003366; text-align: center; font-size: 80px;'>Lựa chọn khoảng thời gian</h1>",
        unsafe_allow_html=True
    )
        option = st.radio("Khoảng thời gian:", ["7 ngày", "1 tháng", "Tất cả"])
        if option == "7 ngày":
            filtered_data = filter_data_by_date_range(study_data, days=7)
        elif option == "1 tháng":
            filtered_data = filter_data_by_date_range(study_data, days=30)
        else:  # "Tất cả"
            filtered_data = filter_data_by_date_range(study_data)  # Không giới hạn days
        if filtered_data:
            # Sắp xếp dữ liệu theo ngày
            sorted_data = dict(sorted(filtered_data.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d")))
            dates = list(sorted_data.keys())
            durations = list(sorted_data.values())
            # Vẽ biểu đồ bằng matplotlib
            fig, ax = plt.subplots(figsize=(7, 3))
            ax.bar(dates, durations, color='skyblue')
            ax.set_xlabel('Ngày')
            ax.set_ylabel('Thời gian học (phút)')
            ax.set_title('Thời gian học theo phương pháp Pomodoro mỗi ngày')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.warning("Không có dữ liệu trong khoảng thời gian được chọn.")
    else:
        st.warning("Chưa có dữ liệu học để vẽ biểu đồ!")





