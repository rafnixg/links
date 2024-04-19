"""The avatar of the app."""

import reflex as rx


def avatar(url: str, alt: str) -> rx.Component:
    """The avatar of the app."""

    return (
        rx.mobile_only(
            rx.avatar(
                src=url,
                fallback=alt,
                size="6",
            ),
        ),
        rx.tablet_and_desktop(
            rx.avatar(
                src=url,
                fallback=alt,
                size="8",
            ),
        ),
    )
