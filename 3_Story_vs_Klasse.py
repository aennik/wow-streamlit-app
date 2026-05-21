import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from ui import sidebar_branding, page_header
from data_loader import load_data
from design import ROLE_MAP, ROLE_COLORS

# --------------------------------
# Page setup
# --------------------------------
sidebar_branding()
st.divider()
st.markdown("""
<div style="
    background-color:#000000;
    padding:20px;
    border-radius:8px;
    text-align:center;
">
  <h2 style="
      font-size:40px;
      color:#f5c77a;
      font-family:Georgia;
      margin-bottom:8px;
  ">
    Pfade der Legenden in Azeroth
  </h2>

  <p style="
      font-size:26px;
      color:#d8cfc4;
      margin-top:0;
      margin-bottom:0;
  ">
    Spieler folgen nicht nur Mechaniken, sondern den Geschichten, die ihre Charaktere verkörpern.
  </p>
</div>
""", unsafe_allow_html=True)
st.divider()

df = load_data()

# Heatmap
race_class_ct = pd.crosstab(df['race'], df['charclass'])

fig, ax = plt.subplots(figsize=(9, 3))
fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')

hm = sns.heatmap(
    race_class_ct,
    annot=True,
    fmt='d',
    cmap='Oranges',
    vmin=0,
    linewidths=0.5,
    linecolor='#2a2a2a',
    annot_kws={
        'color': '#000000',
        'fontsize': 9,
        'fontweight': 'bold'
    },
    ax=ax
)

ax.set_title('Heatmap: Rasse × Klasse (Counts)', pad=8, fontweight='bold', color='#f5f5f5')
ax.set_xlabel('Klasse', color='#f5f5f5')
ax.set_ylabel('Rasse', color='#f5f5f5')
ax.tick_params(axis='x', rotation=35, labelsize=9, colors='#f5f5f5')
ax.tick_params(axis='y', rotation=0, labelsize=9, colors='#f5f5f5')

cbar = hm.collections[0].colorbar
cbar.ax.tick_params(colors='#f5f5f5', labelsize=9)

cbar.formatter = mticker.FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
cbar.update_ticks()

fig.tight_layout(pad=0.5)
st.pyplot(fig, clear_figure=True)

st.markdown('---')

# Barplot Beliebtheit Klassen nach Rolle
class_counts = df['charclass'].value_counts()

colors = [
    ROLE_COLORS.get(ROLE_MAP.get(cls, 'DPS'))
    for cls in class_counts.index
]

fig, ax = plt.subplots(figsize=(9, 3))
fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')

ax.bar(class_counts.index, class_counts.values, color=colors)

ax.set_title(
    'Beliebtheit der Klassen nach Rolle',
    fontsize=12,
    pad=8,
    fontweight='bold',
    color='#f5f5f5'
)
ax.set_xlabel('Klasse', color='#f5f5f5')
ax.set_ylabel('Anzahl Charaktere', labelpad=10, color='#f5f5f5')

ax.tick_params(axis='x', rotation=35, labelsize=9, colors='#f5f5f5')
ax.tick_params(axis='y', labelsize=9, colors='#f5f5f5')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#2a2a2a')
ax.spines['bottom'].set_color('#2a2a2a')

ax.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
)

fig.tight_layout(pad=0.5)
st.pyplot(fig, clear_figure=True)

st.markdown(
    """<h1 style="text-align:center; color:#f5c77a;">Geschichten geben die Richtung vor...</h1>""",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center; font-size:26px; color:#DDDDDD; line-height:1.6;">
        <p>Beliebte Klassen stehen für Archetypen, mit denen sich Spieler besonders identifizieren.</p>
    </div>
    """,
    unsafe_allow_html=True
)
