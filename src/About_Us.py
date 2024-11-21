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
    assets_dir = os.path.join(current_dir, "../assets")

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
    st.markdown("---")
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>⚡️About Us⚡️</h1>",
        unsafe_allow_html=True
    )
    st.markdown("####   Từ 7 thành viên được thầy Long chia team một cách ngẫu nhiên, mỗi thành viên với những tính cách khác nhau, những kinh nghiệm khác nhau đã cùng nhau nỗ lực hoàn thành một sản phẩm chỉn chu nhất, với mong muốn lớn nhất là cải thiện khả năng lập trình, tiến tới bài thi kết thúc học phần; đồng thời vận dụng những kiến thức trong chương trình học vào các dự án thực tế, nhằm làm quen với công việc tương lai. Kết quả đạt được của sản phẩm là kết tinh của sự tâm huyết, của những đêm không ngủ, những buổi họp thật dài và những niềm tin về một kết quả xứng đáng!!!")
    st.markdown("---")
    # Hiển thị tiêu đề
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>✨ Meet Our Astronaut ✨</h1>",
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
        st.markdown("Đừng sợ khác biệt, hãy là chính mình!")
        st.write("Email : trantuan1701ltv@gmail.com")
    with col2:
        st.image(f"data:image/png;base64,{Bao}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>DOÃN QUỐC BẢO</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Hãy thất bại lớn trong những năm tháng này, để thành công lớn trong tương lai!")
        st.write("Email : doanquocbao030805@gmail.com")
    with col3:
        st.image(f"data:image/png;base64,{Tung}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>VŨ BÙI ĐÌNH TÙNG</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Những gì bạn học hôm nay sẽ quyết định bạn là ai ngày mai!")
        st.write("Email : vubuidinhtung@gmail.com")

    # Hàng 2
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.image(f"data:image/png;base64,{Anh}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>PHẠM ĐỨC ANH</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Thời gian là vốn quý, hãy đầu tư cho tương lai!")
        st.write("Email : andypham85@gmail.com")
    with col5:
        st.image(f"data:image/png;base64,{Giang}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>NGUYỄN HƯƠNG GIANG</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Thay vì chờ cơ hội đến, hãy tự tạo ra nó!")
        st.write("Email : nguyenthihuonggiang2005@gmail.com")
    with col6:
        st.image(f"data:image/png;base64,{Huong}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>LÊ LAN HƯƠNG</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Thời sinh viên không phải là đường đua, mà là hành trình khám phá!")
        st.write("Email : lelanhuong22092005@gmail.com")
    with col7:
        st.image(f"data:image/png;base64,{Hieu}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>TRỊNH MINH HIẾU</h1>",
            unsafe_allow_html=True
        )
        st.markdown("Thành công là khi bạn hài lòng với sự tiến bộ của chính mình!")
        st.write("Email : trinhhieu231205@gmail.com")
    st.markdown("---")
    # Hiển thị tiêu đề
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>✨Our Instructor✨</h1>",
        unsafe_allow_html=True
    )
    col11, col12 = st.columns(2)
    with col12:
        st.markdown("### Nhóm xin được gửi lời cảm ơn chân thành nhất đối với sự hướng dẫn và giảng dạy của TS. Nguyễn Tuấn Long về các kiến thức về lập trình căn bản với ngôn ngữ Python. ")
        st.markdown("### Những chỉ dạy của thầy sẽ mãi mãi là nền tảng quan trọng và là kim chỉ nam cho cả nhóm hoàn thành sản phẩm với kết quả như trên!!!❤️❤️❤️")
    with col11:
        st.image(f"data:image/png;base64,{ThayLong}", use_container_width=True)
        st.markdown(
            "<h1 style='text-align: center; font-size: 20px;'>TS. NGUYỄN TUẤN LONG</h1>",
            unsafe_allow_html=True
        )
    st.markdown("---")