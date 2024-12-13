import time
import streamlit as st


@st.fragment()
def strml():
    @st.cache_data
    def load_slides():
        return [
            {"image": "static/project_images/prjct1img1.jpg"},
            {"image": "static/project_images/prjct1img2.png"},
            # Add more slides here
        ]

    # Common slide details
    description = "Description for Slide"
    publish_date = "Published: 2023-12-10"
    last_updated = "Last Updated: 2023-12-12"
    stars = "⭐⭐⭐⭐⭐"

    def carousel_with_autoslide():
        # Load slides
        slides = load_slides()
        # Initialize session state for carousel index
        if "carousel_index" not in st.session_state:
            st.session_state.carousel_index = 0

        # Header Title
        st.subheader("Skills")

        # Image container
        image_container = st.empty()

        # Navigation buttons for the carousel
        col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")
        with col1:
            if st.button("⬅️", key="prev_button"):
                st.session_state.carousel_index = (
                    st.session_state.carousel_index - 1
                ) % len(slides)
        with col2:
            st.write(f"{st.session_state.carousel_index + 1}/{len(slides)}")
        with col3:
            if st.button("➡️", key="next_button"):
                st.session_state.carousel_index = (
                    st.session_state.carousel_index + 1
                ) % len(slides)

        # Auto-slide every 2 seconds
        time.sleep(2)
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(
            slides
        )

        # Get the current slide based on the index
        current_slide = slides[st.session_state.carousel_index]

        # Display carousel content
        with st.container():
            image_container.image(current_slide["image"], use_container_width=True)

            # Description and dates
            st.write(description)
            st.write(publish_date)
            st.write(last_updated)

            # Display stars
            st.write(stars)

            # Two columns with buttons to direct to another page
            col1, col2 = st.columns(2)
            with col1:
                if st.button("More Details"):
                    st.write("Redirecting to more details page...")
                    # Add navigation logic here
            with col2:
                # Button to rate the project
                if st.button("Rate this Project"):
                    st.write("Thank you for rating this project!")

    # Call the function
    carousel_with_autoslide()
