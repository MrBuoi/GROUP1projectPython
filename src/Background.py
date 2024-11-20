import streamlit as st
from pathlib import Path
import base64
def set_background():
    if 'background' in st.session_state and 'sidebar_background' in st.session_state:
        img = st.session_state['background']
        img1 = st.session_state['sidebar_background']
        # Thiết lập CSS cho ảnh nền
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        [data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0);
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("data:image/png;base64,{img1}");
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
def change_background():
    import os
    from pathlib import Path
    st.header("🖼️ Thay đổi ảnh nền")
    # Lấy đường dẫn của file hiện tại
    current_dir = Path(__file__).parent
    # Xây dựng đường dẫn đến thư mục assets
    assets_dir = current_dir / 'assets'
    # Kiểm tra sự tồn tại của thư mục assets
    if not assets_dir.exists():
        st.error(f"Thư mục assets không tồn tại tại đường dẫn: {assets_dir}")
        return
    # Tạo danh sách các ảnh nền chính
    backgrounds_dir = assets_dir / 'backgrounds'
    if not backgrounds_dir.exists():
        st.error(f"Thư mục backgrounds không tồn tại tại đường dẫn: {backgrounds_dir}")
        return
    background_image_files = [f for f in backgrounds_dir.iterdir() if f.suffix.lower() in ['.png', '.jpg', '.jpeg']]
    if not background_image_files:
        st.error("Không có ảnh nền chính nào trong thư mục backgrounds.")
        return
    background_images = {f.stem: f for f in background_image_files}
    # Tạo danh sách các ảnh nền của thanh bên
    sidebars_dir = assets_dir / 'sidebars'
    if not sidebars_dir.exists():
        st.error(f"Thư mục sidebars không tồn tại tại đường dẫn: {sidebars_dir}")
        return
    sidebar_image_files = [f for f in sidebars_dir.iterdir() if f.suffix.lower() in ['.png', '.jpg', '.jpeg']]
    if not sidebar_image_files:
        st.error("Không có ảnh nền nào trong thư mục sidebars.")
        return
    sidebar_images = {f.stem: f for f in sidebar_image_files}
    # Cho phép người dùng chọn ảnh nền
    selected_background = st.selectbox("Chọn hình nền chính:", list(background_images.keys()))
    selected_sidebar_background = st.selectbox("Chọn hình nền sidebar:", list(sidebar_images.keys()))
    # Lấy đường dẫn đến ảnh nền được chọn
    img_path = background_images[selected_background]
    img1_path = sidebar_images[selected_sidebar_background]
    # Chuyển đổi ảnh sang base64
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    img = get_img_as_base64(img_path)
    img1 = get_img_as_base64(img1_path)
    # Lưu lựa chọn vào session_state
    st.session_state['background'] = img
    st.session_state['sidebar_background'] = img1
    st.success("Ảnh nền đã được thay đổi thành công!")
    # Tải lại trang để cập nhật ảnh nền
    st.rerun()