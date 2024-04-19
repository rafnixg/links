"""The links of the app."""

import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    """The links of the app."""
    return rx.vstack(
        title("Links"),
        link_button(text="Personal Website", tag="globe", url="https://rafnixg.dev"),
        link_button(text="Read our blog", tag="rss", url="https://blog.rafnixg.dev"),
        title("Professional"),
        link_button(
            text="LinkedIn", tag="linkedin", url="https://www.linkedin.com/in/rafnixg"
        ),
        link_button(
            text="Resume CV", tag="newspaper", url="https://resume.rafnixg.dev"
        ),
        title("Code"),
        link_button(text="GitHub", tag="github", url="https://github.com/rafnixg"),
        link_button(text="GitLab", tag="gitlab", url="https://github.com/rafnixg"),
    )
