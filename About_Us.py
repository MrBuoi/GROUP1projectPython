import os
import streamlit as st
import base64

# Hàm chuyển đổi ảnh thành Base64
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None  # Nếu không tìm thấy file, trả về None

def render_about_us():
    # Đường dẫn tới thư mục assets và file test.png
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, "assets")
    img_path1 = os.path.join(assets_dir, "Tuan.png")
    img_path2 = os.path.join(assets_dir, "Bao.png")
    img_path3 = os.path.join(assets_dir, "Tung.png")

    # Chuyển ảnh thành Base64
    Tuan = get_img_as_base64(img_path1)
    Tung = get_img_as_base64(img_path2)
    Bao = get_img_as_base64(img_path3)
    
    # Hiển thị thông tin
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>Meet Our Astronaut</h1>",
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(f"data:image/png;base64,{Tuan}", use_container_width=True)
        st.markdown("**Donna Stroupe**")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    with col2:
        st.image(f"data:image/png;base64,{Bao}", use_container_width=True)
        st.markdown("**Cia Rodriguez**")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    with col3:
        st.image(f"data:image/png;base64,{Tung}", use_container_width=True)
        st.markdown("**Adora Montminy**")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
