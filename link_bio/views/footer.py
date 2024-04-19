"""The footer of the app."""

from datetime import date

import reflex as rx


def footer() -> rx.Component:
    """The footer of the app."""
    return rx.vstack(
        rx.text(
            f"©️ 2012-{date.today().year} Made with ❤️ by Rafnix Guzmán",
        ),
        rx.link(
            "Source code available on GitHub.",
            href="https://github.com/rafnixg/links",
            is_external=True,
        ),
        align="center",
    )
