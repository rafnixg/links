"""The header of the app."""

import reflex as rx
from link_bio.styles import styles


def header() -> rx.Component:
    """The header of the app."""
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="/logo.png", fallback="RG", size="8"),
            rx.vstack(
                rx.heading("Hi, I'm Rafnix Guzmán", size="7"),
                rx.text("Python & Odoo Developer | Tech Writer", size="4"),
                rx.text("@rafnixg", weight="bold", size="2"),
            ),
            align="center",
        ),
        align="center",
        margin_top=styles.Size.BIG.value,
    )
