import reflex as rx
from soydaviddev_portfolio.styles.styles import Size
from soydaviddev_portfolio.styles.styles import SizePx


def link_icon(icon: str, href: str, is_external: bool = True) -> rx.Component:
    return rx.button(
        rx.link(
            rx.image(
                src=icon,
                width=SizePx.MEDIUM.value,
            ),
            href=href,
            is_external=is_external,
        ),
        variant="classic",
        size=Size.SMALL.value,
    )