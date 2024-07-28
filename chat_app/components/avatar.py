import reflex as rx
from chat_app.state import State
def avatar(img:str, size=60, **kwargs):
    return rx.avatar(
        src=f"{State.user_pfps[img]}",
        width = f"{size}px", height = f"{size}px", 
        fallback=f"{img[0:2]}", 
        radius="full",
        **kwargs
    ),