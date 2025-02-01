import reflex as rx
from soydaviddev.styles.styles import Size
from soydaviddev.styles.colors import Color
from soydaviddev.styles.colors import TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            color=Color.PRIMARY.value,
        ),
        f"{body}",
        font_size=Size.SMALL.value,
        color=TextColor.BODY.value
    )