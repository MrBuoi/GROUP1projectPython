import streamlit as st
import webbrowser

from style import background63
from style import background64
from style import background65
from style import background66

# Hàm để hiển thị nội dung "Hướng dẫn sử dụng"
def instruction_of_use():
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(
        "<h1 style='color: white; font-size: 40px;'> ⭐️Hướng Dẫn Sử Dụng Ứng Dụng Quản Lý Thời Gian và Lịch Trình</h1>",
        unsafe_allow_html=True
    )
    quanly = st.selectbox("",['Đăng nhập và Đăng ký', 'Bảng lịch trình thời gian biểu', 'Đồng hồ Pomodoro','Sử dụng ma trận Eisenhower','Thống kê thời gian tập trung học'])
    if quanly == 'Đăng nhập và Đăng ký':
        background63()
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 30px;'>Hãy chọn Đăng Nhập nếu bạn đã có tài khoản trên ứng dụng hoặc chọn Đăng Ký nếu bạn chưa có tài khoản</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
    elif quanly == 'Bảng lịch trình thời gian biểu':
        background64()
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Sau khi đăng nhập thành công, bạn sẽ được chuyển đến trang chính của ứng dụng và có thể tạo bảng lịch trình thời gian biểu. Bạn có thể thêm hoặc xóa các công việc ,sự kiện bạn muốn</h1>",
        unsafe_allow_html=True
    )
        st.subheader("Thêm Công việc:")
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Để thêm một công việc mới, hãy nhấn vào nút Thêm Công việc trên giao diện của ứng dụng. Sau đó, hãy nhập tên công việc, thời gian bắt đầu và thời gian kết thúc của công việc , ngày thực hiện và ghi chú của công việc. Sau đó, hãy nhấn vào nút Thêm Thời gian biểu để lưu công việc mới vào bảng lịch trình</h1>",
        unsafe_allow_html=True
    )
        st.subheader("""Xóa Công việc:""")
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Để xóa một công việc, hãy chọn ID công việc mà bạn muốn xóa. ID là các số nằm ở cột đầu tiên của bảng lịch trình, chọn số ID tương ứng với công việc mà bạn đã điền và muốn xóa nó ngay sau đó. Sau khi chọn ID, chọn Xóa Thời gian biểu</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
    elif quanly == 'Đồng hồ Pomodoro':
        background65()
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Người dùng có thể tùy chọn kích hoạt phương pháp học tập Pomodoro. Khi bắt đầu, nhấn nút Start để kích hoạt đồng hồ đếm ngược cho phiên làm việc kéo dài từ 25-30 phút. Sau khi kết thúc một phiên làm việc, hệ thống sẽ tự động thông báo và bắt đầu thời gian nghỉ giải lao ngắn kéo dài 5 phút</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Chu kỳ này sẽ lặp lại cho đến khi hoàn thành công việc. Sau 4 lần nghỉ giải lao ngắn, người dùng sẽ được nhắc nghỉ dài hơn, kéo dài từ 10-15 phút</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Ngoài ra, ứng dụng tích hợp đồng hồ hiển thị thời gian, cung cấp một số câu truyền động lực, và đặc biệt có tùy chọn phát nhạc không lời giúp tạo không gian làm việc tập trung. Người dùng có thể bật hoặc tắt nhạc tùy thích trong quá trình sử dụng</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
    elif quanly == 'Sử dụng ma trận Eisenhower':
        background66()
        def eisenhower():
            webbrowser.open_new_tab("https://gobranding.com.vn/ma-tran-eisenhower-la-gi/")
        st.button("Click it!",on_click= eisenhower)
        st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
    elif quanly == 'Thống kê thời gian tập trung học':
        background63()
        st.markdown(
        "<h1 style='color: white;font-style: italic; font-size: 20px;'>Sau mỗi Pomodoro thì số phút bạn đã học được sẽ cộng vào với nhau, sau đó kết quả cuối cùng là số phút mà bạn đã học được trong ngày hôm ấy. Người dùng cũng có thể so sánh số phút học tập trung trong ngày so với ngày trước đã học</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
