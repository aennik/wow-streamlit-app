import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import base64

WOW_GOLD = "#f5c77a"
WOW_BLUE = "#E57A1F"

@st.cache_data
def load_data(parquet_path: str = "data/wowah_full_clean.parquet") -> pd.DataFrame:
    df = pd.read_parquet(parquet_path)
    df["time_plot"] = pd.to_datetime(df["time_plot"], errors="coerce")
    df = df.dropna(subset=["time_plot"])
    return df

@st.cache_data
def get_daily_active(df: pd.DataFrame) -> pd.DataFrame:
    tmp = df.copy()
    tmp["date"] = tmp["time_plot"].dt.date
    return (
        tmp.groupby("date")["char"]
        .count()
        .reset_index(name="unique_chars")
        .sort_values("date")
    )


@st.cache_data
def get_activity_by_hour(df: pd.DataFrame):
    return df["time_plot"].dt.hour.value_counts().sort_index()


@st.cache_data
def _video_base64(video_path: str) -> str:
    with open(video_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def autoplay_video(video_path: str, width_percent: int = 70):
    encoded = _video_base64(video_path)
    st.markdown(
        f"""
        <video autoplay muted playsinline
               style="width:{width_percent}%; border-radius:16px; display:block; margin:auto;">
            <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )


def plot_daily_active(daily_active: pd.DataFrame):
    fig = px.line(daily_active, x="date", y="unique_chars", markers=True)
    fig.update_layout(
        title=dict(
            text="Kapitel I – Der Tageszyklus",
            font=dict(size=40, color=WOW_GOLD),
            x=0.5,
            xanchor="center"),
        xaxis_title="Datum",
        yaxis_title="Charaktere",
        xaxis_title_font=dict(size=30, color="rgba(230,230,230,0.9)"),
        yaxis_title_font=dict(size=30, color="rgba(230,230,230,0.9)"),
        xaxis=dict(tickfont=dict(size=20, color="rgba(230,230,230,0.85)"), title_standoff=50),
        yaxis=dict(tickfont=dict(size=20, color="rgba(230,230,230,0.85)"), title_standoff=50, tickformat=",d"),
        paper_bgcolor="black",
        plot_bgcolor="black",
        height=500,
        margin=dict(t=160, b=80, l=80, r=40)
    )
    fig.update_traces(line=dict(color=WOW_BLUE, width=3), marker=dict(size=6, color=WOW_GOLD))
    return fig


def plot_activity_by_hour(activity_by_hour):
    fig, ax = plt.subplots(figsize=(20, 4))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.plot(activity_by_hour.index, activity_by_hour.values,
            color=WOW_BLUE, marker="o", linewidth=2,
            markerfacecolor=WOW_GOLD, markeredgecolor=WOW_GOLD)

    ax.set_xlabel("Stunde des Tages", labelpad=25, fontsize=14, color="white")
    ax.set_ylabel("Charaktere", labelpad=25, fontsize=14, color="white")
    ax.set_title("Kapitel II – Die Rückkehr am Abend", fontsize=20, color=WOW_GOLD, pad=25, fontweight="bold")
    ax.set_xticks(range(0, 24))
    ax.grid(True, color="white", alpha=0.15, linestyle="--")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.ticklabel_format(style="plain", axis="y")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")

    fig.tight_layout(rect=[0, 0, 1, 0.88])
    return fig
