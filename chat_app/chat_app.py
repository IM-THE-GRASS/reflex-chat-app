import reflex as rx
from .components.chat import *
from .components.avatar import *
from .components.sidebar import *
from chat_app.state import State


    



def message(name, content):
    return rx.hstack(
        avatar(name),
        rx.vstack(
            rx.text(name, color="#71D083"),
            rx.text(content, color="#71D083", font_size="24px", width = "50vw"),
            gap="2px",
        ),
        padding="20px",
        gap="12px",
    ),







def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            chat_header(),
            rx.box(
                rx.scroll_area(
                    message("DevCmb", "mee"),
                    message("The Grass", "hi"),
                    message("FireEntity", "aaa"),
                    message("The Grass", "TEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAPTEXT WRAP"),
                    message("example person with no avatar", "I have no avatar!!"),
                    type="always",
                    scrollbars="vertical",
                    height = "60vh",
                    width = "73vw"
                ),
                flex=1
            ),
            chat_input(),
            width="100%",
        ),
        width="100%",
        bg="#121B17",
    )

app = rx.App()
app.add_page(index)
