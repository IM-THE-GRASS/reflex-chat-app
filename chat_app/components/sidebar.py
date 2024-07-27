import reflex as rx

from chat_app.components.avatar import avatar
from chat_app.state import State

def user_block(userinfo : dict, index: int):
    return rx.hstack(
        #avatar(name),
        rx.vstack(
        #    rx.text(name, color="#71D083", font_size="25px", font_weight="600"),
        #    rx.text(status, color="#71D083", font_size="16px", font_weight="400"),
            align_items="flex-start",
            spacing="0px",
        ),
        width="294px",
        height="79px",
        padding="10px",
        align_items="center",
        gap="12px",
        #bg = State.get_button_bg(name),
        bg="rgba(112, 254, 140, 0.11)",
        border_radius="16px",
        border="2px solid #3E7949",
        on_mount=print
        #on_mouse_enter= State.hover_person(name, True),
        #on_mouse_leave= State.hover_person(name, False),
        #on_mouse_down= State.activate_person(name)
        
        
    )

def welcome_block():
    return rx.hstack(
        avatar("user"),
        rx.vstack(
            rx.text("Welcome back,", color="#C2F0C2", font_size="16px", font_weight="400"),
            rx.text("Josh", color="#C2F0C2", font_size="25px", font_weight="600"),
            align_items="flex-start",
            spacing="0px",
        ),
        bg="rgba(112, 254, 140, 0.11)",
        border_radius="16px",
        width="294px",
        height="79px",
        padding="10px",
        align_items="center",
        gap="12px",
    )
    
def sidebar():
    return rx.vstack(
        welcome_block(),
        rx.divider(border_color="rgba(113, 255, 143, 0.29)", border_width="2.5px", margin_y="15px"),
        rx.scroll_area(
            rx.foreach(
                State.people, 
                lambda color, index: user_block(color, index),
            ),
            scrollbars="vertical",
            height= "100%",
        ),
        width="25vw",
        height="100%",
        bg="rgba(41, 249, 157, 0.04)",
        border_radius="12px",
        border="1px solid #20573E",
        padding="15px",
        align_items="center",
        spacing="10px",
    )