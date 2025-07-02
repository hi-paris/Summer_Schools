import os
import joblib
import streamlit as st

from streamlit_gsheets import GSheetsConnection


@st.cache_data()
def load_artifact(file):
    # Uncomment for local deployment
    # path_artifact = r"saved_models/"
    
    # For streamlit cloud deployment, specify the relative path to the saved models from the root of the github repository
    base = os.path.dirname(__file__)  # path to streamlit-app/
    path_artifact = os.path.join(base, "saved_models", file)
    artifact = joblib.load(path_artifact)
    return artifact

