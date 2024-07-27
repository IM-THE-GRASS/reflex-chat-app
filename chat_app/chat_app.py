import reflex as rx
class State(rx.State):
    user = "user"
    user_pfps: dict = {
        "user": "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/3josh.jpg ",
        "DevCmb": "./devcbt.webp",
        "FireEntity": "./mrplane.webp",
        "Nibbles": "./nibbler.webp",
        "Shuflduf": "./shuffler.webp",
        "eepydavid": "./javid.webp",
    }
def avatar(img:str, size=60):
    return rx.avatar(
        src=f"{State.user_pfps[img]}",
        width = f"{size}px", height = f"{size}px", 
        fallback=f"{img[0:2]}", 
        radius="full"
    ),

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

def user_block(name, status="Online"):
    return rx.hstack(
        avatar(name),
        rx.vstack(
            rx.text(name, color="#71D083", font_size="25px", font_weight="600"),
            rx.text(status, color="#71D083", font_size="16px", font_weight="400"),
            align_items="flex-start",
            spacing="0px",
        ),
        width="294px",
        height="79px",
        padding="10px",
        align_items="center",
        gap="12px",
        bg="rgba(112, 254, 140, 0.11)",
        border_radius="16px",
        border="2px solid #3E7949",
    )

def sidebar():
    return rx.vstack(
        welcome_block(),
        rx.divider(border_color="rgba(113, 255, 143, 0.29)", border_width="2.5px", margin_y="15px"),
        user_block("DevCmb"),
        user_block("FireEntity"),
        user_block("Nibbles"),
        user_block("Shuflduf"),
        user_block("eepydavid"),
        width="325px",
        height="1075px",
        bg="rgba(41, 249, 157, 0.04)",
        border_radius="12px",
        border="1px solid #20573E",
        padding="15px",
        align_items="center",
        spacing="10px",
    )
def chat_header():
    return rx.hstack(
        avatar("devcmb", size=95),
        rx.vstack(
            rx.text("DevCmb", color="#71D083", font_size="25px", font_weight="600"),
            rx.text("Online", color="#71D083", font_size="14px"),
            align_items="flex-start",
        ),
        padding="10px",
        gap="12px",
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
        padding="32px 40px",
    )

def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            chat_header(),
            chat_input(),
            height="100vh",
            width="100%",
        ),
        width="100%",
        height="100vh",
        bg="#121B17",
    )

app = rx.App()
app.add_page(index)
