import reflex as rx
from soydaviddev.styles.styles import Size as Size

def link_langs(icon:str) -> rx.Component:
    return rx.image(
        src=icon,
        height="60px",
    )