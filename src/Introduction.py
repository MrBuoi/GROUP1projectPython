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
    st.markdown("---")
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
            """
            <style>
            .custom-font {
                color: white;
                font-size: 80px;
                font-family: 'Montserrat';
            }
            </style>
            <h6 class='custom-font'>
                TIMELY
            </h6>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
        "<h1 style='color: white; font-size: 30px; font-weight: bold;'> CỖ MÁY THỜI GIAN CỦA CÁC NHÀ THÁM HIỂM VŨ TRỤ</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h6 style='color: white; font-size: 18px; font-style: italic;'>Hãy tưởng tượng bạn là một phi hành gia, bước vào vùng không gian bao la – nơi mỗi giây phút đều quý giá như ngọc ngà, và mọi quyết định đều có thể thay đổi quỹ đạo của cả hành trình. TIMELY chính là người bạn đồng hành, một cỗ máy thời gian giúp bạn định hướng giữa các vì sao, vạch lối trên hành trình khám phá vô tận. </h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h6 style='color: white; font-size: 18px; font-style: italic;'>Vũ trụ không chỉ là khoảng không xa xăm, mà còn là những giấc mơ ấp ủ, những thử thách vĩ đại. TIMELY giúp bạn biến từng khoảnh khắc thành những mảnh ghép hoàn hảo trong câu chuyện cuộc đời mình – một cuộc đời được tối ưu hóa, đầy đam mê và mục tiêu rõ ràng. </h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h6 style='color: white; font-size: 18px; font-style: italic;'>Trên hành trình chinh phục này, sẽ không thiếu những ngã rẽ hay thử thách. Nhưng TIMELY là người dẫn đường, giúp bạn tiến lên một cách mạnh mẽ và trọn vẹn nhất. Sống, đối với TIMELY, không chỉ là tồn tại, mà là cách bạn khai phá từng giây phút – để mỗi ngày trở thành một cuộc phiêu lưu đáng nhớ. </h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h6 style='color: white; font-size: 18px; font-style: italic; '>Hãy đặt chân lên khoang tàu cùng TIMELY, nơi thời gian không còn là giới hạn. Hãy để TIMELY biến mỗi bước đi thành cánh cửa mở ra những chân trời mới – những hành tinh của ước mơ, khát vọng, và khám phá bất tận.</h1>",
        unsafe_allow_html=True
    )
        st.markdown(
        "<h6 style='color: white; font-size: 22px; font-style: italic;'>TIMELY – Vì hành trình của bạn không chỉ là thời gian, mà là cuộc phiêu lưu vĩ đại!!!</h1>",
        unsafe_allow_html=True
    )
        
    st.markdown("---")
    
    with b:
        st.image(f"data:image/png;base64,{VuTru}")
        
    cola, colb, colc = st.columns(3)
    st.markdown(
            """
            <style>
            .custom-font {
                color: white;
                font-size: 70px;
                text-align: center;
                font-family: 'Montserrat';
            }
            </style>
            <h6 class='custom-font'>
                CÁC TÍNH NĂNG CỦA TIMELY
            </h6>
            """,
            unsafe_allow_html=True
        )
    with cola:
        pass 
    st.write("")
    cold,colk = st.columns(2)
    with colk:
        st.write("")
        left, mid ,right = st.columns(3)
        with mid:
            st.markdown("<h4 style='color: yellow;'> FOCUS ZONE</h3>", unsafe_allow_html=True)
            st.write("")
        st.markdown(
        "<h1 style='color: white; text-align: center;font-style: italic; font-size: 20px;'> Sử dụng đồng hồ Pomodoro để tập trung tối đa trong khoảng thời gian làm việc ngắn. Kết hợp với nhạc nền Lofi để tăng hiệu quả làm việc. Hiển thị đồng hồ đếm ngược và nhắc nhở nghỉ ngơi đúng lúc </h1>",
        unsafe_allow_html=True
    )
    with cold:
        image1 = Image.open(r"assets/Focus Zone.png")
        st.image(image1,caption="""Tập trung tối đa: Phương pháp Pomodoro kết hợp với nhạc thư giãn.
""")
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
        st.markdown(
        "<h1 style='color: white;font-style: italic; text-align: center; font-size: 20px;'> Thêm lịch trình cá nhân hoặc công việc chỉ với vài bước đơn giản. Sắp xếp nhiệm vụ theo mức độ quan trọng và khẩn cấp. Xem các lịch trình sắp tới dưới dạng bảng trực quan </h1>",
        unsafe_allow_html=True
    )
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Lịch  trình thời gian.png')
        st.image(image,caption= """Dễ dàng lập kế hoạch: Tạo lịch trình nhanh chóng và rõ ràng.
""")
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
        st.markdown(
        "<h1 style='color: white; text-align: center;font-style: italic; font-size: 20px;'> Xây dựng hệ thống công việc với từng mức độ công việc cụ thể. Tuỳ chọn sắp xếp theo các tiêu chí </h1>",
        unsafe_allow_html=True
    )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Lịch trình.png')
        st.image(image,caption= """Lịch trình rành mạch ,dễ nhìn : Tạo động lực hoàn thành việc làm.
""")
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
        st.markdown(
        "<h1 style='color: white; text-align: center;font-style: italic; font-size: 20px;'> Giúp bạn phân loại công việc dựa trên ma trận Quan trọng - Khẩn cấp, dễ dàng xác định thứ tự ưu tiên cho từng nhiệm vụ </h1>",
        unsafe_allow_html=True
    )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/n_eisen.PNG')
        st.image(image,caption= """Ưu tiên hợp lý: Dựa vào mức độ quan trọng và khẩn cấp để ra quyết định.
""")
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
        st.markdown(
        "<h1 style='color: white; text-align: center;font-style: italic; font-size: 20px;'> Đây là công cụ để kiểm tra xem năng suất học tập trung của người dùng là bao nhiêu, từ đó người dùng có thể nắm bắt được tình trạng học của bản thân </h1>",
        unsafe_allow_html=True
    )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        image = Image.open(r'assets/Thống kê thời gian.png')
        st.image(image,caption= """Số liệu rõ ràng: Thống kê tình trạng học tập trung học.
""")
    st.markdown("---")
    q,w,e = st.columns([1,10,1])
    with w:
        st.write("")
        st.markdown(
        "<h1 style='color: white; text-align: center; font-size: 40px;'> THỜI GIAN QUÝ GIÁ - HÃY ĐỂ TIMELY GIÚP BẠN TẬN DỤNG ĐIỀU ĐÓ!!!</h1>",
        unsafe_allow_html=True
    )
    a, b, c = st.columns(3)
    with b:
        image3 = Image.open(r"assets/Ảnh cuối.png")
        st.image(image3)
    st.markdown(
        "<h1 style='color: white; font-size: 10px;'> © 2024 TIMELY - All Rights Reserved </h1>",
        unsafe_allow_html=True
    )
 