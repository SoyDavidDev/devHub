import reflex as rx
from soydaviddev.styles.styles import Size as Size

def link_icon(image:str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            height=Size.LARGE.value
        ),
        href=url,
        is_external=True
    )