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
            margin_y=styles.Size.DEFAULT.value,
        ),
        footer(),
        align="center",
        padding_x=styles.Size.SMALL.value,
    )


app = rx.App(style=styles.BASE_STYLE, theme=rx.theme(appearance="dark"))

app.add_page(
    component=index,
    title="Rafnix Guzmán | Enlaces, proyectos y artículos.",
    description="Enlaces a mis redes sociales, proyectos y artículos.",
    meta=[
        {"name": "author", "content": "Rafnix Guzmán"},
        {"name": "keywords", "content": "Python, Odoo, Developer, Tech Writer"},
        {"charset": "UTF-8"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        {
            "name": "description",
            "content": "Enlaces a mis redes sociales, proyectos y artículos.",
        },
        {
            "property": "og:title",
            "content": "Rafnix Guzmán | Enlaces, proyectos y artículos.",
        },
        {
            "property": "og:description",
            "content": "Enlaces a mis redes sociales, proyectos y artículos.",
        },
        {"property": "og:image", "content": "https://links.rafnixg.dev/logo.png"},
        {"property": "og:url", "content": "https://links.rafnixg.dev"},
        {"property": "og:type", "content": "website"},
        {"property": "og:site_name", "content": "Rafnix Guzmán"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@rafnixg"},
        {"name": "twitter:creator", "content": "@rafnixg"},
        {
            "name": "twitter:title",
            "content": "Rafnix Guzmán | Enlaces, proyectos y artículos.",
        },
        {
            "name": "twitter:description",
            "content": "Enlaces a mis redes sociales, proyectos y artículos.",
        },
        {"name": "twitter:image", "content": "https://links.rafnixg.dev/logo.png"},
        {"name": "twitter:image:alt", "content": "Rafnix Guzmán"},
    ],
)
