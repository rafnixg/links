"""Heading component."""
import reflex as rx

from link_bio.styles import styles

def heading() -> rx.Component:
    """The heading of the app."""
    return rx.vstack(
        rx.heading("Hi, I'm Rafnix Guzmán", style=styles.heading),
        rx.text("Python & Odoo Developer | Tech Writer", style=styles.sub_heading),
        rx.text("@rafnixg", weight="bold", size="2"),
    )
