import streamlit as st
st.set_page_config(layout="wide")

from logics.date_range import date_range
from pages.User_Engagement_and_Activity import user_engagement_activity
from logics.export_data import export_data

# Hide all default pages using custom CSS
st.markdown('''
    <style>
        [data-testid="stSidebarNav"] > ul {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            height: auto !important;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
''', unsafe_allow_html=True)

def main():
    # Custom sidebar navigation
    st.sidebar.page_link("main.py", label="🏠 Overview")
    st.sidebar.page_link("pages/Google_Ads_Performance.py", label="📊 Google")
    st.sidebar.page_link("pages/facebook_ads.py", label="👥 Facebook")
    st.sidebar.page_link("pages/instagram_data.py", label="📷 Instagram")

    st.sidebar.divider()
    start_date, end_date = date_range()

    export_button = st.sidebar.toggle("Export_Data")
    if export_button:
        export_data(start_date, end_date)

    user_engagement_activity(start_date, end_date)

if __name__ == '__main__':
    main()
