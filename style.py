import streamlit as st
import os
import base64

def css_full_app():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img_path = os.path.join(assets_dir, 'Background.png')
    img = get_img_as_base64(img_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
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
    # Cấu hình hiệu ứng CSS cho sidebar và các nút
    st.markdown("""
    <style>
    /* Tùy chỉnh sidebar và hiệu ứng hover */
    .css-1aumxhk {{
        background-color: #0d0c0c;
    }}
    .stSidebar .stSelectbox > div:hover {{
        background-color: #E8E8E8;
        color: #c41414;
        transform: scale(1.1);
        transition: transform 0.2s ease, background-color 0.2s ease;
    }}
    .stSelectbox > div:hover {{
        background-color: #E8E8E8;
        transform: scale(1.1);
        transition: transform 0.2s ease, background-color 0.2s ease;
    }}
    button:hover {{
        background-color: #F6F5F4;
        color: white;
        transform: scale(1.15);
        transition: transform 0.5s ease, background-color 0.5s ease;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255, 102, 0, 0.5);
    }}
    button:active {{
        transform: scale(0.98);
        box-shadow: 0px 2px 4px rgba(255, 102, 0, 0.2);
    }}
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
    .stSidebar .stSelectbox > div:hover {
        background-color: #E8E8E8;
        color: #c41414;
        transform: scale(1.1); /* Phóng to nhẹ */
        transition: transform 0.2s ease, background-color 0.05s ease; /* Animation khi hover */
    }
    .stSelectbox > div:hover {
        background-color: #E8E8E8;
        transform: scale(1.1); /* Phóng to nhẹ */
        transition: transform 0.2s ease, background-color 0.2s ease; /* Animation khi hover */
    }
    /* Tạo hiệu ứng chuyển động nhấp nháy */
    .stSidebar .stSelectbox > div:hover {
        animation: glow s ease-in-out infinite alternate; /* Hiệu ứng chuyển động nhấp nháy */
    }
    .stSelectbox > div:hover {
        animation: glow 1s ease-in-out infinite alternate; /* Hiệu ứng chuyển động nhấp nháy */
    }
    /* Tuỳ chỉnh màu tiêu đề SlectBox */
    .stSidebar .stSelectbox label {
        font-family: 'Arial', sans-serif; 
        font-size: 100px;
        color: #ffcc00; /* Màu chữ của tiêu đề */
        font-weight: bold;
        margin-bottom: 0px;    /* Khoảng cách dưới */
        display: inline-block;
    }
    .stSelectbox label {
        font-family: 'Arial', sans-serif; 
        font-size: 50px;
        color: #ffcc00; /* Màu chữ của tiêu đề */
        font-weight: bold;
    }
    
    /* Tùy chỉnh phông chữ và hiệu ứng của các mục chọn */
    .stSidebar .stSelectbox > div {
        background-color: #1c1c1e; /* Màu nền của selectbox */
        color: white; /* Màu chữ của selectbox */
        font-size: 16px;
        border-radius: 10px;
        padding: 5px;
        transition: all 0.3s ease; /* Thời gian chuyển đổi chung */
    }
    .stSelectbox > div {
        background-color: #1c1c1e; /* Màu nền của selectbox */
        color: white; /* Màu chữ của selectbox */
        font-size: 16px;
        border-radius: 10px;
        padding: 5px;
        transition: all 0.3s ease; /* Thời gian chuyển đổi chung */
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
        display: none; /* Ẩn phần tử select gốc */
    }
    .hover-3d {
    transition: transform 0.2s ease-in-out;
    }
    .hover-3d:hover {
    transform: rotateX(15deg) rotateY(15deg) scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)
    # Đổi màu toàn bộ Dropdown của Các SelectBox trong ứng dụng
    st.markdown("""
        <style>
    /* Main container */
    [data-baseweb="select"] {
        background-color: #1E1E1E;
    } 
    /* Dropdown menu container */
    [data-baseweb="popover"] {
        background-color: #1E1E1E !important;
    }   
    /* Menu container */
    [data-baseweb="menu"] {
        background-color: #1E1E1E !important;
        padding: 0 !important;  /* Remove padding */
    }   
    /* Each option item */
    [data-baseweb="menu"] div[role="option"] {
        background-color: #1E1E1E !important;
        color: white !important;
        padding: 8px 16px !important;  /* Add padding to option itself */
        width: 100% !important;  /* Full width */
        margin: 0 !important;  /* Remove margin */
    }   
    /* Hover effect for options */
    [data-baseweb="menu"] div[role="option"]:hover {
        background-color: #BA4849 !important;
        color: white !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 8px 16px !important;
    }    
    /* Selected option */
    [role="option"][aria-selected="true"] {
        background-color: #BA4849 !important;
        width: 100% !important;
    }    
    /* Override any default hover styles */
    [data-baseweb="menu"] div[role="option"][data-highlighted="true"] {
        background-color: #BA4849 !important;
        width: 100% !important;
    }   
    /* Remove any gaps or spaces */
    [data-baseweb="menu"] > div {
        padding: 0 !important;
        margin: 0 !important;
    }    
    /* Ensure the list takes full width */
    [data-baseweb="list"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)
    def set_button_hover_style():
        st.markdown("""
        <style>
        /* Hiệu ứng hover cho tất cả các nút trong ứng dụng */
        button:hover {
            background-color: #F6F5F4; /* Màu nền khi hover */
            color: white; /* Màu chữ khi hover */
            transform: scale(1.15); /* Phóng to nhẹ */
            transition: transform 0.5s ease, background-color 0.5s ease; /* Animation khi hover */
            border-radius: 10px; /* Bo góc cho nút */
            box-shadow: 0 0 10px rgba(255, 102, 0, 0.5); /* Hiệu ứng bóng */
            animation: glow 1s ease-in-out infinite alternate;
        }
        /* Hiệu ứng khi nhấn vào nút */
        .stButton>button:active {
            transform: scale(0.98); /* Thu nhỏ nhẹ khi nhấn */
         box-shadow: 0px 2px 4px rgba(255, 102, 0, 0.2); /* Đổ bóng nhẹ hơn khi nhấn */
    }
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
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
    img5_path = os.path.join(assets_dir, '63.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
    img5_path = os.path.join(assets_dir, '641.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
    img5_path = os.path.join(assets_dir, '65.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def background66():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img5_path = os.path.join(assets_dir, '662.png')
    img5 = get_img_as_base64(img5_path)
    # CSS tùy chỉnh cho nền và sidebar
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img5}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)