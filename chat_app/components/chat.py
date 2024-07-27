import reflex as rx
from chat_app.components.avatar import avatar
from chat_app.state import State
def chat_header():
    return rx.box(
        rx.hstack(
            avatar("DevCmb", size=70),
            rx.vstack(
                rx.text("DevCmb", color="#71D083", font_size="25px", font_weight="600"),
                rx.text("Online", color="#71D083", font_size="20px"),
                align_items="flex-start",
            ),
            padding="15px",
            gap="12px",
            width="100%",
            bg="rgba(112, 254, 140, 0.11)",
            border="1px solid #2D5736",
            border_radius="81px",
        ),
        padding = "25px",
        width = "100%"
    )
def chat_input():
    return rx.hstack(
        rx.input(
            placeholder="Type a message...",
            flex=1,
            bg="#25482D",
            border="1px solid #2D5736",
            border_radius="81px",
            padding="12px 16px",
            color="#C2F0C2",
            font_size="25px",
            font_weight="600",
            height="58px",
        ),
        rx.button(
            rx.icon("send"),
            bg="rgba(101, 255, 130, 0.63)",
            border="1px solid #2C2C2C",
            border_radius="32px",
            width="58px",
            height="58px",
        ),
        width="100%",
        padding="5px 40px",
    )