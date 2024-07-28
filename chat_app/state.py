import reflex as rx
from reflex.state import BaseState

class State(rx.State):
    people : dict[str, dict] = {
        "DevCmb":{
            "name":"DevCmb",
            "hover":False,
            "active":True,
            "status":"Offline"
        },
        "FireEntity":{
            "name":"FireEntity",
            "hover":False,
            "active":False,
            "status":"Online"
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
        "The Grass":{
            "name":"The Grass",
            "hover":False,
            "active":False,
            "status":"Online"
        },
    }
    user_pfps: dict = {
        "user": "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/3josh.jpg ",
        "DevCmb": "./devcbt.webp",
        "FireEntity": "./mrplane.webp",
        "Nibbles": "./nibbler.webp",
        "Shuflduf": "./shuffler.webp",
        "eepydavid": "./javid.webp",
        "The Grass": "./josh.jpg"
    }
    messages: list[list[str]] = [
        ["DevCmb","HELLO"],
        ["The Grass", "HII"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
        ["DevCmb","HELLO"],
    ]
    
    
    
    user = "The Grass"
    active_person:str = "DevCmb"
    current_text:str
    
    def set_current_text(self, text):
        self.current_text = text
    def send_msg(self):
        self.messages.append([self.user, self.current_text])
    
    
    def get_person(self, index):
        return self.people[index]
    def activate_person(self, person):
        
        self.people[self.active_person]["active"] = False
        self.people[person]["active"] = True
        self.active_person = person
