import reflex as rx
import datetime
import soydaviddev.constants as const
from soydaviddev.styles.styles import Size as Size
from soydaviddev.styles.colors import Color as Color
from soydaviddev.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.flex(
        rx.image(
            src="favicon.png",
            height = "auto",
            width = "150px",
            border_radius="25%",
        ),
        rx.link(
            rx.box(
                f"© 2022-{datetime.date.today().year} ",
                        color = Color.PRIMARY.value),
            is_external=True,
            font_size = Size.MEDIUM.value,
            align_items = "center",
        ),
        rx.text("Creando SOFTWARE con ♥ FROM VALENCIA. by SoyDavidDev",
            font_size = Size.MEDIUM.value,
            margin_top= Size.ZERO.value,
            href=const.LINKEDIN_URL,
        ),
        margin_top="100px",
        margin_bottom="30px",
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
        flex_direction = "column",
        align_items = "center",

    )