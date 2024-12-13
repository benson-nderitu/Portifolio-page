import streamlit as st
import streamlit.components.v1 as components
import base64


@st.fragment(run_every="5s")
def show_home():
    def get_base64_image(image_path):
        """Convert a local image file to a Base64 string."""
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def render_dynamic_carousel(images, title, text, timestamp):
        """
                Create a dynamic carousel component with given images and content.
        s
                Args:
                    images (list): List of image URLs or Base64-encoded image strings.
                    title (str): Title of the carousel content.
                    text (str): Body text of the card.
                    timestamp (str): Timestamp or footer text.
        """
        # Dynamically generate carousel items
        carousel_items = ""
        for i, img in enumerate(images):
            active_class = "active" if i == 0 else ""
            carousel_items += f"""
            <div class="carousel-item {active_class}" data-bs-interval="5000">
                <img src="{img}" class="d-block w-100 " style="min-height: 400px; max-height: 350px; overflow: auto;" alt="Slide {i+1}">
            </div>
            """

        component_html = f"""
        <div class="card w-100">
            <div class="card-img-top">
                <div id="dynamicCarousel" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        {carousel_items}
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#dynamicCarousel" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#dynamicCarousel" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
            <div class="card-body">
                <h4 class="card-title">{title}</h4>
                <p class="card-text">{text}</p>
                <small class="text-muted">{timestamp}</small>
            </div>
        </div>
        """

        # Embed the carousel in Streamlit
        components.html(
            f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    .card {{
                        margin: auto;
                    }}
                </style>
            </head>
            <body>
                {component_html}
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
            """,
            height=1000,
        )

    hy, ji, ki = st.columns(3)
    with hy:
        images = [
            "https://via.placeholder.com/1200x800?text=Image+1",
            "https://via.placeholder.com/1200x800?text=Image+2",
            "https://via.placeholder.com/1200x800?text=Image+3",
        ]
        render_dynamic_carousel(
            images=images,
            title="News 2",
            text="Different description here.",
            timestamp="2 hours ago",
        )
    with ji:
        images = [
            "https://img.freepik.com/free-vector/dark-background-luxury-design_677411-1722.jpg?t=st=1734004777~exp=1734008377~hmac=f36924484af2849ac0baf0d14fc30d1e9cd14865f732d9b2b0a64ef6f86155ff&w=826",
            "https://img.freepik.com/free-vector/abstract-black-luxury-background-with-abstracts_361591-4303.jpg?ga=GA1.1.657497177.1733867837&semt=ais_hybrid",
            "https://via.placeholder.com/1200x800?text=Image+3",
        ]
        render_dynamic_carousel(
            images=images,
            title="News 2",
            text="Different description here.",
            timestamp="2 hours ago",
        )
    with ki:
        # Define the content for each slide
        with st.container(border=True):
            slides = [
                {
                    "title": "Skills Slide 1",
                    "image": "static/project_images/prjct1img1.jpg",
                    "description": "Description for Slide 1",
                    "timestamp": "2 hours ago",
                },
                {
                    "title": "Skills Slide 2",
                    "image": "static/project_images/prjct1img2.png",
                    "description": "Description for Slide 2",
                    "timestamp": "1 day ago",
                },
                # Add more slides as needed
            ]

            # Initialize session state for carousel index
            if "carousel_index" not in st.session_state:
                st.session_state.carousel_index = 0

            # Navigation buttons
            col1, col2, col3 = st.columns([1, 6, 1])
            with col1:
                if st.button("⬅️", key="prev_button"):
                    st.session_state.carousel_index = (
                        st.session_state.carousel_index - 1
                    ) % len(slides)
            with col3:
                if st.button("➡️", key="next_button"):
                    st.session_state.carousel_index = (
                        st.session_state.carousel_index + 1
                    ) % len(slides)

            # Get the current slide based on index
            current_slide = slides[st.session_state.carousel_index]

            # Display the current slide
            with st.container():
                st.subheader(current_slide["title"])
                st.image(current_slide["image"])
                st.write(current_slide["description"])
                st.write(current_slide["timestamp"])
