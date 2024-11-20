import streamlit as st
import pandas as pd
from datetime import datetime
from src.schedule.scheduler import add_schedule, get_schedule, delete_schedule


def display_schedule(username):
    st.header("Quản lý Thời gian biểu")


    # Form thêm thời gian biểu mới
    with st.form("add_schedule_form"):
        title = st.text_input("Tiêu đề sự kiện")
        start_time = st.time_input("Giờ bắt đầu")
        end_time = st.time_input("Giờ kết thúc")
        date = st.date_input("Ngày")
        urgency = st.slider("Mức độ khẩn cấp", 0, 1000, 500, step=1, format = '')
        importance = st.slider("Mức độ quan trọng", 0, 1000, 500, step=1, format = '')
        note = st.text_area("Ghi chú")
        submit_button = st.form_submit_button(label="Thêm Thời gian biểu")


        if submit_button:
            # Thêm sự kiện vào lịch của người dùng với username
            add_schedule(username, title, start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), date.strftime("%Y-%m-%d"), urgency, importance, note)
            st.success("Đã thêm thời gian biểu!")


    # Hiển thị lịch trình
    st.subheader("Lịch trình")
    view_date = st.date_input("Chọn ngày để xem lịch trình", value=datetime.today())
    days = st.slider("Số ngày muốn xem", 1, 7, 1)
    sort_by = st.radio("Sắp xếp theo", options=["Thời gian", "Mức độ khẩn cấp", "Mức độ quan trọng"], index=0)


    # Xác định cách sắp xếp dựa trên lựa chọn của người dùng
    if sort_by == "Mức độ khẩn cấp":
        sort_by = "urgency"
    elif sort_by == "Mức độ quan trọng":
        sort_by = "importance"
    else:
        sort_by = None


    # Lấy lịch từ hàm get_schedule, truyền thêm username và cách sắp xếp
    schedules = get_schedule(username=username, date=view_date.strftime("%Y-%m-%d"), days=days, sort_by=sort_by)


    if schedules:
        # Đảm bảo rằng mỗi sự kiện đều có trường "note" và thêm "ID" cho từng sự kiện
        for i, event in enumerate(schedules):
            event["ID"] = schedules[i]["ID"]  # Gán ID cho từng sự kiện
            if "note" not in event:
                event["note"] = ""
            if "urgency" not in event:
                event["urgency"] = 0
            if "importance" not in event:
                event["importance"] = 0


        # Chuyển đổi dữ liệu thành DataFrame
        schedule_table = pd.DataFrame(schedules)


        # Chuyển mức độ khẩn cấp và quan trọng thành nhãn
        schedule_table["Mức độ khẩn cấp"] = schedule_table["urgency"].apply(lambda x: "Rất khẩn cấp" if x >= 500 else "Ít khẩn cấp")
        schedule_table["Mức độ quan trọng"] = schedule_table["importance"].apply(lambda x: "Rất quan trọng" if x >= 500 else "Ít quan trọng")


        # Loại bỏ cột mức độ khẩn cấp và quan trọng gốc
        schedule_table = schedule_table.drop(columns=["urgency", "importance"])


        # Sắp xếp lại các cột và đặt tên cột
        schedule_table = schedule_table[["ID", "title", "date", "start_time", "end_time", "Mức độ khẩn cấp", "Mức độ quan trọng", "note"]]
        schedule_table.columns = ["ID", "Tiêu đề", "Ngày", "Giờ bắt đầu", "Giờ kết thúc", "Mức độ khẩn cấp", "Mức độ quan trọng", "Ghi chú"]


        # Đặt `ID` làm chỉ mục và đặt tên cho chỉ mục là "ID"
        schedule_table.set_index("ID", inplace=True)
        schedule_table.index.name = "ID"


        # Hiển thị bảng
        st.table(schedule_table)


        # Chọn sự kiện để xóa
        delete_id = st.number_input("Nhập ID sự kiện để xóa", min_value=1, step=1)
        if st.button("Xóa Thời gian biểu"):
            # Xóa sự kiện khi nhấn nút "Xóa"
            if delete_schedule(username, delete_id):
                st.success("Đã xóa sự kiện!")
            else:
                st.error("ID không tồn tại.")
    else:
        st.write("Không có thời gian biểu nào cho ngày đã chọn.")





