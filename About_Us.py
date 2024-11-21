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
    # Đường dẫn tới thư mục assets và file ảnh
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, "assets")

    # File ảnh
    img_path1 = os.path.join(assets_dir, "Tuan.png")
    img_path2 = os.path.join(assets_dir, "Tung.png")
    img_path3 = os.path.join(assets_dir, "Bao.png")
    img_path4 = os.path.join(assets_dir, "Anh.png")
    img_path5 = os.path.join(assets_dir, "Giang.png")
    img_path6 = os.path.join(assets_dir, "Huong.png")
    img_path7 = os.path.join(assets_dir, "Hieu.png")
    img_path8 = os.path.join(assets_dir, "ThayLong.png")
    # Chuyển ảnh thành Base64
    Tuan = get_img_as_base64(img_path1)
    Tung = get_img_as_base64(img_path2)
    Bao = get_img_as_base64(img_path3)
    Anh = get_img_as_base64(img_path4)
    Giang = get_img_as_base64(img_path5)
    Huong = get_img_as_base64(img_path6)
    Hieu = get_img_as_base64(img_path7)
    ThayLong = get_img_as_base64(img_path8)

    # Hiển thị tiêu đề
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>Meet Our Astronaut</h1>",
        unsafe_allow_html=True
    )

    # Hàng 1
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(f"data:image/png;base64,{Tuan}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>TRẦN ANH TUẤN</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    with col2:
        st.image(f"data:image/png;base64,{Bao}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>DOÃN QUỐC BẢO</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    with col3:
        st.image(f"data:image/png;base64,{Tung}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>VŨ BÙI ĐÌNH TÙNG</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")

    # Hàng 2
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.image(f"data:image/png;base64,{Anh}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>PHẠM ĐỨC ANH</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    with col5:
        st.image(f"data:image/png;base64,{Giang}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>NGUYỄN THỊ HƯƠNG GIANG</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    with col6:
        st.image(f"data:image/png;base64,{Huong}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>LÊ LAN HƯƠNG</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    with col7:
        st.image(f"data:image/png;base64,{Hieu}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>TRỊNH MINH HIẾU</h1>",
            unsafe_allow_html=True
        )
        st.markdown(" Học để biết, biết để làm, làm để sống, và sống để cống hiến")
        st.write("Email : doanquocbao030805@gmail.com")
    # Hiển thị tiêu đề
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>Our Instructor</h1>",
        unsafe_allow_html=True
    )
    col10, col11, col12 = st.columns(3)
    with col10:
        st.markdown("#### \n Nhóm xin chân thành cảm ơn sự hướng dẫn và giảng dạy của TS. Nguyễn Tuấn Long với các kiến thức về lập trình căn bản với ngôn ngữ Python. Những chỉ dạy của thầy là nền tảng quan trọng và là kim chỉ nam cho cả nhóm hoàn thành sản phẩm với kết quả như trên")
    with col12:
        pass
    with col11:
        st.image(f"data:image/png;base64,{ThayLong}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>NGUYỄN TUẤN LONG</h1>",
            unsafe_allow_html=True
        )
        st.write("Giảng Viên Khoa Toán Kinh Tế")
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>About Us</h1>",
        unsafe_allow_html=True
    )
    st.markdown("## Từ 7 thành viên được thầy Long chia team một cách ngẫu nhiên, mỗi thành viên với những tính cách khác nhau, những kinh nghiệm khác nhau đã cùng nhau nỗ lực hoàn thành một sản phẩm chỉn chu nhất, với mong muốn lớn nhất là cải thiện khả năng lập trình, tiến tới bài thi kết thúc học phần; đồng thời vận dụng những kiến thức trong chương trình học vào các dự án thực tế, nhằm làm quen với công việc tương lai. Kết quả đạt được của sản phẩm là kết tinh của sự tâm huyết, của những đêm không ngủ, những buổi họp thật dài và những niềm tin về một kết quả xứng đáng.")