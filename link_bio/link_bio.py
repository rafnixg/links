"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from link_bio.styles import styles
from link_bio.views.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links

class State(rx.State):
    """The state of the app."""


def index() -> rx.Component:
    """The main page of the app."""
    return rx.vstack(
        rx.vstack(
            header(),
            links(),
            align="center",
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=styles.Size.BIG.value,
        ),
        footer(),
        align="center",
    )


app = rx.App(
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="dark"
    )
)
app.add_page(index)
