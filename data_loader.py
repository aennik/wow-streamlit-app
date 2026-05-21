import pandas as pd
import streamlit as st
from pathlib import Path

DATA_PATH = Path('data') / 'wowah_full_clean.parquet'

@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    df = pd.read_parquet(DATA_PATH)
    df.columns = [c.strip() for c in df.columns]
    return df