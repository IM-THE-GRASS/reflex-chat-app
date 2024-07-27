import reflex as rx
from reflex.state import BaseState

class State(rx.State):
    user = "user"
    active_person:str = "None"
    people : dict[str, dict] = {
        "DevCmb":{
            "name":"DevCmb",
            "hover":False,
            "active":False,
            "status":"Offline"
        },
        "FireEntity":{
            "name":"FireEntity",
            "hover":False,
            "active":False,
            "status":"Offline"
        },
        "Nibbles":{
            "name":"Nibbles",
            "hover":False,
            "active":False,
            "status":"Offline"
        },
        "Shuflduf":{
            "name":"Shuflduf",
            "hover":False,
            "active":False,
            "status":"Offline"
        },
    }
    user_pfps: dict = {
        "user": "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/3josh.jpg ",
        "DevCmb": "./devcbt.webp",
        "FireEntity": "./mrplane.webp",
        "Nibbles": "./nibbler.webp",
        "Shuflduf": "./shuffler.webp",
        "eepydavid": "./javid.webp",
    }
    def get_person(self, index):
        return self.people[index]