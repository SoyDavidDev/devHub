import reflex as rx
import soydaviddev.styles.styles as styles
from soydaviddev.styles.styles import Size as Size
from soydaviddev.styles.colors import Color as Color

def link_button(body: str, image: str, url: str)-> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.link(
                rx.button( 
                    rx.hstack(
                        rx.image(   
                            src=image,
                            width="40px",
                            height="40px",
                        ),
                        rx.vstack(
                            rx.text(body, style=styles.button_body_style),
                            align_items="center",
                            spacing=Size.LARGE.value,
                        ),
                        align_items="center",
                    ),
                    padding_y=Size.LARGE.value,
                    padding_x=Size.LARGE.value,
                    height="100px",
                    width="200px",
                ),
                href=url,
                is_external=True,
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.link(
                rx.button( 
                    rx.hstack(
                        rx.image(
                            src=image,
                            width="40px",
                            height="40px"
                        ),
                        rx.vstack(
                            rx.text(body, style=styles.button_body_style),
                            spacing=Size.LARGE.value,
                            align_items="center",
                        ),
                        align_items="center",
                    ),
                    padding_y=Size.VERY_BIG2.value,
                    padding_x=Size.VERY_BIG2.value,
                    height="100%",
                    width="350px",
                    align_items="center",
                    spacing=Size.LARGE.value,
                ),
                href=url,
                is_external=True,
                width="100%",
                align_items="center",
            ),
        ),
    )