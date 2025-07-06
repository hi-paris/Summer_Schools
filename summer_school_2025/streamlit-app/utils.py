import os
import joblib
import streamlit as st

from streamlit_gsheets import GSheetsConnection


@st.cache_data()
def load_artifact(file):
    base = os.path.dirname(__file__)
    path_artifact = os.path.join(base, "saved_models", file)
    artifact = joblib.load(path_artifact)
    return artifact

