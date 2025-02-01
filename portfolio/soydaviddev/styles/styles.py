import reflex as rx
from enum import Enum

from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = '1'
    MEDIUM = '2'
    DEFAULT = '5'
    LARGE = '6'
    BIG = '7'
    VERY_BIG = '8'
    VERY_BIG2 = '9'

class FontSize(Enum):
    SMALL = "1em"
    MEDIUM = "1.5em"
    LARGE = "2em"
    BIG = "3em"
    VERY_BIG = "4em"

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100px",
        "display": "block",
        "padding": Size.LARGE.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

DARK_MODE_STYLE = {
    "background_color": Color.BACKGROUND_DARK.value,
    rx.heading: {
        "color": TextColor.HEADER_DARK.value,
    },
    rx.button: {
        "color": TextColor.HEADER_DARK.value,
        "background_color": Color.CONTENT_DARK.value,
        "_hover": {
            "background_color": Color.SECONDARY_DARK.value,
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}


title_style = dict(
    padding_top=Size.DEFAULT.value,
    font_size=FontSize.SMALL.value,
    font_family=Font.TITLE.value,
    font_weight="bold",
)
button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=FontSize.SMALL.value,
    color=TextColor.HEADER.value,
)
button_body_style = dict(
    font_size=FontSize.SMALL.value,
    color=TextColor.BODY.value,
)