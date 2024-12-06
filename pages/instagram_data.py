import streamlit as st

from logics.date_range import *

from plots.plots_instagram import *
from plots.cards import *

from logics.load_data import instagram_data_load


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


st.sidebar.page_link("main.py", label="Overview", icon="🏠")
st.sidebar.page_link("pages/Google_Ads_Performance.py",       label="Google",       icon="👥", disabled=False)
st.sidebar.page_link("pages/facebook_ads.py",                 label="Facebook",     icon="👥", disabled=False)
st.sidebar.page_link("pages/instagram_data.py",               label="Instagram",    icon="👥", disabled=False)

access_token            = 'EAAOBMtxoGREBO58g9ObISpWDNaseWBelRO5FwZCdm4MPdpA6EZAqxKUK9DkKbaNPeTi0U16m0qYyQUGyZBkFzyX9YxdzFfNZCk9Md3OBv8DBrYAq4GEVr3e5rcgrjRz4ZAznNGjaGhiCu1I4r2dTG2gClHfGATERvdv6sloNLnw3xhl3vh1fVKQZDZD' #st.secrets["access_tokens"]["user_access_token"]
instagram_user_id       = st.secrets["instagram"]["instagram_user_id"]

start_date, end_date = date_range()

export_button = st.sidebar.toggle("Export_Data")
if export_button:
    export_data(start_date, end_date)


if instagram_user_id and access_token:
    try:
        (dates,  ig_insights_by_total_values, 
         impressions_values, reach_values, 
         profile_views_values, follower_count_values, 
         email_contacts, phone_call_clicks, 
         text_message_clicks, get_directions_clicks, 
         website_clicks) = instagram_data_load(instagram_user_id, access_token, start_date, end_date)

        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            total_impressions = pd.DataFrame(impressions_values)
            title = "Total de Impressões Mensais"
            cards(title , total_impressions.sum()[0])
        with col2:
            total_page_reach = pd.DataFrame(reach_values)
            title = "Alcance da Página Mensal"
            cards(title , total_page_reach.sum()[0])
        with col3:
            total_profile_views = pd.DataFrame(profile_views_values)
            title = "Visualizações de Perfil Mensal"
            cards(title , total_profile_views.sum()[0])
        with col4:
            total_followers_count = pd.DataFrame(follower_count_values)
            title = "Seguidores Mensais"
            cards(title , total_followers_count.sum()[0])

        st.divider()

        inst_page_impression_reach_profile_views(impressions_values, reach_values, profile_views_values, dates)
        inst_profile_view_followers(profile_views_values, follower_count_values)

        st.divider()

        phone_text_website_get_directions(phone_call_clicks, text_message_clicks, 
                                            get_directions_clicks, website_clicks, dates)
        sum_phone_text_website_get_directions(phone_call_clicks, text_message_clicks, 
                                            get_directions_clicks, website_clicks, dates)  
        st.divider()

        col1, col2 = st.columns([1.9,1])
        with col1:
            total_likes_by_titled_line_plot(ig_insights_by_total_values)
        with col2:
            total_likes_by_titled_pie_chart(ig_insights_by_total_values)          
    except:
        pass


