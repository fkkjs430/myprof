from pathlib import Path

import streamlit as st

st.title("나만의 작은 교수님")
from st_pages import Page, add_page_title, show_pages, Section

show_pages(
        [   Page("streamlit_app.py", "Home", icon=":🏠:"),
            # Can use :<icon-name>: or the actual icon
            Section(name="전공목록"),
            # The pages appear in the order you pass them
            Page("example_app/AI대학원.py", "AI대학원"),
            Page("example_app/물리광과학과.py", name="물리광과학과"),
            # Will use the default icon and name based on the filename if you don't
            # pass them
            Page("example_app/전기전자컴퓨터공학부.py", "전기전자컴퓨터공학부"),
            Page("example_app/의생명공학부.py", "의생명공학부"),
        ]
)

add_page_title()  # Optional method to add title and icon to current page


"#광주과학기술원은 ~~~~ ."
"#그래서 우리는 ~~~하는 웹사이트를 통해 ~~하려고 한다."

import streamlit as st

# 페이지 제목
st.markdown("<h1 style='font-size: 24px; font-weight: bold; color: #4B8BBE;'>전공 목록</h1>", unsafe_allow_html=True)

import streamlit as st

majors = {
    "AI대학원": {
        "description": "AI대학원에 대한 설명입니다.",
        "links": {
            "홈페이지": "https://ai.university.example",
            "연구실 목록": "AI대학원"
        }
    },
    "물리광과학과": {
        "description": "물리광과학과에 대한 설명입니다.",
        "links": {
            "홈페이지": "https://physics.university.example",
            "연구실 목록": "example_app/물리광과학과.py"
        }
    },
    "전기전자컴퓨터공학부": {
        "description": "전기전자컴퓨터공학부에 대한 설명입니다.",
        "links": {
            "홈페이지": "https://eece.university.example",
            "연구실 목록": "example_app/전기전자컴퓨터공학부.py"
        }
    },
    "의생명공학부": {
        "description": "의생명공학부에 대한 설명입니다.",
        "links": {
            "홈페이지": "https://biomedical.university.example",
            "연구실 목록": "example_app/의생명공학부.py"
        }
    }
}

# 전공 목록 표시
for major, info in majors.items():
    with st.expander(f"{major}", expanded=True):
        st.write(info["description"])
        link_texts = " | ".join([f"[{text}]({url})" for text, url in info["links"].items()])
        st.markdown(link_texts)

# 페이지 로드
query_params = st.query_params
page = query_params.get("Page", ["Home"])[0]


# 페이지 로드
if page == "AI대학원":
    exec(open("example_app/AI대학원.py").read())
elif page == "물리광과학과":
    exec(open("example_app/물리광과학과.py").read())
elif page == "전기전자컴퓨터공학부":
    exec(open("example_app/전기전자컴퓨터공학부.py").read())
elif page == "의생명공학부":
    exec(open("example_app/의생명공학부.py").read())