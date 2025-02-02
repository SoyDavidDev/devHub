import reflex as rx
import datetime
import soydaviddev_portfolio.constants as const
from soydaviddev_portfolio.styles.styles import MAX_WIDTH
from soydaviddev_portfolio.styles.styles import Size
from soydaviddev_portfolio.styles.styles import SizePx
from soydaviddev_portfolio.styles.styles import SizeWord
from soydaviddev_portfolio.styles.colors import Color
from soydaviddev_portfolio.components.link_icon import link_icon
from soydaviddev_portfolio.components.info_text import info_text

def header() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.avatar(
                src="avatar2.png",
                size=Size.VERY_BIG.value,
                radius=SizeWord.LARGE.value,
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "David Sánchez Valero 🧑‍💻",
                        size=Size.VERY_BIG.value,
                    ),
                    justify_content="center",
                    align="start",
                ),
                rx.text(
                    "Software Engineer - Backend, Frontend & Fullstack Web Developer",
                    size=Size.DEFAULT.value,
                    margin_top=SizePx.SMALL.value,
                ),
                rx.hstack(
                    rx.text.kbd(
                        f"🚀 {datetime.datetime.now().year} 🏄‍♂️ 🤙",
                        size=Size.MEDIUM.value,
                        align="right",
                    ),
                    rx.spacer(),
                    info_text(
                        f"+{experience()} ",
                        " años de formación",
                    ),
                    rx.spacer(),
                    info_text(
                        f"+{experience()-2} ",
                        " años de experiencia",
                    ),
                ),
                flex_direction="column",
                justify_content="start",
                align="start",
            ),
            margin_left=SizePx.SMALL.value,

        ),
        rx.flex(
            rx.hstack(
                link_icon("/icons/linkedin.svg", const.LINKEDIN_URL),
                link_icon("/icons/whatsapp.svg", const.WHATSAPP),
                link_icon("/icons/github.svg", const.GITHUB_URL),
                link_icon("/icons/id-card-solid.svg", const.CV),
                spacing=Size.MEDIUM.value,
                justify_content="start",
            ),
            flex_direction="column",
            margin=SizePx.MEDIUM.value,
            max_width=MAX_WIDTH,
        ),
        rx.flex(
            rx.accordion.root(
                rx.accordion.item(
                    content=[
                        rx.text(
                            "Soy Ingeniero de Software y Desarrollador Fullstack, porque, claro, "
                            "¿quién no querría ser experto tanto en backend (Python/Django) como en "
                            "frontend (Vue.js y Nuxt.js)? ",                    
                            as_="p"
                        ),
                        rx.spacer(),
                        rx.text(
                            "Me encanta resolver problemas complejos "
                            "creando APIs RESTful y, si se puede, añadir un poco de magia con IA y "
                            "Machine Learning, usando herramientas como scikit-learn. También soy "
                            "AWS Certified Cloud Practitioner (sí, me tomé el tiempo para aprender "
                            "todo sobre la nube, ¡y sí, planeo seguir coleccionando más certificaciones"
                            " porque, bueno, no se va a hacer solo!) ",                 
                            as_="p"
                        ),
                        rx.spacer(),
                        rx.text(
                            " Me aseguro de que todo el código "
                            "sea limpio y bien organizado, aplicando metodologías ágiles como Scrum "
                            "para que el proceso sea lo más eficiente posible, sin perder la calidad. "
                            "Porque, a fin de cuentas, ¿quién tiene tiempo para hacer las cosas mal?",                                      
                            as_="p"
                        ),
                    ],
                    header="Sobre mí (porque obvio, quieres saber más)",
                ),
                collapsible=True,
                variant="outline",
            ),
            direction="row",
            spacing="2",
        ),
        flex_direction="column",
        margin_top=SizePx.VERY_BIG.value,
    )

def experience()-> int:
    return datetime.datetime.now().year - 2022