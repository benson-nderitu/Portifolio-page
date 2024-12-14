import os
import time
import pathlib
import pages as pg
import streamlit as st
import streamlit_antd_components as sac
from pathlib import Path

from portifolio import show_home

# from about import show_about
from skills import strml

st.set_page_config(
    page_title="Benson Nderitu",
    page_icon=":material/bar_chart:",
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
        padding: 1.8rem 1rem 10rem;
        min-width: auto;
        max-width: initial;
        }
            """,
    unsafe_allow_html=True,
)
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
# resume_file = current_dir / "static" / "CV.pdf"


# --- LOAD CSS, PDF  ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()

# -------------------Load the external CSS file ------------------
# def load_css(file_path):
#     with open(file_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# css_path = pathlib.Path("styles/style.css")
# load_css(css_path)


# ================================================================
@st.fragment()
def main():
    tabs = sac.tabs(
        [
            sac.TabsItem(label="About Me", icon="person-circle"),
            sac.TabsItem(label="Portfolio", icon="laptop"),
            sac.TabsItem(label="Skills", icon="rocket"),
        ],
        align="center",
        size="lg",
        variant="outline",
    )

    if tabs == "About Me":
        # --- HERO SECTION ---
        with st.container(key="heroContainer"):
            NAME = "John Doe"
            DESCRIPTION = """
            Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
            """
            col1, col2 = st.columns(2, gap="small")
            with col1:
                with st.container(key="CTAContainer"):
                    st.title(NAME)
                    st.write(DESCRIPTION)
                    st.write("Here's my resume:")
                    viewcol, downloadcol = st.columns(2)
                    with viewcol:
                        if st.button(
                            label="Read Resume",
                            icon=":material/open_in_new:",
                            type="primary",
                        ):
                            st.write("View Resume")
                    with downloadcol:
                        if st.button(
                            label="Download Resume",
                            icon=":material/download:",
                            key="download_resume",
                            type="primary",
                        ):
                            st.write("Downloading...")
                    # st.download_button(
                    #     label=" 📄 Download Resume",
                    #     data=PDFbyte,
                    #     file_name=resume_file.name,
                    #     mime="application/octet-stream",
                    # )

            with col2:
                with st.container(key="profileImageContainer"):
                    st.image("static/profile.png", use_container_width=True)
        with st.container(border=True):
            st.write("About me")
    elif tabs == "Portfolio":

        @st.cache_data()
        def get_project_cards():
            return [
                {
                    "projectId": 1,
                    "projectTitle": "Ultimate Personal Budgeting",
                    "images": [
                        "static/images/1.png",
                        "static/images/2.png",
                        "static/images/3.png",
                    ],
                    "projectDescription": "This is the description for Project One.",
                    "publishDate": "2023-12-10",
                    "updateDate": "2023-12-12",
                },
                {
                    "projectId": 2,
                    "projectTitle": "Project Two",
                    "images": [
                        "static/images/1.png",
                        "static/images/2.png",
                        "static/images/3.png",
                    ],
                    "projectDescription": "This is the description for Project Two.",
                    "publishDate": "2023-11-20",
                    "updateDate": "2023-11-25",
                },
                {
                    "projectId": 3,
                    "projectTitle": "Project Three",
                    "images": [
                        "static/images/1.png",
                        "static/images/2.png",
                        "static/images/3.png",
                    ],
                    "projectDescription": "This is the description for Project Three.",
                    "publishDate": "2023-10-05",
                    "updateDate": "2023-10-10",
                },
                {
                    "projectId": 4,
                    "projectTitle": "Project Four",
                    "images": [
                        # "static/images/6.png",
                        "static/images/6.svg",
                        "static/images/7.svg",
                    ],
                    "projectDescription": "This is the description for Project Four.",
                    "publishDate": "2023-10-05",
                    "updateDate": "2023-10-10",
                },
                {
                    "projectId": 5,
                    "projectTitle": "Project Five",
                    "images": [
                        "static/images/1.png",
                        "static/images/2.png",
                        "static/images/3.png",
                    ],
                    "projectDescription": "This is the description for Project Five.",
                    "publishDate": "2023-10-05",
                    "updateDate": "2023-10-10",
                },
                {
                    "projectId": 6,
                    "projectTitle": "Project Six",
                    "images": [
                        "static/images/1.png",
                        "static/images/2.png",
                        "static/images/3.png",
                    ],
                    "projectDescription": "This is the description for Project Six.",
                    "publishDate": "2023-10-05",
                    "updateDate": "2023-10-10",
                },
            ]

        @st.fragment
        def carousel_with_autoslide(project):
            with st.container(border=True):
                slides = [{"image": img} for img in project["images"]]
                description = project["projectDescription"]
                publish_date = project["publishDate"]
                last_updated = project["updateDate"]

                # Initialize session state for carousel index
                carousel_key = f"carousel_index_{project['projectId']}"
                if carousel_key not in st.session_state:
                    st.session_state[carousel_key] = 0

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
                        # Navigate to the previous slide
                        st.session_state[carousel_key] = (
                            st.session_state[carousel_key] - 1
                        ) % len(slides)
                with col2:
                    # Display current slide number
                    st.markdown(
                        f"<div style='text-align: center;'>{st.session_state[carousel_key] + 1}/{len(slides)}</div>",
                        unsafe_allow_html=True,
                    )
                with col3:
                    if st.button(
                        label="",
                        key=f"next_button_{project['projectId']}",
                        icon=":material/arrow_forward_ios:",
                    ):
                        # Navigate to the next slide
                        st.session_state[carousel_key] = (
                            st.session_state[carousel_key] + 1
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
                    [2, 1.5, 1.5], vertical_alignment="center"
                )
                with detailcol:
                    if st.button(
                        label="Read More",
                        key=f"details_{project['projectId']}",
                        type="primary",
                        icon=":material/call_made:",
                    ):
                        st.write("Redirecting to more details page...")
                with ratecol:
                    if st.button(
                        label="Rate",
                        icon=":material/thumb_up_alt:",
                        key=f"rate_{project['projectId']}",
                    ):
                        st.write("Thank you for rating this project!")
                with vwrtcol:
                    stars = "⭐"
                    st.write(stars, "4.9/5 (200)")

        # Generate & Display projects cards in columns
        project_cards = get_project_cards()
        cols = st.columns(3)
        for i, project in enumerate(project_cards):
            with cols[i % 3]:  # Cycle through columns for each project
                carousel_with_autoslide(project)

        # @st.fragment()
        # def carousel_with_autoslide(project):
        #     # Display carousel content
        #     with st.container(border=True):
        #         slides = [{"image": img} for img in project["images"]]
        #         description = project["projectDescription"]
        #         publish_date = project["publishDate"]
        #         last_updated = project["updateDate"]

        #         # Initialize session state for carousel index
        #         carousel_key = f"carousel_index_{project['projectId']}"
        #         if carousel_key not in st.session_state:
        #             st.session_state[carousel_key] = 0
        #             st.session_state[f"last_update_time_{project['projectId']}"]
        #         # Header Title
        #         st.subheader(project["projectTitle"])

        #         # Image container
        #         image_container = st.empty()

        #         # Navigation buttons for the carousel
        #         col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")
        #         with col1:
        #             if st.button(
        #                 label="",
        #                 key=f"prev_button_{project['projectId']}",
        #                 icon=":material/arrow_back_ios:",
        #             ):
        #                 st.session_state.carousel_index = (
        #                     st.session_state.carousel_index - 1
        #                 ) % len(slides)
        #         with col2:
        #             st.markdown(
        #                 f"<div style='text-align: center;'>{st.session_state.carousel_index + 1}/{len(slides)}</div>",
        #                 unsafe_allow_html=True,
        #             )

        #         with col3:
        #             if st.button(
        #                 label="",
        #                 key=f"next_button_{project['projectId']}",
        #                 icon=":material/arrow_forward_ios:",
        #             ):
        #                 st.session_state.carousel_index = (
        #                     st.session_state.carousel_index + 1
        #                 ) % len(slides)

        #         # Get the current slide based on the index
        #         current_slide = slides[st.session_state[carousel_key]]
        #         image_container.image(current_slide["image"], use_container_width=True)

        #         # Description and dates
        #         st.write(description)
        #         # Two columns with buttons to direct to another page
        #         pbldate, lupdte = st.columns(2, vertical_alignment="bottom")
        #         with pbldate:
        #             st.write(
        #                 f"Published: <span style='font-weight: bold;'>{publish_date}</span>",
        #                 unsafe_allow_html=True,
        #             )

        #         with lupdte:
        #             st.write(
        #                 f"Last Updated: <span style='font-weight: bold;'>{last_updated}</span>",
        #                 unsafe_allow_html=True,
        #             )

        #         detailcol, ratecol, vwrtcol = st.columns(
        #             [3, 2, 1], vertical_alignment="center"
        #         )
        #         with detailcol:
        #             if st.button(
        #                 label="More Details",
        #                 key=f"details_{project['projectId']}",
        #                 type="primary",
        #                 icon=":material/call_made:",
        #             ):
        #                 st.write("Redirecting to more details page...")
        #                 # Add navigation logic here
        #         with ratecol:
        #             # Button to rate the project
        #             if st.button(
        #                 label="Rate this Project",
        #                 icon=":material/star:",
        #                 key=f"rate_{project['projectId']}",
        #             ):
        #                 st.write("Thank you for rating this project!")
        #         with vwrtcol:
        #             # Display stars
        #             stars = "⭐"
        #             # st.write(stars, f"{project['projectId']}.9/5 (200)")
        #             st.write(stars, "4.9/5 (200)")
        #         # Auto-slide functionality
        #     # current_time = time.time()
        #     if (
        #         # current_time
        #         -st.session_state[f"last_update_time_{project['projectId']}"]
        #         > 5
        #     ):
        #         st.session_state[carousel_key] = (
        #             st.session_state[carousel_key] + 1
        #         ) % len(slides)
        #         st.session_state[f"last_update_time_{project['projectId']}"] = (
        #             # current_time
        #         )
        #         st.rerun()

        # # generate & Display projects cards in columns
        # project_cards = get_project_cards()
        # cols = st.columns(3)
        # for i, project in enumerate(project_cards):
        #     with cols[i % 3]:  # Cycle through columns for each project
        #         carousel_with_autoslide(project)

    elif tabs == "Skills":
        strml()


if __name__ == "__main__":
    main()
