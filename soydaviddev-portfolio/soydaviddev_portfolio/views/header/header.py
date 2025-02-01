import reflex as rx
import datetime
import soydaviddev_portfolio.constants as const
from soydaviddev_portfolio.styles.styles import Size
from soydaviddev_portfolio.styles.styles import SizePx
from soydaviddev_portfolio.styles.styles import SizeWord
from soydaviddev_portfolio.styles.colors import Color
from soydaviddev_portfolio.components.link_icon import link_icon


def header() -> rx.Component:
    return rx.flex(
        rx.avatar(
            src="/assets/avatar2.png",
            size=Size.VERY_BIG.value,
            radius=SizeWord.LARGE.value,
            border_color=Color.PRIMARY.value,
        ),
        rx.flex(
            rx.vstack(
                rx.heading(
                    "David Sánchez Valero",
                    size=Size.BIG.value,
                ),
                margin_top=Size.DEFAULT.value,
                justify_content="center",
                align="start",
            ),
            rx.vstack(
                rx.text(
                    "Software Engineer - Backend, Frontend & Fullstack Web Developer",
                    size=Size.DEFAULT.value,
                ),
                rx.text(
                    f"🚀 {datetime.datetime.now().year}",
                    size=Size.DEFAULT.value,
                ),
                flex_direction="row",
                justify_content="start",
                align="start",
            ),
            rx.vstack(
                link_icon("/assets/icons/linkedin.svg", const.LINKEDIN_URL),
                link_icon("/assets/icons/whatsapp.svg", const.WHATSAPP),
                link_icon("/assets/icons/github.svg", const.GITHUB_URL),
                link_icon("/assets/icons/id-card-solid.svg", const.CV),
                flex_direction="row",
                spacing=Size.VERY_BIG2.value,
                justify_content="center",
                margin=SizePx.MEDIUM.value,
            ),
            rx.vstack(
                rx.text(
                    "Soy Ingeniero de Software y Desarrollador Fullstack, porque, claro, "
                    "¿quién no querría ser experto tanto en backend (Python/Django) como en "
                    "frontend (Vue.js y Nuxt.js)? ",                    
                    as_="p"
                ),
                rx.text(
                    "Me encanta resolver problemas complejos "
                    "creando APIs RESTful y, si se puede, añadir un poco de magia con IA y "
                    "Machine Learning, usando herramientas como scikit-learn. También soy "
                    "AWS Certified Cloud Practitioner (sí, me tomé el tiempo para aprender "
                    "todo sobre la nube, ¡y sí, planeo seguir coleccionando más certificaciones"
                    " porque, bueno, no se va a hacer solo.!) ",                 
                    as_="p"
                ),
                rx.text(
                    " Me aseguro de que todo el código "
                    "sea limpio y bien organizado, aplicando metodologías ágiles como Scrum "
                    "para que el proceso sea lo más eficiente posible, sin perder la calidad. "
                    "Porque, a fin de cuentas, ¿quién tiene tiempo para hacer las cosas mal?",                                      
                    as_="p"
                ),
            ),
            flex_direction="column",
            margin=SizePx.MEDIUM.value,
            justify_content="center",
        ),
        margin_top=SizePx.VERY_BIG  .value,
    ),