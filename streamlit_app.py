import os
import time
import pathlib
import pages as pg
import streamlit as st
import streamlit_antd_components as sac
from portifolio import show_home

# from about import show_about
from skills import strml

st.set_page_config(
    page_title="Benson Nderitu",
    page_icon="B",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# =============LOGO============
logo = "static/logo.png"
st.logo(image=logo, size="large", icon_image=logo)


# --------------------CUSTOM CSS TO REMOVE PADDING---------------------------------------------------------------
st.markdown(
    """
        <style>
        .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 1rem 1rem 10rem;
        min-width: auto;
        max-width: initial;
        }
            """,
    unsafe_allow_html=True,
)
# -----------REMOVE GAP BETWEEN HEADER AND CONTENT ----------------
st.markdown(
    """
    <style>
    
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------Load the external CSS file ------------------
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


css_path = pathlib.Path("styles/style.css")
load_css(css_path)


# ================================================================
def main():
    tabs = sac.tabs(
        [
            sac.TabsItem(label="About Me", icon="person-circle"),
            sac.TabsItem(label="Portfolio", icon="laptop"),
            sac.TabsItem(label="Skills", icon="rocket"),
        ],
        align="center",
        size="md",
        variant="outline",
    )

    if tabs == "About Me":
        with st.container(key="about"):
            st.write("About me")
    elif tabs == "Portfolio":

        @st.cache_data()
        def get_project_cards():
            return [
                {
                    "projectId": 1,
                    "projectTitle": "Project One",
                    "images": [
                        "static/project_images/1.png",
                        "static/project_images/2.png",
                    ],
                    "projectDescription": "This is the description for Project One.",
                    "publishDate": "2023-12-10",
                    "updateDate": "2023-12-12",
                },
                {
                    "projectId": 2,
                    "projectTitle": "Project Two",
                    "images": [
                        "static/project_images/1.png",
                        "static/project_images/2.png",
                    ],
                    "projectDescription": "This is the description for Project Two.",
                    "publishDate": "2023-11-20",
                    "updateDate": "2023-11-25",
                },
                {
                    "projectId": 3,
                    "projectTitle": "Project Three",
                    "images": [
                        "static/project_images/1.png",
                        "static/project_images/2.png",
                    ],
                    "projectDescription": "This is the description for Project Three.",
                    "publishDate": "2023-10-05",
                    "updateDate": "2023-10-10",
                },
            ]

        @st.fragment
        def carousel_with_autoslide(project):
            # Display carousel content
            with st.container(border=True):
                slides = [{"image": img} for img in project["images"]]
                description = project["projectDescription"]
                publish_date = project["publishDate"]
                last_updated = project["updateDate"]

                # Initialize session state for carousel index
                carousel_key = f"carousel_index_{project['projectId']}"
                if carousel_key not in st.session_state:
                    st.session_state[carousel_key] = 0
                    st.session_state[f"last_update_time_{project['projectId']}"]
                # Header Title
                st.subheader(project["projectTitle"])

                # Image container
                image_container = st.empty()

                # Navigation buttons for the carousel
                col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")
                with col1:
                    if st.button(
                        label="",
                        key=f"prev_button_{project['projectId']}",
                        icon=":material/arrow_back_ios:",
                    ):
                        st.session_state.carousel_index = (
                            st.session_state.carousel_index - 1
                        ) % len(slides)
                with col2:
                    st.markdown(
                        f"<div style='text-align: center;'>{st.session_state.carousel_index + 1}/{len(slides)}</div>",
                        unsafe_allow_html=True,
                    )

                with col3:
                    if st.button(
                        label="",
                        key=f"next_button_{project['projectId']}",
                        icon=":material/arrow_forward_ios:",
                    ):
                        st.session_state.carousel_index = (
                            st.session_state.carousel_index + 1
                        ) % len(slides)

                # Get the current slide based on the index
                current_slide = slides[st.session_state[carousel_key]]
                image_container.image(current_slide["image"], use_container_width=True)

                # Description and dates
                st.write(description)
                # Two columns with buttons to direct to another page
                pbldate, lupdte = st.columns(2, vertical_alignment="bottom")
                with pbldate:
                    st.write(
                        f"Published: <span style='font-weight: bold;'>{publish_date}</span>",
                        unsafe_allow_html=True,
                    )

                with lupdte:
                    st.write(
                        f"Last Updated: <span style='font-weight: bold;'>{last_updated}</span>",
                        unsafe_allow_html=True,
                    )

                detailcol, ratecol, vwrtcol = st.columns(
                    [3, 2, 1], vertical_alignment="center"
                )
                with detailcol:
                    if st.button(
                        label="More Details",
                        key=f"details_{project['projectId']}",
                        type="primary",
                        icon=":material/call_made:",
                    ):
                        st.write("Redirecting to more details page...")
                        # Add navigation logic here
                with ratecol:
                    # Button to rate the project
                    if st.button(
                        label="Rate this Project",
                        icon=":material/star:",
                        key=f"rate_{project['projectId']}",
                    ):
                        st.write("Thank you for rating this project!")
                with vwrtcol:
                    # Display stars
                    stars = "⭐"
                    # st.write(stars, f"{project['projectId']}.9/5 (200)")
                    st.write(stars, "4.9/5 (200)")
                # Auto-slide functionality
            # current_time = time.time()
            if (
                # current_time
                -st.session_state[f"last_update_time_{project['projectId']}"]
                > 5
            ):
                st.session_state[carousel_key] = (
                    st.session_state[carousel_key] + 1
                ) % len(slides)
                st.session_state[f"last_update_time_{project['projectId']}"] = (
                    # current_time
                )
                st.rerun()

        # generate & Display projects cards in columns
        project_cards = get_project_cards()
        cols = st.columns(3)  
        for i, project in enumerate(project_cards):
            with cols[i % 3]:  # Cycle through columns for each project
                carousel_with_autoslide(project)

    elif tabs == "Skills":
        strml()


if __name__ == "__main__":
    main()
