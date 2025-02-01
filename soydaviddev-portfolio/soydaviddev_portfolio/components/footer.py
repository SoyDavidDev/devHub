import reflex as rx
import datetime
import soydaviddev_portfolio.constants as const

from soydaviddev_portfolio.styles.styles import Size as Size
from soydaviddev_portfolio.styles.styles import SizePx as SizePx
from soydaviddev_portfolio.styles.colors import Color as Color
from soydaviddev_portfolio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.flex(
        rx.divider(),
        rx.hstack(
            rx.text(
                "Creando SOFTWARE con ♥ FROM VALENCIA. by SoyDavidDev",
                font_size = Size.MEDIUM.value,
                size=Size.MEDIUM.value,
                white_space="nowrap",
                weight="medium",
            ),
            justify_content="center",
            width="100%",
            spacing=Size.DEFAULT.value,
            margin_top=SizePx.MEDIUM.value,
        ),
        rx.hstack(
            rx.link(
                rx.box(
                    f"© 2022-{datetime.date.today().year} ",
                            color = Color.PRIMARY.value),
                is_external=True,
                font_size = SizePx.SMALL.value,
                href=const.LINKEDIN_URL,
            ),
            justify_content="center",
            margin_top=SizePx.SMALL.value,
        ),
        flex_direction="column",
        width="100%",
    )