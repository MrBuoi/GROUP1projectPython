import streamlit as st
import os
import base64

def css_full_app():
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_css = """
    <style>
    /* Đặt màu nền cho sidebar */
    [data-testid="stSidebar"] > div:first-child {
        background-color: #0d0c0c;
    }
    /* Di chuyển toolbar nếu cần */
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    </style>
    """
    st.markdown(page_bg_css, unsafe_allow_html=True)
    
    # Cấu hình hiệu ứng CSS cho sidebar và các nút
    st.markdown("""
    <style>
    /* Tùy chỉnh sidebar và hiệu ứng hover */
    .css-1aumxhk {
        background-color: #0d0c0c;
    }
    /* Hiệu ứng hover cho các thành phần trong sidebar */
    .stSidebar .stSelectbox > div:hover,
    .stSelectbox > div:hover {
        background-color: #E8E8E8;
        color: #c41414;
        transform: scale(1.1);
        transition: transform 0.2s ease, background-color 0.2s ease;
    }
    /* Hiệu ứng hover cho nút */
    button:hover {
        background-color: #F6F5F4;
        color: white;
        transform: scale(1.15);
        transition: transform 0.5s ease, background-color 0.5s ease;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255, 102, 0, 0.5);
    }
    button:active {
        transform: scale(0.98);
        box-shadow: 0px 2px 4px rgba(255, 102, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # CSS tùy chỉnh để tạo hiệu ứng hover với animation cho sidebar
    st.markdown("""
    <style>
    /* Nền của sidebar */
    .css-1aumxhk {
        background-color: #0d0c0c;
    }   
    /* Tạo animation khi hover Sidebar */
    .stSidebar .stSelectbox > div:hover,
    .stSelectbox > div:hover {
        background-color: #E8E8E8;
        transform: scale(1.1);
        transition: transform 0.2s ease, background-color 0.2s ease;
    }
    /* Tuỳ chỉnh màu tiêu đề SelectBox */
    .stSidebar .stSelectbox label,
    .stSelectbox label {
        font-family: 'Arial', sans-serif; 
        font-size: 50px;
        color: #ffcc00;
        font-weight: bold;
    }
    /* Tùy chỉnh phông chữ và hiệu ứng của các mục chọn */
    .stSidebar .stSelectbox > div,
    .stSelectbox > div {
        background-color: #1c1c1e;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 5px;
        transition: all 0.3s ease;
    }
    /* Keyframes cho hiệu ứng glow */
    @keyframes glow {
        from {
            box-shadow: 0 0 5px #ff6600, 0 0 10px #ff6600;
        }
        to {
            box-shadow: 0 0 20px #ffcc00, 0 0 30px #ffcc00;
        }
    }
    .custom-select select {
        display: none;
    }
    .hover-3d {
        transition: transform 0.2s ease-in-out;
    }
    .hover-3d:hover {
        transform: rotateX(15deg) rotateY(15deg) scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Đổi màu toàn bộ Dropdown của các SelectBox trong ứng dụng
    st.markdown("""
    <style>
    /* Main container */
    [data-baseweb="select"] {
        background-color: #1E1E1E;
    } 
    /* Dropdown menu container */
    [data-baseweb="popover"],
    [data-baseweb="menu"] {
        background-color: #1E1E1E !important;
    }   
    /* Each option item */
    [data-baseweb="menu"] div[role="option"] {
        background-color: #1E1E1E !important;
        color: white !important;
        padding: 8px 16px !important;
        width: 100% !important;
        margin: 0 !important;
    }   
    /* Hover effect for options */
    [data-baseweb="menu"] div[role="option"]:hover,
    [data-baseweb="menu"] div[role="option"][data-highlighted="true"] {
        background-color: #BA4849 !important;
        color: white !important;
    }    
    /* Selected option */
    [role="option"][aria-selected="true"] {
        background-color: #BA4849 !important;
    }    
    /* Remove any gaps or spaces */
    [data-baseweb="menu"] > div,
    [data-baseweb="list"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Thiết lập hiệu ứng hover cho nút
    def set_button_hover_style():
        st.markdown("""
        <style>
        /* Hiệu ứng hover cho tất cả các nút trong ứng dụng */
        button:hover {
            background-color: #F6F5F4;
            color: white;
            transform: scale(1.15);
            transition: transform 0.5s ease, background-color 0.5s ease;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 102, 0, 0.5);
            animation: glow 1s ease-in-out infinite alternate;
        }
        /* Hiệu ứng khi nhấn vào nút */
        .stButton>button:active {
            transform: scale(0.98);
            box-shadow: 0px 2px 4px rgba(255, 102, 0, 0.2);
        }
        /* Hiệu ứng bounce */
        .bounce-button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #06775F;
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            transition: transform 0.2s ease-in-out;
        }
        .bounce-button:hover {
            animation: bounce 1s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        } 
        </style>
        """, unsafe_allow_html=True)
    set_button_hover_style()

    
def hesen_background():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '1.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: black;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background5():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '5.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background11():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '61.png')
    img5 = get_img_as_base64(img5_path)
    
    # CSS tùy chỉnh 
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background63():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '631.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background64():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '6411.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background65():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '651.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background66():
    @st.cache_data #Dùng để cache kết quả, giảm thời gian xử lý khi hàm được gọi nhiều lần với cùng dữ liệu.
    def get_img_as_base64(file): #Chuyển đổi một hình ảnh thành chuỗi mã hóa Base64 để có thể nhúng vào CSS.
        with open(file, "rb") as f: #Đường dẫn tới file hình ảnh. Mở file dưới dạng nhị phân (rb).
            data = f.read()
        encoded = base64.b64encode(data).decode() #Mã hóa dữ liệu hình ảnh thành Base64.
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__)) #Lấy thư mục hiện tại nơi file Python đang chạy.
    assets_dir = os.path.join(current_dir, 'assets') #Kết hợp để tạo đường dẫn tới thư mục assets.
    img5_path = os.path.join(assets_dir, '6.png') #Tạo đường dẫn đầy đủ tới file ảnh 662.png.
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def none():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, 'none.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def A():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, 'D.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def B():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, 'B.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def css_timetable():
    st.markdown(
    """
    <style>
    label {
        color: white !important;
    }
    textarea, .stTextInput, .stSlider label {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <style>
    /* Thay đổi màu chữ nhãn */
    label {
        color: white !important;
    }

    /* Đổi màu chữ cho st.radio */
    .stRadio > label {
        color: white !important;
        font-weight: bold;
    }

    /* Đổi màu cho tiêu đề và slider */
    .stSlider > label {
        color: white !important;
    }

    /* Đổi màu cho các input */
    .stTextInput > label,
    .stNumberInput > label,
    .stDateInput > label,
    .stTimeInput > label,
    .stTextArea > label {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def sidebar():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded

    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    sidebar_bg_base64_path = os.path.join(assets_dir, 'hihiii.png')
    sidebar_bg_base64  = get_img_as_base64(sidebar_bg_base64_path)
    sidebar_bg_base65_path = os.path.join(assets_dir, 'hahu.png')
    sidebar_bg_base65  = get_img_as_base64(sidebar_bg_base65_path)
    # CSS tùy chỉnh cho sidebar
    # HTML để hiển thị ảnh logo trong sidebar
    logo_html = f'''
    <div style="text-align: center; padding: 50px 0;">
        <img src="data:image/png;base64,{sidebar_bg_base64}" style="width: 100%; height: auto;">
        <img src="data:image/png;base64,{sidebar_bg_base65}" style="width: 100%; height: auto;">
    </div>
    '''
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)


