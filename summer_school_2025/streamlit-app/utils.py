import os
import joblib
import streamlit as st

from streamlit_gsheets import GSheetsConnection


@st.cache_data()
def load_artifact(file):
    # Uncomment for local deployment
    # path_artifact = r"saved_models/"
    
    # For streamlit cloud deployment, specify the relative path to the saved models from the root of the github repository
    path_artifact = r"summer_school_2025/streamlit-app/saved_models/saved_models/"
    
    artifact = joblib.load(os.path.join(path_artifact, file))
    return artifact

