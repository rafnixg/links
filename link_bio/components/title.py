"""The title of the app."""
import reflex as rx
from link_bio.styles import styles

def title(text: str) -> rx.Component:
    """The title of the app."""
    return rx.heading(
        text,
        size='4',
        text_align='center',
        width='100%',
        margin_top=styles.Size.SMALL.value,
    )
