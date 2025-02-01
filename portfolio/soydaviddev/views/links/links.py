import reflex as rx
from soydaviddev.components.link_button import link_button
from soydaviddev.components.title import title
from soydaviddev.styles.styles import Size as Size
from soydaviddev import constants


def links() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                title("Mis enlaces"),
                rx.flex(
                    link_button(
                        "Red de contactos profesional.",
                        "icons/linkedin.svg",
                        constants.LINKEDIN_URL
                    ),
                    link_button(
                        "El código importa y se comparte.",
                        "icons/github.svg",
                        constants.GITHUB_URL
                    ),
                        link_button(
                        "Revisa mi experiencia profesional y académica.",
                        "icons/id-card-solid.svg",
                        constants.CV
                    ),
                spacing=Size.VERY_BIG2.value,
                ),
                title("Proyectos"),
                rx.flex(
                    link_button(
                        "Python Web con Reflex. Mi Web de links.",
                        "icons/reflex.svg",
                        constants.WEB_LINKS
                    ),
                    rx.vstack(
                        link_button(
                            "Tudú App (Backend). Django, DRF, PostgreSQL.",
                            "icons/django.svg",
                            constants.TUDU_APP_BACKEND
                        ),
                        link_button(
                            "Tudú App (Frontend). VueJS, NuxtJS.",
                            "icons/vuejs.svg",
                            constants.TUDU_APP_FRONTEND
                        ),
                        spacing=Size.VERY_BIG2.value,
                    ),
                    link_button(
                        "Web Live4Live. Fullstack, Django y Vue.js.",
                        "icons/django.svg",
                        constants.LIVE_4_LIFE
                    ),
                    link_button(
                        "Traductor App con IA. Whisper.",
                        "icons/openai.svg",
                        constants.WHISPER_APP
                    ),
                    spacing=Size.VERY_BIG2.value,

                ),
                title("Contacto"),
                rx.flex(
                    link_button(
                        "Escríbeme!",
                        "icons/envelope-solid.svg",
                        f"mailto:{constants.EMAIL}"
                    ),
                    link_button(
                        "'Hello world!', no dudes en contactarme!",
                        "icons/whatsapp.svg",
                        constants.WHATSAPP,
                    ),
                    spacing=Size.VERY_BIG2.value,

                ),
                spacing = Size.VERY_BIG2.value,
                align_items = "center", 
                width = "100%"
            ),
            spacing = Size.VERY_BIG2.value,
            align_items = "center", 
            width = "100%",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                title("Mis enlaces"),
                rx.flex(
                    link_button(
                        "Red de contactos profesional.",
                        "icons/linkedin.svg",
                        constants.LINKEDIN_URL
                    ),
                    link_button(
                        "El código importa y se comparte.",
                        "icons/github.svg",
                        constants.GITHUB_URL
                    ),
                        link_button(
                        "Revisa mi experiencia profesional y académica.",
                        "icons/id-card-solid.svg",
                        constants.CV
                    ),
                    spacing=Size.VERY_BIG2.value,
                    flex_direction = "column",
                ),
                title("Proyectos"),
                rx.flex(
                    rx.vstack(
                        link_button(
                            "Python Web con Reflex. Mi Web de links.",
                            "icons/reflex.svg",
                            constants.WEB_LINKS
                        ),
                        rx.vstack(
                            link_button(
                                "Tudú App (Backend). Django, DRF, PostgreSQL.",
                                "icons/django.svg",
                                constants.TUDU_APP_BACKEND
                            ),
                            link_button(
                                "Tudú App (Frontend). VueJS, NuxtJS.",
                                "icons/vuejs.svg",
                                constants.TUDU_APP_FRONTEND
                            ),
                            spacing=Size.VERY_BIG2.value,
                        ),
                        link_button(
                            "Web Live4Live. Fullstack, Django y Vue.js.",
                            "icons/django.svg",
                            constants.LIVE_4_LIFE
                        ),
                        link_button(
                            "Traductor App con IA. Whisper.",
                            "icons/openai.svg",
                            constants.WHISPER_APP
                        ),
                        spacing=Size.VERY_BIG2.value,
                    ),
                    spacing=Size.VERY_BIG2.value,
                    flex_direction = "column",
                ),
                
                title("Contacto"),
                rx.flex(
                    link_button(
                        "Escríbeme!",
                        "icons/envelope-solid.svg",
                        f"mailto:{constants.EMAIL}"
                    ),
                    link_button(
                        "'Hello world!', no dudes en contactarme!",
                        "icons/whatsapp.svg",
                        constants.WHATSAPP,
                    ),
                    spacing = Size.VERY_BIG2.value,
                    flex_direction = "column",
                ),
                spacing = Size.VERY_BIG2.value,
                align_items = "center", 
                height = "100%",
            ),
        ),
        width = "100%",
        align_items = "center",
    )
