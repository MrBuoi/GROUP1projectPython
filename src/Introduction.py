import streamlit as st
from PIL import Image 
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
def introduction():
    # Đường dẫn tới thư mục assets và file ảnh
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, "../assets")
    img_path9 = os.path.join(assets_dir, "VuTru.png")
    VuTru = get_img_as_base64(img_path9)
    
    
    #a, b, c = st.columns([2,22,2])
    #with b:
        #image2 = Image.open(r"assets/Title.png")
        #st.image(image2,use_container_width=True)
        #pass
    a, b = st.columns(2)
    with a:
        st.markdown(
        "<h1 style='text-align:; font-size: 80px;'>TIMELY </h1>",
        unsafe_allow_html=True
    )
        st.markdown("### Cỗ máy thời gian của những nhà khai phá vũ trụ")
        st.write("""

    Hãy tưởng tượng bạn là một phi hành gia, đang bước vào vùng không gian bao la – nơi mà từng giây phút đều quý giá như ngọc ngà, và mỗi quyết định đều có thể thay đổi quỹ đạo của cả hành trình. TIMELY chính là cỗ máy thời gian đồng hành, giúp bạn định hướng giữa các vì sao, vạch lối trên hành trình khám phá không giới hạn.

    Vũ trụ của bạn có thể là công việc, là những giấc mơ ấp ủ, hay những mục tiêu đầy thách thức. TIMELY sẽ trở thành bản đồ sao – nơi từng khoảnh khắc đều được tính toán để tối ưu hóa. Với TIMELY, bạn không chỉ quản lý thời gian, mà còn biến nó thành nhiên liệu, đẩy bạn bay xa hơn qua những khoảng không vô tận của khả năng.

    Trên hành trình ấy, bạn sẽ không còn cảm thấy lạc lối. TIMELY không chỉ giúp bạn bước qua những chặng đường đơn độc mà còn giúp bạn cảm nhận sâu sắc giá trị của từng phút giây. Đó không chỉ là việc "sống" qua ngày, mà là cách bạn "khai phá" từng giây phút – để mỗi ngày trở thành một cuộc phiêu lưu đáng nhớ.

    Hãy bước vào khoang tàu của TIMELY, nơi thời gian không còn là giới hạn, mà trở thành đôi cánh đưa bạn chạm đến những giấc mơ xa xôi nhất.

    **TIMELY – Khi bạn là phi hành gia của chính cuộc đời mình, hãy để thời gian làm bệ phóng cho những hành trình vĩ đại.**
    """)
    st.markdown("---")
    
    with b:
        st.image(f"data:image/png;base64,{VuTru}")
        
    cola, colb, colc = st.columns(3)
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px;'>Các tính năng của TIMELY </h1>",
        unsafe_allow_html=True
    )
    with cola:
        pass 
    st.write("")
    st.write("")
    st.write("")
    cold,colk = st.columns(2)
    with colk:
        st.write("")
        left, mid ,right = st.columns(3)
        with mid:
            st.markdown("<h4 style='color: yellow;'> FOCUS ZONE</h3>", unsafe_allow_html=True)
            st.write("")
            st.write("")
        st.markdown("""
                            ##### Sử dụng đồng hồ Pomodoro để tập trung tối đa trong khoảng thời gian làm việc ngắn. Kết hợp với nhạc nền Lofi để tăng hiệu quả làm việc. Hiển thị đồng hồ đếm ngược và nhắc nhở nghỉ ngơi đúng lúc.
                        """)
    with cold:
        image1 = Image.open(r"assets/Focus Zone.png")
        st.image(image1,caption="""Tập trung tối đa: Phương pháp Pomodoro kết hợp với nhạc thư giãn.
""",use_container_width= True)
    col4,col3 = st.columns(2)
    with col4:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        l,m,r = st.columns([1,3,1])
        with m:
            st.write("")
            st.write("")
            st.markdown("<h4 style='color: yellow;'> LỊCH TRÌNH THÔNG MINH</h3>", unsafe_allow_html=True)
            st.write("")
            st.write("")
        st.markdown("""
            ##### Thêm lịch trình cá nhân hoặc công việc chỉ với vài bước đơn giản. Sắp xếp nhiệm vụ theo mức độ quan trọng và khẩn cấp. Xem các lịch trình sắp tới dưới dạng bảng trực quan.

            """)
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Lịch  trình thời gian.png')
        st.image(image,caption= """Dễ dàng lập kế hoạch: Tạo lịch trình nhanh chóng và rõ ràng.
""",use_container_width= True)
    col2,col1 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        l,m,r = st.columns([1,3,1])
        with m:
            st.markdown("<h4 style='color: yellow;'> BẢNG LỊCH TRÌNH</h3>", unsafe_allow_html=True)
            st.write("")
        st.markdown("""
            ##### Xây dựng hệ thống công việc với từng mức độ công việc cụ thể. Tuỳ chọn sắp xếp theo các tiêu chí
             """)
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Lịch trình.png')
        st.image(image,caption= """Lịch trình rành mạch ,dễ nhìn : Tạo động lực hoàn thành việc làm.
""",use_container_width= True)
    col1,col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        l,m,r = st.columns([1,3,1])
        with m:
            st.markdown("<h4 style='color: yellow;'> MA TRẬN EISENHOWER</h3>", unsafe_allow_html=True)
            st.write("")
        st.markdown("""
            ##### Giúp bạn phân loại công việc dựa trên ma trận "Quan trọng - Khẩn cấp", dễ dàng xác định thứ tự ưu tiên cho từng nhiệm vụ.
             """)
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/n_eisen.PNG')
        st.image(image,caption= """Ưu tiên hợp lý: Dựa vào mức độ quan trọng và khẩn cấp để ra quyết định.
""",use_container_width= True)
    col2,col1 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        l,m,r = st.columns([1,3,1])
        with m:
            st.markdown("<h4 style='color: yellow;'> THỐNG KÊ THỜI GIAN TẬP TRUNG HỌC</h3>", unsafe_allow_html=True)
            st.write("")
        st.markdown("""
            ##### Đây là công cụ để kiểm tra xem năng suất học tập trung của người dùng là bao nhiêu, từ đó người dùng có thể nắm bắt được tình trạng học của bản thân.
             """)
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Thống kê thời gian.png')
        st.image(image,caption= """Số liệu rõ ràng: Thống kê tình trạng học tập trung học.
""",use_container_width= True)
    st.markdown("---")
    q,w,e = st.columns([1,10,1])
    with w:
        st.write("")
        st.markdown(
        "<h1 style='text-align: center; font-size: 40px;'>THỜI GIAN QUÝ GIÁ - HÃY ĐỂ TIMELY GIÚP BẠN TẬN DỤNG ĐIỀU ĐÓ</h1>",
        unsafe_allow_html=True
    )
    a, b, c = st.columns(3)
    with b:
        image3 = Image.open(r"assets/Ảnh cuối.PNG")
        st.image(image3)
        
 