import reflex as rx
from reflex_motion import motion
from chat_app.components.avatar import avatar
from chat_app.state import State

def user_block(name):
    status = State.userdata[name]["status"]
    return rx.box(
        rx.desktop_only(
            motion(
                rx.hstack(
                    avatar(
                        name
                    ),
                    rx.vstack(
                        rx.text(name, color="#71D083", font_size="25px", font_weight="600"),
                        rx.text(status, color="#71D083", font_size="16px", font_weight="400"),
                        align_items="flex-start",
                        spacing="0px",
                    ),
                    
                    width="auto",
                    height="79px",
                    padding="10px",
                    align_items="center",
                    gap="12px",
                    bg="rgba(112, 254, 140, 0)",
                    border_radius="16px",
                    border="2px solid #3E7949",
                    
                    on_mouse_down= lambda: State.activate_person(name)
                    
                ),
                while_hover={
                    "scale":1.01,
                    "background-color":"rgba(112, 254, 140, 0.11)"
                },
                while_tap={
                    "scale": 0.85
                },
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            )
        ),
        rx.mobile_and_tablet(
            motion(
                rx.hstack(
                    avatar(name),
                    
                    width="80px",
                    height="80px",
                    padding="10px",
                    align_items="center",
                    gap="12px",
                    #bg = State.get_button_bg(name),
                    bg="rgba(112, 254, 140, 0)",
                    border_radius="16px",
                    border="2px solid #3E7949",
                    
                    on_mouse_down= lambda: State.activate_person(name)
                        
                ),
                while_hover={
                    "scale":1.01,
                    "background-color":"rgba(112, 254, 140, 0.11)"
                },
                while_tap={
                    "scale": 0.85
                },
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            )
        ),
        padding_top = "5px"
    )
def swap_account_menu():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.hstack(
                    rx.text("Swap account", size = "3"),
                    rx.icon("arrow-left-right", stroke_width=2, size=20)
                ),
                color_scheme="green",
                padding = "10px"
            )
        ),
        rx.dialog.content(
            rx.flex(
                rx.text(
                    "Name",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    value = State.username,
                    default_value=State.user,
                    placeholder="Enter your username",
                    on_change=State.set_username
                ),
                rx.text(
                    "Password",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    value=State.password,
                    placeholder="Enter your password",
                    type="password",
                    on_change=State.set_password
                ),
                
                rx.dialog.close(
                    rx.button(
                        "Confirm",
                        color_scheme="green",
                        on_click=State.set_user,
                    )
                ),
                direction="column",
                spacing="3",
            ),
        ),
    ),
def welcome_block():
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.box(
                            rx.desktop_only(
                                rx.hstack(
                                    avatar(State.user),
                                    rx.desktop_only(
                                        rx.vstack(
                                            rx.text("Welcome back,", color="#C2F0C2", font_size="16px", font_weight="400"),
                                            rx.text(State.user, color="#C2F0C2", font_size="25px", font_weight="600"),
                                            align_items="flex-start",
                                            spacing="0px",
                                        ),
                                    ),
                                    bg="rgba(112, 254, 140, 0.11)",
                                    border_radius="16px",
                                    width="100%",
                                    #height="auto",
                                    padding="10px",
                                    align_items="center",
                                    gap="12px",
                                )
                            ),
                            rx.mobile_and_tablet(
                                rx.hstack(
                                    avatar("user"),
                                    bg="rgba(112, 254, 140, 0.11)",
                                    border_radius="16px",
                                    width="80px",
                                    height="80px",
                                    padding="10px",
                                    align_items="center",
                                    gap="12px",
                                )
                            ),
                            width = "100%"
                        ),
                        variant="ghost",
                        border_radius = "16px",
                        width = "100%",
                        color_scheme="green"
                    )
                ),
                rx.dialog.content(
                    rx.vstack(
                        rx.dialog.title("Settings"),
                        rx.text(f"You are logged in as:"),
                        rx.text(State.user, weight="bold", size= "5"),
                        avatar(State.user, size=100, radius="large"),
                        
                        swap_account_menu(),
                        rx.dialog.close(
                            rx.button(
                                rx.hstack(
                                    rx.text("Confirm", size = "3"),
                                    rx.icon("check", stroke_width=3.5, size=20, padding_top = "3px")
                                ),
                                color_scheme="green",
                                padding = "10px"
                            )
                        ),
                    ),
                    
                )
            ),
    
    
    
def sidebar():
    return rx.box( 
        rx.desktop_only(
            rx.vstack(
                
                welcome_block(),
                rx.divider(border_color="rgba(113, 255, 143, 0.29)", border_width="2.5px", margin_y="15px"),
                rx.hstack(
                    rx.heading(
                        "Friends:",
                        color_scheme= "green",
                        align="left",
                        padding_right="65%"
                    ),
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button(
                                rx.icon(
                                    "plus",
                                    stroke_width=5,
                                    size=60
                                
                                ),
                                color_scheme="green",
                                variant="outline",
                                size="1",
                                height="5vh",
                                width="5vh",
                            ),
                        ),
                        rx.dialog.content(
                            rx.dialog.title(
                                "Add friend:",
                                color_scheme="green"
                            ),
                            rx.flex(
                                rx.input(
                                    value=State.friend_text,
                                    placeholder="Enter your friend's username",
                                    on_change=State.change_friend_text,
                                    width="100%",
                                    color_scheme="green"
                                ),
                                rx.dialog.close(
                                    rx.button(
                                        "Confirm",
                                        color_scheme="green",
                                        variant="soft",
                                        on_click=State.add_friend
                                    ),
                                ),
                                
                                direction="column",
                                spacing="3"
                            ),
                            color_scheme="green"
                        )
                    )
                    
                ),
                
                
                rx.scroll_area(
                    rx.foreach(
                        State.current_friends, 
                        user_block,
                    ),
                    scrollbars="vertical",
                    height= "100%",
                    spacing="2",
                    on_mount=State.get_friends
                ),
                width="25vw",
                height="100vh",
                bg="rgba(41, 249, 157, 0.04)",
                border_radius="12px",
                border="1px solid #20573E",
                padding="15px",
                align_items="center",
                spacing="10px",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                welcome_block(),
                rx.divider(border_color="rgba(0, 255, 143, 0.29)", border_width="2.5px", margin_y="15px"),
                rx.scroll_area(
                    rx.foreach(
                        State.current_friends, 
                        user_block,
                    ),
                    scrollbars="vertical",
                    height= "100%",
                    spacing="10px",
                    on_mount=State.get_friends
                ),
                width="112.5px",
                height="100vh",
                bg="rgba(41, 249, 157, 0.04)",
                border_radius="12px",
                border="1px solid #20573E",
                padding="15px",
                align_items="center",
                spacing="10px",
            )
        ),
        height="100%"
    )