import reflex as rx
from soydaviddev.styles.colors import Color as Color
from soydaviddev.styles.colors import TextColor as TextColor
from soydaviddev.styles.styles import Size as Size

def navbar_searchbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.box(
                        rx.heading(
                            "soyDavid", size="7", weight="bold",
                            color=Color.PRIMARY.value,
                        ),
                    ),
                    rx.heading(
                        "Dev", size="7", weight="bold",margin_right="5em",
                        color=Color.SECONDARY.value,
                    ),
                    align_items="center",
                ),
                justify="between",
                align_items="center",
                position="sticky",
                padding_y=Size.DEFAULT.value,
                padding_x=Size.BIG.value,
                z_index="999",
                top="0",
            ),
        ),
        rx.mobile_and_tablet(
            rx.center(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="6em",
                        height="auto",
                        border_radius="25%",
                    ),
                    align_items="center",
                ),
                justify="center",
                align_items="center",
            ),
        ),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )