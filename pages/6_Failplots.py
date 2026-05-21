import streamlit as st
import glob
from ui import sidebar_branding, page_header

sidebar_branding()
st.divider()
st.markdown("""
<div style="
    background-color:#000000;
    padding:16px;
    border-radius:8px;
    text-align:center;
">
  <h2 style="
      font-size:36px;
      color:#f5c77a;
      font-family:Georgia;
      margin-bottom:6px;
  ">
    Failplots 😄
  </h2>

  <p style="
      font-size:22px;
      color:#aaa;
      margin-top:0;
      margin-bottom:0;
  ">
    Statische Bilder – bewusst ohne großes Design.
  </p>
</div>
""", unsafe_allow_html=True)
st.divider()


files = []
files += sorted(glob.glob('plot_fails/*.png'))
files += sorted(glob.glob('plot_fails/*.jpg'))
files += sorted(glob.glob('plot_fails/*.jpeg'))

if not files:
    st.warning('Lege Failplot-Bilder in plot_fails/ ab (png/jpg).')
else:
    cols = st.columns(3)
    for i, fp in enumerate(files):
        cols[i % 3].image(fp, width='stretch', caption=fp.split('/')[-1])
