"""The link button component of the app."""

import reflex as rx


def link_button(tag: str, text: str, url: str) -> rx.Component:
    """The link button of the app."""
    return rx.link(
        rx.button(
            rx.icon(tag=tag),
            text,
            variant="solid",
        ),
        href=url,
        is_external=True,
        width="100%",
    )
