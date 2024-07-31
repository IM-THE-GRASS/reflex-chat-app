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
            chat_msgs(),
            chat_input(),
            width="100%",
        ),
        width="100%",
        bg="#121B17",
    )

app = rx.App()
app.add_page(index)
