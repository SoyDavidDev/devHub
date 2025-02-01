import reflex as rx
import datetime

from soydaviddev.components.link_icon import link_icon
from soydaviddev.components.info_text import info_text
from soydaviddev.components.dark_model_toggle import dark_mode_toggle
from soydaviddev.styles.styles import Size
from soydaviddev.styles.colors import Color
from soydaviddev.styles.colors import TextColor
import soydaviddev.constants as const

def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar2.png", 
                size="8", 
                radius="full",
                color=TextColor.BODY.value,
                background_color=Color.CONTENT.value,
                padding="2px",
                border="0.1em solid",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                dark_mode_toggle(),
                rx.heading(
                    "David Sánchez Valero", 
                    size="7",
                    align="center",
                ),
                rx.button(
                    rx.text(
                        "@SoyDavidDev",
                        margin_top=Size.ZERO.value,
                        color = TextColor.BODY.value
                    ),
                ),
                rx.hstack(
                    rx.button(
                        link_icon("icons/linkedin.svg",const.LINKEDIN_URL),
                        link_icon("icons/whatsapp.svg",const.WHATSAPP),
                        link_icon("icons/github.svg",const.GITHUB_URL),
                        link_icon("icons/id-card-solid.svg",const.CV),
                    )
                ),
                align_items= "center",
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de formación"
            ),            
            rx.spacer(),
            info_text(
                f"{experience()-2}+",
                "años de experiencia",
            ), 
            width="100%",
            align_items="center",
            justify_content="center",
            spacing=Size.DEFAULT.value      
        ),
        rx.text("""Software Engineer con experiencia en desarrollo backend, frontend
                y fullstack.""",
            font_size=Size.DEFAULT.value,
            text_align = "center",
        ),
        rx.text("""Actualmente, formo parte de Capgemini, donde colaboro en 
                proyectos de software innovadores, integrando IA, AWS y buenas 
                prácticas de Clean Code.""",
            font_size=Size.DEFAULT.value,
            text_align = "center",
        ),
        rx.text("""Python | Django | FastAPI | Vue.js | AWS (Certified) 
                | PostgreSQL | MySQL | MongoDB | DynamoDB | Redis | Docker 
                | Git & GitHub """,
            font_size=Size.DEFAULT.value,
            text_align = "center",
        ),
        rx.text("""¡Bienvenid@!""",
            font_size=Size.DEFAULT.value,
            text_align = "center",
        ),
        spacing = Size.DEFAULT.value,
        align_items= "center",
        width = "100%",
        padding = "1em",
    )

def experience()->int:
    return datetime.datetime.now().year - 2022