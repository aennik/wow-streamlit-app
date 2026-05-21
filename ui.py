import streamlit as st

# Allgemein
def set_config():
    st.set_page_config(
        page_title='WoW Account History Dataset',
        layout='centered'
    )

    st.markdown(
        """
        <style>
        .block-container {
            max-width: 1240px !important;
            padding-top: 1.8rem;
            padding-bottom: 2.0rem;
        }
        hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.10);
            margin: 1.1rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar
def sidebar_branding():
    st.sidebar.markdown('**Fraktion:** Horde')

    st.sidebar.markdown('---')
    st.sidebar.caption('Story-Reihenfolge:')
    st.sidebar.write('1) Identität')
    st.sidebar.write('2) Motivation')
    st.sidebar.write('3) Gewohnheit')
    st.sidebar.write('4) Gemeinschaft')
    st.sidebar.markdown('---')


# Page Header
def page_header(title: str, subtitle: str = ''):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.markdown('---')


def framed_layout(left_paths: list[str], right_paths: list[str], center_ratio: int = 8):
    left, center, right = st.columns([1, center_ratio, 1], vertical_alignment='top')

    with left:
        for p in left_paths:
            st.image(p, width=64)

    with right:
        for p in right_paths:
            st.image(p, width=64)

    return center
