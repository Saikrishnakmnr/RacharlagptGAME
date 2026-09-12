import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="RacharlaGPT Challenge",
    page_icon="🎮",
    layout="centered",
)

html_file = Path(__file__).parent / "RacharlaGPT_Challenge.html"

html = html_file.read_text(encoding="utf-8")

st.components.v1.html(
    html,
    height=900,
    scrolling=False,
)
