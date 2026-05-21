import streamlit as st
from ui import set_config, sidebar_branding
from data_loader import load_data
from design import ROLE_COLORS

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# Page setup (Design kommt aus ui.py)
# --------------------------------------------------
set_config()
sidebar_branding()


# --------------------------------------------------
# Story-Header
# --------------------------------------------------
st.divider()
st.markdown("""
<div style="
    background-color:#000000;
    padding:18px;
    border-radius:8px;
    text-align:center;
    max-width:720px;
    margin:0 auto;
">
  <h2 style="
      font-size:34px;
      color:#f5c77a;
      font-family:Georgia;
      margin-bottom:6px;
  ">
    Bande der Gemeinschaft in Azeroth
  </h2>

  <p style="
      font-size:22px;
      color:#d8cfc4;
      margin-top:0;
      margin-bottom:12px;
  ">
    Gilden offenbaren, wie Zusammenhalt Helden länger an diese Welt bindet.
  </p>

  <p style="
      font-size:20px;
      color:#bbb;
      margin:0 auto;
  ">
    In dieser Analyse betrachten wir zwei Aspekte der Spielerschaft:<br><br>
    <b>1.</b> Wie verteilen sich Spieler über die verschiedenen Levelgruppen?<br>
    <b>2.</b> Unterscheidet sich die Verweildauer zwischen Solo- und Gildenspielern
    über diese Levelgruppen hinweg?
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()


# --------------------------------------------------
# Daten laden
# --------------------------------------------------
df = load_data()


# ==================================================
# PLOT 1 – Levelgruppen-Verteilung
# ==================================================
st.subheader('Aufteilung der Levelgruppen')

lv_group = df['level_group'].value_counts()

role_palette = list(ROLE_COLORS.values())
colors = role_palette[:len(lv_group)]

fig1, ax1 = plt.subplots(figsize=(4.2, 4.2))
fig1.patch.set_facecolor('#000000')
ax1.set_facecolor('#000000')

ax1.pie(
    lv_group,
    labels=lv_group.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'color': '#f5f5f5', 'fontsize': 9}
)

ax1.set_title(
    'Aufteilung der Levelgruppen',
    color='#f5f5f5',
    pad=6,
    fontweight='bold'
)

ax1.axis('equal')
fig1.tight_layout(pad=0.6)
st.pyplot(fig1, clear_figure=True)


# ==================================================
# PLOT 2 – Median-Verweildauer (Solo vs. Gilde)
# ==================================================
st.subheader('Median-Verweildauer je Levelgruppe (Solo vs. Gilde)')

df2 = df.copy()

# Levelgruppen (5er-Schritte)
df2['level_group'] = ((df2['level'] - 1) // 5) * 5 + 1
df2['level_group'] = (
    df2['level_group'].astype(int).astype(str)
    + '-'
    + (df2['level_group'] + 4).astype(int).astype(str)
)

# time_plot sicher als datetime
df2['time_plot'] = pd.to_datetime(df2['time_plot'], errors='coerce')
df2 = df2.dropna(subset=['time_plot'])

# Verweildauer je Charakter & Levelgruppe
stay = (
    df2.groupby(['char', 'level_group'], as_index=False)
       .agg(
           start=('time_plot', 'min'),
           end=('time_plot', 'max'),
           is_guild_player=('is_guild_player', 'max')
       )
)

stay['duration_days'] = (
    (stay['end'] - stay['start']).dt.total_seconds() / 86400
)

stay = stay[stay['duration_days'] > 0]

# Median je Levelgruppe & Spielstil
med = stay.pivot_table(
    index='level_group',
    columns='is_guild_player',
    values='duration_days',
    aggfunc='median'
)

# Sortierung nach Startlevel
order = (
    med.index.to_series()
    .astype(str)
    .str.extract(r'(\d+)')[0]
    .astype(int)
)
med = med.loc[order.sort_values().index]


# --------------------------------------------------
# Plot
# --------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(5.0, 2.8))
fig2.patch.set_facecolor('#000000')
ax2.set_facecolor('#000000')

ax2.plot(
    med.index,
    med.get(False),
    marker='o',
    label='Solo',
    color=ROLE_COLORS.get('DPS')
)

ax2.plot(
    med.index,
    med.get(True),
    marker='o',
    label='Gilde',
    color=ROLE_COLORS.get('Healer')
)

ax2.set_title(
    'Median-Verweildauer je Levelgruppe',
    color='#f5f5f5',
    pad=6,
    fontweight='bold'
)

ax2.set_xlabel('Levelgruppe', color='#f5f5f5')
ax2.set_ylabel('Median Verweildauer (Tage)', color='#f5f5f5')

ax2.tick_params(axis='x', rotation=45, labelsize=9, colors='#f5f5f5')
ax2.tick_params(axis='y', labelsize=9, colors='#f5f5f5')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color('#2a2a2a')
ax2.spines['bottom'].set_color('#2a2a2a')

ax2.grid(True, alpha=0.25)
ax2.legend(frameon=False, labelcolor='#f5f5f5')

fig2.tight_layout(pad=0.6)
st.pyplot(fig2, clear_figure=True)


# --------------------------------------------------
# Abschluss
# --------------------------------------------------
st.markdown(
    """<h1 style="text-align:center; color:#f5c77a; font-size:30px;">Gemeinschaft erhöht Bindung.</h1>""",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center; font-size:22px; color:#DDDDDD; line-height:1.6; max-width:720px; margin:0 auto;">
        <p>Wer gemeinsam spielt, bleibt länger, spielt regelmäßiger und investiert mehr Zeit.</p>
        <p>World of Warcraft ist damit nicht nur ein Online-Spiel —</p>
        <p>sondern ein sozialer Raum, in dem Beziehungen und Zusammenarbeit entscheidend sind.</p>
    </div>
    """,
    unsafe_allow_html=True
)
