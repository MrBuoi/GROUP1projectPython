import streamlit as st

# Khởi tạo trạng thái session state
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "email" not in st.session_state:
    st.session_state["email"] = ""

def contact():
    st.subheader("📋 Form Liên hệ trực tuyến")
    
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
            else:
                st.error("Vui lòng điền đầy đủ thông tin trước khi gửi!")

    # Hiển thị thông báo nếu form đã được gửi
    if st.session_state["submitted"]:
        st.success(f"Cảm ơn {st.session_state['name']}! Tin nhắn của bạn đã được gửi. Chúng tôi sẽ liên hệ qua email: {st.session_state['email']}.")

# Gọi hàm khi trang được load
    st.markdown("## ❗️Nếu bạn có bất kỳ câu hỏi hoặc cần hỗ trợ, xin vui lòng liên hệ với chúng tôi qua Hotline : 0886619869❗️")
    # Footer
    st.markdown("---")
    st.write("© 2024 AppName - All Rights Reserved")