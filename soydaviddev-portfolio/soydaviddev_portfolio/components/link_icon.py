import reflex as rx
from soydaviddev_portfolio.styles.styles import Size


def link_icon(icon: str, href: str, is_external: bool = True) -> rx.Component:
    return rx.link(
        rx.image(
            src=icon,
            size=Size.BIG.value,
        ),
        href=href,
        is_external=is_external,
        size=Size.BIG.value,
    )