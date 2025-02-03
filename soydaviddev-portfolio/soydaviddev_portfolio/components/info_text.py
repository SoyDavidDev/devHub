import reflex as rx
from soydaviddev_portfolio.styles.styles import Size
from soydaviddev_portfolio.styles.styles import SizePx
from soydaviddev_portfolio.styles.colors import Color

def info_text(title: str, body: str)-> rx.Component:
    return rx.flex(
        rx.text.kbd(
            title + " ",
            color=Color.PRIMARY.value,
        ),
        f"{body} ",
        font_size=SizePx.SMALL.value,
        spacing=Size.SMALL.value,
    ),

