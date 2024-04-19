"""The header of the app."""

import reflex as rx
from link_bio.components.avatar import avatar
from link_bio.components.heading import heading
from link_bio.styles import styles


def header() -> rx.Component:
    """The header of the app."""
    return rx.vstack(
        rx.hstack(
            avatar("/logo.png", "RG"),
            heading(),
            align="center",
        ),
        align="center",
        margin_top=[
            "0px",
            styles.Size.BIG.value,
            styles.Size.BIG.value,
            styles.Size.BIG.value,
            styles.Size.BIG.value,
            styles.Size.BIG.value,
        ],
    )
