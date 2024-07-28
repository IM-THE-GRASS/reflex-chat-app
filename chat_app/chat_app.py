import reflex as rx
from .components.chat import *
from .components.avatar import *
from .components.sidebar import *
from chat_app.state import State

    







def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            chat_header(),
            rx.box(
                rx.scroll_area(
                    rx.foreach(
                        State.messages,
                        message
                    ),
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
