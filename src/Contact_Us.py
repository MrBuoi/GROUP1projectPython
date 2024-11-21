import streamlit as st
import json
from pathlib import Path

# Đường dẫn tới file lưu phản hồi
feedback_file_path = Path("src/database/feed_back.json")

# Hàm lưu phản hồi vào file JSON
def save_feedback(email, feedback):
    # Kiểm tra và tạo file nếu chưa tồn tại
    if not feedback_file_path.exists():
        feedback_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(feedback_file_path, "w") as file:
            json.dump({}, file, indent=4)
    
    # Đọc dữ liệu hiện tại từ file
    with open(feedback_file_path, "r") as file:
        data = json.load(file)
    
    # Thêm phản hồi mới
    data[email] = feedback
    
    # Ghi lại dữ liệu vào file
    with open(feedback_file_path, "w") as file:
        json.dump(data, file, indent=4)

# Khởi tạo trạng thái session state
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "email" not in st.session_state:
    st.session_state["email"] = ""

def contact():
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>📋 Form Liên hệ trực tuyến</h1>",
        unsafe_allow_html=True
    )
    
    with st.form("contact_form"):
        name = st.text_input("Họ và Tên", placeholder="Nhập tên của bạn")
        email = st.text_input("Email", placeholder="Nhập email của bạn")
        message = st.text_area("Tin nhắn", placeholder="Nhập tin nhắn hoặc câu hỏi của bạn")
        submitted = st.form_submit_button("Gửi")
        
        # Xử lý gửi form
        if submitted:
            if name and email and message:
                st.session_state["submitted"] = True
                st.session_state["name"] = name
                st.session_state["email"] = email

                # Lưu phản hồi vào file JSON
                save_feedback(email, message)

                st.success(f"Cảm ơn {st.session_state['name']}! Tin nhắn của bạn đã được gửi. Chúng tôi sẽ liên hệ qua email: {st.session_state['email']}.")
            else:
                st.error("Vui lòng điền đầy đủ thông tin trước khi gửi!")


    st.markdown("## ❗️Nếu bạn có bất kỳ câu hỏi hoặc cần hỗ trợ, xin vui lòng liên hệ với chúng tôi qua Hotline : 0886619869❗️")
    # Footer
    st.markdown("---")
    st.write("© 2024 AppName - All Rights Reserved")