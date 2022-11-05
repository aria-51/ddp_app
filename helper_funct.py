import streamlit as st
import glob, random

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "your guide: bob";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def get_random_artwork(n):
    file_path_type = ["./album_covers/*.jpg"]
    images = glob.glob(random.choice(file_path_type))
    image_list =[]
    for i in range(n):
        image_list.append(random.choice(images))
    return image_list