import reflex as rx
from chat_app.components.avatar import avatar
from chat_app.state import State

def chat_msgs():
    return rx.box(
        rx.scroll_area(
            rx.foreach(
                State.messages,
                message
            ),
            type="always",
            scrollbars="vertical",
            height = "58vh",
            width = "73vw"
        ),
        flex=1
    ),

def chat_header():
    return rx.box(
        rx.hstack(
            avatar(State.active_person, size=70),
            rx.vstack(
                rx.text(State.active_person, color="#71D083", font_size="25px", font_weight="600"),
                rx.text(State.people[State.active_person]["status"], color="#71D083", font_size="20px"),
                align_items="flex-start",
            ),
            padding="15px",
            gap="12px",
            width="100%",
            border="1px solid #2D5736",
            border_radius="81px",
        ),
        padding = "25px",
        width = "100%"
    )
def chat_input():
    return rx.hstack(
        rx.input(
            value = State.current_text,
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
            on_change=State.set_current_text
        ),
        rx.button(
            rx.icon("send"),
            bg="rgba(101, 255, 130, 0.63)",
            border="1px solid #2C2C2C",
            border_radius="32px",
            width="58px",
            height="58px",
            on_click=State.send_msg
        ),
        width="100%",
        padding="5px 40px",
    )
def message(msginfo: list):
    name = msginfo[0]
    content = msginfo[1]
    return rx.box(
        rx.hstack(
            avatar(name),
            rx.vstack(
                rx.text(name, color="#71D083"),
                rx.text(content, color="#71D083", font_size="24px", width = "50vw"),
                gap="2px",
            ),
            padding="20px",
            gap="12px",
        ),
    )