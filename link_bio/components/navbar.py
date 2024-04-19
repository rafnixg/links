"""The navbar of the app."""
import reflex as rx


def navbar() -> rx.Component:
    """The navbar of the app."""
    return rx.hstack(
        rx.text("Rafnix Guzmán", height="40px"),
        position="sticky",
        top=0,
        bg="blue",
        padding="16px",
        z_index=1,
    )
