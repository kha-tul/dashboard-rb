import streamlit as st

from plots.plots_user_engagement_and_activity import *
from plots.cards import *

from logics.utilis import load_google_api
from logics.load_data import google_analytics_data_load

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


def user_engagement_activity(start_date, end_date):
    client, property_id, dimensions, metrics = load_google_api()
    data_, rose_pie_data_, eventCount_data_, sunbrust_data_ = google_analytics_data_load(client, property_id, start_date, end_date)

    data = pd.DataFrame(data_)
    rose_pie = pd.DataFrame(rose_pie_data_)
    eventCount = pd.DataFrame(eventCount_data_)
    sunbrust_data = pd.DataFrame(sunbrust_data_)

    data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')
    data['dayOfWeek'] = pd.to_datetime(data['date']).dt.day_name()
    data['sessions'] = pd.to_numeric(data['sessions'], errors='coerce')
    data = data.dropna(subset=['sessions'])

    # Cards in a single row
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with col1:
        title = "Total de Países"
        cards(title, int(data['country'].nunique()))
    with col2:
        title = "Sessões"
        cards(title, int(data['sessions'].nunique()))
    with col3:
        title = "Sessões Engajadas"
        cards(title, int(data['engagedSessions'].nunique()))
    with col4:
        title = "Duração Média da Sessão"
        cards(title, round(data['averageSessionDuration'].nunique(), 2))
    with col5:
        title = "Contagem de Eventos"
        cards(title, int(data['eventCount'].nunique()))
    with col6:
        title = "Visualizações de Páginas/Telas"
        cards(title, int(data['screenPageViews'].nunique()))

    st.divider()

    # First chart
    bounceRate_engagementRate_engagedSessions(data)
    st.divider()
    
    # Second and third charts in same row
    col1, col2 = st.columns(2)
    with col1:
        dauPerMau_wauPerMau(data)
    with col2:
        source_activeUsers(rose_pie)
    st.divider()
    
    # Rest of the charts in single rows
    eventName_eventCount_eventCountPerUser(eventCount)
    st.divider()
    
    averageSessionDuration_continent(data)
    st.divider()
    
    screenPageViews_operatingSystem(data)
    st.divider()
    
    sessionSourceMedium_screenPageViews(data)
    st.divider()
    
    session_over_time(data)
    st.divider()
    
    session_over_dayOfWeeks(data)
    st.divider()
    
    session_over_OS_Device_Browser(sunbrust_data)
