"""The link button component of the app."""

import reflex as rx


def _get_color_scheme(tag: str) -> str:
    switcher = {
        "globe": "lime",
        "rss": "lime",
        "linkedin": "sky",
        "newspaper": "mint",
        "github": "gray",
        "gitlab": "orange",
    }
    return switcher.get(tag, "indigo")


def link_button(tag: str, text: str, url: str) -> rx.Component:
    """The link button of the app."""

    return rx.link(
        rx.button(
            rx.icon(tag=tag),
            text,
            variant="surface",
            color_scheme=_get_color_scheme(tag),
        ),
        href=url,
        is_external=True,
        width="100%",
    )
