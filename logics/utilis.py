from dotenv import load_dotenv
from pages.User_Engagement_and_Activity import *
import os

from logics.fetch_google_analytics_data import initialize_ga4_client
from logics.fetch_google_analytics_data import get_metadata

from logics.fetch_instagram import get_valid_metrics_by_days


def load_google_api():
    try:
        # Load environment variables from .env
        load_dotenv()
        # Get the key path from the environment variable
        key_path = os.getenv('KEY_PATH')
        if key_path is None:
            print("Warning: KEY_PATH is not defined in the environment.")
        # Check if all loaded variables are present in the environment
        if not os.environ.get('KEY_PATH'):
            print('Warning: KEY_PATH is not present in the environment.')
        else:
            print('Correctly deploy need to  Users')
        # Initialize Google Analytics 4 client
        client = initialize_ga4_client()
        # client = initialize_ga4_client(key_path)
        if client is None:
            raise ValueError("Failed to initialize GA4 client")
        property_id = '323323366'
        # client = initialize_ga4_client(key_path)
        dimensions, metrics = get_metadata(client, property_id)

        return client, property_id, dimensions, metrics
    
    except ValueError as e:
        print(f"ValueError: {e}")

    except Exception as e:
        print(f"Error fetching data: {e}")


def facebook_apis_tokens():
    page_access_token    = 'EAAOBMtxoGREBO9d80DZANBLqLYIcA7hbR6F0jiskumtfZCi8pudZBkmpWghpFR2gS0EqLitboAQitWyzeHamknBjJ3pMzGkiUKYWKG8ZAZCNUb1ihAwxImHDTbkqEFSU63HiTVAg5ZBj2JIXryVS0ZAPvkZAHEFbKdZA976E52WEdpqvrLSRUl9HONvJGs7XSZBQZDZD' #st.secrets["access_tokens"]["page_access_token"]
    user_access_token    = 'EAAOBMtxoGREBO58g9ObISpWDNaseWBelRO5FwZCdm4MPdpA6EZAqxKUK9DkKbaNPeTi0U16m0qYyQUGyZBkFzyX9YxdzFfNZCk9Md3OBv8DBrYAq4GEVr3e5rcgrjRz4ZAznNGjaGhiCu1I4r2dTG2gClHfGATERvdv6sloNLnw3xhl3vh1fVKQZDZD' #st.secrets["access_tokens"]["user_access_token"]
    page_id              = '1060285064080786' #st.secrets["facebook"]["page_id"]
    adaccount_account_id = st.secrets["adaccount"]["adaccount_account_id"]
    adaccount_id         = st.secrets["adaccount"]["adaccount_id"]

    return page_access_token, user_access_token, page_id, adaccount_account_id, adaccount_id


def instagram_api_data_fetch():
    metrics = get_valid_metrics_by_days()
    period   = 'day'
    lifetime = None

    return metrics, period, lifetime