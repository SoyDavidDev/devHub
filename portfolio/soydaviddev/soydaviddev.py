"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from soydaviddev.components.navbar import navbar_searchbar
from soydaviddev.components.footer import footer
from soydaviddev.views.header.header import header
from soydaviddev.views.links.links import links
from soydaviddev.styles.styles import Size as Size
from soydaviddev.styles import styles

class State(rx.State):
    """The app state."""
    color_mode: str = "dark"


def index() -> rx.Component:
    return rx.fragment(
        navbar_searchbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value,
                padding = Size.BIG.value               
            ),
        ),
        footer()
    )

app = rx.App( 
    theme=rx.theme( 
        appearance="dark", 
        has_background=True, 
        radius="large",
        accent_color="blue",
    )
)
app.add_page(
    index,
    title="David Sánchez | Software Engineer - Backend, Frontend & Fullstack Web Developer",
    description="Hola, soy David Sánchez, un Software Engineer especializado en Backend, APIs y Cloud. Trabajo con Python, Django, FastAPI, AWS y más. 🚀",
    image="favicon.ico",
)
app._compile()