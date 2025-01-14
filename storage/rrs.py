import streamlit as st

def page_2():
    st.title("RRS")

pg = st.navigation([st.Page("gamification.py"), st.Page(page_2)])
pg.run()