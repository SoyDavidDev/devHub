import reflex as rx
import soydaviddev_portfolio.constants as const
from soydaviddev_portfolio.styles.styles import MAX_WIDTH
from soydaviddev_portfolio.components.link_card import link_card


def links() -> rx.Component:
    return(rx.vstack(
        rx.flex(
            rx.accordion.root(
                rx.accordion.item(
                    content=[
                        rx.vstack(
                            link_card(
                                "Red de contactos profesional.",
                                "Conecta conmigo en LinkedIn.",
                                "/icons/dark/linkedin.svg",
                                const.LINKEDIN_URL,
                            ),
                            link_card(
                                "Explora mi GitHub.",
                                "El código importa y se comparte (excepto contraseñas).",
                                "/icons/dark/github.svg",
                                const.GITHUB_URL,
                            ),
                            link_card(
                                "Mi CV en PDF.",
                                "Descarga mi CV en PDF.",
                                "icons/dark/id-card-solid.svg",
                                const.CV,
                            ),
                        align="center",
                        justify_content= "center",
                        ),
                    ],
                    header="Mis links, porque mandar un fax ya no se usa",
                    justify_content= "center",
                    align="center",
                ),
                rx.accordion.item(
                    content=[
                        rx.vstack(
                            link_card(
                                "Python + Reflex = Esta web.",
                                "Mira qué bonito quedó.",
                                "icons/reflex.svg",
                                const.WEB_LINKS,
                            ),
                            link_card(
                                "Tudú App (Backend). Django, DRF, PostgreSQL.",
                                "Porque las listas de tareas no se hacen solas",
                                "icons/django.svg",
                                const.TUDU_APP_BACKEND,
                            ),
                            link_card(
                                "Tudú App (Frontend). VueJS, NuxtJS.",
                                "Haciendo que el backend luzca bonito.",
                                "icons/vuejs.svg",
                                const.TUDU_APP_FRONTEND,
                            ),
                            link_card(
                                "Web Live4Live. Django y Vue.js.",
                                "Fullstack, porque backend o frontend sólo sería muy fácil",
                                "icons/django.svg",
                                const.LIVE_4_LIFE,
                            ),
                            link_card(
                                "Traductor App con IA. Whisper.",
                                "OpenAI y un poco de magia.",
                                "icons/openai.svg",
                                const.WHISPER_APP,
                            ),
                        align="center",
                        justify_content= "center",
                        ),
                    ],
                    header="Pruebas de que trabajo",
                ),
                rx.accordion.item(
                    content=[
                        rx.vstack(
                            link_card(
                                "Escríbeme!",
                                "¿Quieres contactar conmigo? ¡Hazlo!",
                                "icons/envelope-solid.svg",
                                f"mailto:{const.EMAIL}"
                            ),
                            link_card(
                                "Hello, World!",
                                "Whatsapeame, que es más rápido.",
                                "icons/whatsapp.svg",
                                const.WHATSAPP,
                            ),
                        align="center",
                        justify_content= "center",
                        ),
                    ],
                    header="Contáctame (o no, tú decides)",
                    justify_content= "center",
                    align="center",
                ),
                collapsible=True,
                variant="outline",
                justify_content= "center",
                align="center",
            ),
            direction="row",
            spacing="2",
            justify_content= "center",
            align="center",
            width=MAX_WIDTH,
        ),
    ),
    )