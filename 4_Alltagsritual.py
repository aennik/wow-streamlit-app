import streamlit as st
from ui import sidebar_branding, page_header
from utils4 import (
    load_data,
    get_daily_active,
    get_activity_by_hour,
    autoplay_video,
    plot_daily_active,
    plot_activity_by_hour,
)

# sidebar_branding()
# page_header('Alltagsritual – Wie?', 'Aktivität über Tageszeiten und wiederkehrende Routinen.')

# MUSS ganz oben stehen
st.set_page_config(layout="wide", page_title="Chroniken von Azeroth")


# Head
st.divider()
st.markdown("""
<div style="
    background-color:#000000;
    padding:20px;
    border-radius:8px;
    text-align:center;
">
  <h1 style="font-size:56px; color:#f5c77a; font-family:Georgia; margin-bottom:10px;">
    Chroniken des Lebens in Azeroth
  </h1>
  <p style="font-size:30px; color:#ccc; margin-top:0;">
    Server-Snapshots erzählen die Geschichte, wann Abenteurer Azeroth bevölkerten.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

autoplay_video("assets/clock.mp4", width_percent=70)
st.divider()

wow_df = load_data()
daily_active = get_daily_active(wow_df)
activity_by_hour = get_activity_by_hour(wow_df)

fig1 = plot_daily_active(daily_active)
st.plotly_chart(fig1, width="stretch")

st.divider()

fig2 = plot_activity_by_hour(activity_by_hour)
st.pyplot(fig2)

st.divider()

st.markdown(
    """<h1 style="text-align:center; color:#f5c77a;">Was die Chroniken flüstern...</h1>""",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center; font-size:26px; color:#DDDDDD; line-height:1.6;">
        <p>• Der Tageszyklus zeigt, wie sich Aktivität über die Zeit verändert.</p>
        <p>• Der Stundenplot zeigt den durchschnittlichen Tagesrhythmus.</p>
        <p>• Für Aussagen zur Spieldauer bräuchte man zusammenhängende Zeitreihen pro Charakter.</p>
    </div>
    """,
    unsafe_allow_html=True
)
