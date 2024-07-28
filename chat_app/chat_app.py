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
            align_items="flex-start",
            gap="2px",
        ),
        padding="20px",
        justify_content="flex-start",
        align_items="flex-start",
        gap="12px",
    ),







def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            chat_header(),
            rx.box(
                rx.scroll_area(
                    message("devcmb", "mee"),
                    message("your", "mom"),
                    message("your", "mom"),
                    message("your", "momaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
                    message("your", "mom"),
                    message("your", "mom"),
                    type="always",
                    scrollbars="vertical",
                    #height = "20%",
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
