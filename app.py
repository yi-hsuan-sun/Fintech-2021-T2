import streamlit as st
import app_overall_news
import app_keyword_search
import app_categories
import app_ppt
import app_positive_rate

import SessionState

st.set_page_config(layout="wide")
# set the width of sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="0"] > div:first-child {
        width: 200px;
        margin-left: -200px;
    }
    .stButton>button {
    height: 2em;
    width: 10em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
PAGES = {
    "Selected News": app_overall_news,
    "By Categories": app_categories,
    "Keyword Search": app_keyword_search,
    "Positive Rate": app_positive_rate,
    "PPT Generator": app_ppt    
}
st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()
st.sidebar.markdown('\n')
PAGES_keys = list(PAGES.keys())
button_0 = st.sidebar.button(PAGES_keys[0])
button_1 = st.sidebar.button(PAGES_keys[1])
button_2 = st.sidebar.button(PAGES_keys[2])
button_3 = st.sidebar.button(PAGES_keys[3])
button_4 = st.sidebar.button(PAGES_keys[4])

s = SessionState.get(b0=0, b1=0, b2=0, b3=0, b4=0)

# not the first page
if sum([s.b0, s.b1, s.b2, s.b3, s.b4]) == 1:     
    last_button = [s.b0, s.b1, s.b2, s.b3, s.b4].index(1)
    # st.markdown([button_0, button_1, button_2, button_3])
    # st.markdown([s.b0, s.b1, s.b2, s.b3])
    this_button = [i for i, x in enumerate([button_0, button_1, button_2, button_3, button_4]) if x]
    # if a button is pressed
    if this_button: 
        # and it's a new button 
        if last_button != this_button:
            # change page
            if last_button == 0:
                s.b0 = 0
            elif last_button == 1:
                s.b1 = 0
            elif last_button == 2:
                s.b2 = 0
            elif last_button == 3:
                s.b3 = 0
            else:
                s.b4 = 0

# first page / we don't have to change page
if button_0 or s.b0:
    s.b0 = 1
    PAGES[PAGES_keys[0]].app()
if button_1 or s.b1:
    s.b1 = 1
    PAGES[PAGES_keys[1]].app()
if button_2 or s.b2:
    s.b2 = 1
    PAGES[PAGES_keys[2]].app()
if button_3 or s.b3:
    s.b3 = 1
    PAGES[PAGES_keys[3]].app()
if button_4 or s.b4:
    s.b4 = 1
    PAGES[PAGES_keys[4]].app()
