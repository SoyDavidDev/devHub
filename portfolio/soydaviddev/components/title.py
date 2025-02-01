import reflex as rx
import soydaviddev.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.text(text, style=styles.title_style)