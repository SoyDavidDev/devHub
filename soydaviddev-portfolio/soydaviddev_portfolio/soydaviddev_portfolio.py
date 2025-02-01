"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from soydaviddev_portfolio.styles.styles import Size as Size
from soydaviddev_portfolio.components.navbar import navbar_searchbar
from soydaviddev_portfolio.components.footer import footer
from soydaviddev_portfolio.views.header.header import header
class State(rx.State):
    """The app state."""
    appearence: str = "dark"
    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar_searchbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Bienvenid@s a mi Portfolio!", size=Size.VERY_BIG2.value),
            header(),
            # rx.text(
            #     "Get started by editing ",
            #     rx.code(f"{config.app_name}/{config.app_name}.py"),
            #     size="5",
            # ),
            # rx.link(
            #     rx.button("Check out our docs!"),
            #     href="https://reflex.dev/docs/getting-started/introduction/",
            #     is_external=True,
            # ),
            spacing=Size.DEFAULT.value,
            justify="center",
            min_height="65vh",
        ),
        footer(),
        rx.logo(),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        radius="large",
)
)
app.add_page(
    index,
    title="David Sánchez | Software Engineer - Backend, Frontend & Fullstack Web Developer",
    description="Hola, soy David Sánchez, un Software Engineer especializado en Backend, APIs y Cloud. Trabajo con Python, Django, FastAPI, AWS (Certified) y más. 🚀",
    image="favicon.ico",
)
