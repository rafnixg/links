"""Styles for the link_bio app."""

from enum import Enum
import reflex as rx


MAX_WIDTH = "560px"


class Size(Enum):
    """The spacer sizes."""

    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"


BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding_y": "0.7em",
        "padding_x": Size.BIG.value,
        "border_radius": Size.SMALL.value,
    },
}

heading = {
    "font_size": ["1.3em", "1.5em", "2em", "2em", "2em"],
}
sub_heading = {
    "font_size": ["1.12em", "1.2em", "1.2em", "1.2em", "1.2em"],
}
