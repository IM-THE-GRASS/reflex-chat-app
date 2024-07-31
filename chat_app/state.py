import reflex as rx
from reflex.state import BaseState
import os
import pickle

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
    
    
    
    
    
    user:str = "The Grass"
    active_person:str = "DevCmb"
    current_text:str
    username:str
    password:str
    
    
    
    
    
    def get_msgs(self):
        msg_file = f"./user_msgs/{self.user}/{self.active_person}.pickle"
        msg_dir = f"./user_msgs/{self.user}"
        msg_file_2 = f"./user_msgs/{self.active_person}/{self.user}.pickle"
        msg_dir_2 = f"./user_msgs/{self.active_person}"
        if not os.path.isfile(msg_file):
            if not os.path.isfile(msg_file_2):
                try:
                    os.makedirs(msg_dir)    
                except:
                    pass
                open(msg_file, 'x')
                
                with open(msg_file, "wb") as file:
                    pickle.dump([], file)
                self.messages = []
            else:
                with open(msg_file_2, "rb") as file:
                    self.messages = pickle.load(file)
        else:
            with open(msg_file, "rb") as file:
                self.messages = pickle.load(file)
    def update_msg_file(self):
        msg_file = f"./user_msgs/{self.user}/{self.active_person}.pickle"
        if not os.path.isfile(msg_file):
            msg_file = f"./user_msgs/{self.active_person}/{self.user}.pickle"
        with open(msg_file, "wb") as file:
                pickle.dump(self.messages, file)
            
            
    def set_current_text(self, text):
        self.current_text = text
    def send_msg(self):
        self.messages.append([self.user, self.current_text])
        self.update_msg_file()
        self.current_text = ""
    def set_user(self):
        self.user = self.username
        return rx.toast("Login succesful!")
    
    def set_username(self, new_username):
        self.username = new_username
    def set_password(self, new_pass):
        self.password = new_pass
    
    
    
    
    def get_person(self, index):
        return self.people[index]
    def activate_person(self, person):
        self.get_msgs()
        self.people[self.active_person]["active"] = False
        self.people[person]["active"] = True
        self.active_person = person
        self.get_msgs()
