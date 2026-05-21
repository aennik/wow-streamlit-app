import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import streamlit as st

from ui import set_config, sidebar_branding
from design import CLASS_COLORS, RACE_COLORS
from data_loader import load_data


set_config()
sidebar_branding()

# Überschriften :
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
    Spuren der Identität in Azeroth
  </h2>

  <p style="
      font-size:22px;
      color:#d8cfc4;
      margin-top:0;
      margin-bottom:0;
  ">
    Die Wahl von Klasse und Rasse zeigt, wie Abenteurer ihre Rolle in dieser Welt definieren.
  </p>
</div>
""", unsafe_allow_html=True)
st.divider()

# Daten laden :
df = load_data()

classes = sorted(df['charclass'].dropna().unique())

selected_races = st.multiselect(
    'Rassen auswählen',
    sorted(df['race'].dropna().unique()),
    default=['Orc', 'Tauren', 'Troll'] if all(r in df['race'].unique() for r in ['Orc', 'Tauren', 'Troll']) else sorted(df['race'].dropna().unique())[:3]
)

# PLOT 1: Rassenverteilung

fig1, ax1 = plt.subplots(figsize=(8.5, 3.2))
fig1.patch.set_facecolor('#000000')
ax1.set_facecolor('#000000')

sns.countplot(
    data=df,
    x='race',
    order=df['race'].value_counts().index,
    palette=RACE_COLORS,
    ax=ax1
)

ax1.set_title('Verteilung der Rassen', color='#f5f5f5', pad=8, fontweight='bold')
ax1.set_xlabel('Rasse', color='#f5f5f5')
ax1.set_ylabel('Anzahl Charaktere', color='#f5f5f5')

ax1.tick_params(axis='x', rotation=45, labelsize=9, colors='#f5f5f5')
ax1.tick_params(axis='y', labelsize=9, colors='#f5f5f5')

# --- KEINE Scientific Notation ---
ax1.ticklabel_format(axis='y', style='plain', useOffset=False)
ax1.yaxis.get_offset_text().set_visible(False)
ax1.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#2a2a2a')
ax1.spines['bottom'].set_color('#2a2a2a')

ax1.grid(True, axis='y', alpha=0.20)

fig1.tight_layout(pad=0.6)
st.pyplot(fig1, clear_figure=True)

st.divider()


# Filter
selected_classes = st.multiselect(
    'Klassen auswählen',
    classes,
    default=classes
)

df_f = df[
    df['race'].isin(selected_races) &
    df['charclass'].isin(selected_classes)
].copy()

# PLOT 2: Klassenverteilung
class_order = df_f['charclass'].value_counts().index

fig2, ax2 = plt.subplots(figsize=(8.5, 3.2))
fig2.patch.set_facecolor('#000000')
ax2.set_facecolor('#000000')

sns.countplot(
    data=df_f,
    x='charclass',
    order=class_order,
    palette=CLASS_COLORS,
    ax=ax2
)

ax2.set_title('Verteilung der Klassen', color='#f5f5f5', pad=8, fontweight='bold')
ax2.set_xlabel('Klasse', color='#f5f5f5')
ax2.set_ylabel('Anzahl Charaktere', color='#f5f5f5')

ax2.tick_params(axis='x', rotation=45, labelsize=9, colors='#f5f5f5')
ax2.tick_params(axis='y', labelsize=9, colors='#f5f5f5')

# --- KEINE Scientific Notation ---
ax2.ticklabel_format(axis='y', style='plain', useOffset=False)
ax2.yaxis.get_offset_text().set_visible(False)
ax2.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.'))
)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color('#2a2a2a')
ax2.spines['bottom'].set_color('#2a2a2a')

ax2.grid(True, axis='y', alpha=0.20)

fig2.tight_layout(pad=0.6)
st.pyplot(fig2, clear_figure=True)

st.divider()

# PLOT 3: Relative Klassenverteilung innerhalb der Rassen (100%)
class_order_3 = [c for c in CLASS_COLORS.keys() if c in df_f['charclass'].unique()]
race_class_ct = pd.crosstab(df_f['race'], df_f['charclass'])

if class_order_3:
    race_class_ct = race_class_ct[class_order_3]

race_class_pct = race_class_ct.div(race_class_ct.sum(axis=1), axis=0) * 100
colors_3 = [CLASS_COLORS[c] for c in class_order_3] if class_order_3 else None

fig3, ax3 = plt.subplots(figsize=(9.2, 3.8))
fig3.patch.set_facecolor('#000000')
ax3.set_facecolor('#000000')

race_class_pct.plot(
    kind='bar',
    stacked=True,
    color=colors_3,
    ax=ax3
)

ax3.set_title('Relative Klassenverteilung innerhalb der Rassen (100%)', color='#f5f5f5', pad=8, fontweight='bold')
ax3.set_xlabel('Rasse', color='#f5f5f5')
ax3.set_ylabel('Anteil (%)', color='#f5f5f5')

ax3.tick_params(axis='x', rotation=0, labelsize=9, colors='#f5f5f5')
ax3.tick_params(axis='y', labelsize=9, colors='#f5f5f5')

ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_color('#2a2a2a')
ax3.spines['bottom'].set_color('#2a2a2a')

ax3.grid(True, axis='y', alpha=0.20)

leg = ax3.legend(title='Klasse', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False)
if leg:
    plt.setp(leg.get_texts(), color='#f5f5f5')
    plt.setp(leg.get_title(), color='#f5f5f5')

fig3.tight_layout(pad=0.6)
st.pyplot(fig3, clear_figure=True)

# Fazit
st.markdown(
    """<h1 style="text-align:center; color:#f5c77a; font-size:30px;">Identität prägt den Weg..</h1>""",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center; font-size:22px; color:#DDDDDD; line-height:1.6; max-width:720px; margin:0 auto;">
        <p>Die Verteilung zeigt, dass Spieler ihre Charaktere nach Zugehörigkeit und Vorstellung formen.</p>
        <p>Die Charaktererstellung ist für viele Spieler der erste emotionale Einstieg ins Spiel.</p>
        <p>Klasse und Rasse sind keine bloßen Attribute, sondern Teil einer selbstgewählten Rolle innerhalb der Spielwelt.</p>
        <p>World of Warcraft beginnt für viele Spieler also nicht beim Gameplay —</p>
        <p>sondern bereits bei der Frage:</p>
        <p>„Wer möchte ich in dieser Welt sein?"</p>
    </div>
    """,
    unsafe_allow_html=True
)

