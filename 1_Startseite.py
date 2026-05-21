import streamlit as st
from ui import sidebar_branding

sidebar_branding()

v1, v2, v3 = st.columns([0.5, 9, 0.5])

with v2:
    st.markdown(
        """
        <div style="
            background-color:#000000;
            padding:22px;
            border-radius:10px;
            text-align:center;
        ">
        """,
        unsafe_allow_html=True
    )

    st.image("assets/logo_hero.png", width=1240)

    st.markdown(
        """
        <h2 style="text-align:center;
            font-size:36px;
            color:#f5c77a;
            font-family:Georgia;
            margin-bottom:6px;
        ">
            Chroniken von Azeroth
        </h2>

        <p style="text-align:center;
            font-size:22px;
            color:#aaa;
            margin-top:0;
        ">
            Eine datengetriebene Reise durch Identität, Motivation und Gemeinschaft
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.video("assets/wow.mp4")
    st.image(
        "assets/race.png",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)




st.divider()

# ------------------------------------------------------------
# NAVIGATION – Kapitelübersicht
# ------------------------------------------------------------
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
      margin-bottom:0;
  ">
    Kapitel der Chronik
  </h2>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------------------
# KACHELN
# ------------------------------------------------------------
a, b, c = st.columns(3)

with a:
    st.markdown("### 📊 Grundplots – Wer?")
    st.page_link("pages/2_Grundplots.py", label="Zur Analyse")

    st.markdown("### 🧙 Story vs. Klasse – Warum?")
    st.page_link("pages/3_Story_vs_Klasse.py", label="Zur Analyse")

with b:
    st.markdown("### ⏰ Alltagsritual – Wie?")
    st.page_link("pages/4_Alltagsritual.py", label="Zur Analyse")

    st.markdown("### 👥 Solo vs. Gilde")
    st.page_link("pages/5_Solo_vs_Gilde.py", label="Zur Analyse")

with c:
    st.markdown("### 💥 Failplots")
    st.page_link("pages/6_Failplots.py", label="Zur Analyse")