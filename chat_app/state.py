import reflex as rx
from reflex.state import BaseState
import os
import pickle

class State(rx.State):
    def pickledump(self, filed, obj):
        with open(filed, "wb") as file:
            pickle.dump(obj, file)
    def pickleread(self, file):
        with open(file, "rb") as file:
            return pickle.load(file)
    userdata : dict[str, dict] = pickle.load(open("./userdata.pickle", "rb"))   
    print(userdata)
    def load_userdata(self):
        self.userdata = self.pickleread("./userdata.pickle")
        print("loaded the userdata")
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
    
    
    
    friend_text:str
    user:str = "The Grass"
    active_person:str = "DevCmb"
    current_text:str
    username:str
    password:str
    friends:dict[str, list[str]]
    current_friends:list[str]
    def get_friends(self):
        self.friends = {}
        for person in self.userdata:
            self.friends[person] = list(self.userdata[person]["friends"])
        self.current_friends = self.friends[self.user] 
        print(self.current_friends)
        print(self.friends)
        print("AAAA")
    
    
    def add_friend(self):
        friend= self.friend_text
        if not friend in self.userdata:
            return rx.toast("User not found")
        if friend in self.friends[self.user]:
            return rx.toast("You are already friends with this user!")
        else:
            self.current_friends.append(friend) 
            self.userdata[self.user]["friends"].append(friend)
            self.pickledump(
                "./userdata.pickle",
                self.userdata
            )
            return rx.toast("Friend added successfully")
    
    def change_friend_text(self, new_text):
        self.friend_text = new_text
    
    
    def get_msgs(self):
        msg_file = f"./user_msgs/{self.user}/{self.active_person}.pickle"
        msg_dir = f"./user_msgs/{self.user}"
        msg_file_2 = f"./user_msgs/{self.active_person}/{self.user}.pickle"
        if not os.path.isfile(msg_file):
            if not os.path.isfile(msg_file_2):
                try:
                    os.makedirs(msg_dir)    
                except:
                    pass
                open(msg_file, 'x')
                
                self.pickledump(msg_file, [])
                self.messages = []
            else:
                self.messages = self.pickleread(msg_file_2)
        else:
            self.messages = self.pickleread(msg_file)
    def update_msg_file(self):
        msg_file = f"./user_msgs/{self.user}/{self.active_person}.pickle"
        if not os.path.isfile(msg_file):
            msg_file = f"./user_msgs/{self.active_person}/{self.user}.pickle"
        self.pickledump(msg_file, self.messages)
            
    def set_current_text(self, text):
        self.current_text = text
    def send_msg(self):
        self.messages.append([self.user, self.current_text])
        self.update_msg_file()
        self.current_text = ""
        
        

        
    def set_user(self):
        try:
            if self.password == self.userdata[self.username]["password"]:
                self.password = ""
                self.user = self.username
                self.get_friends()
                return rx.toast("Login succesful!")
                
            else:
                self.password = ""
                return rx.toast("Incorrect username or password")
        except:
            self.password = ""
            return rx.toast("Incorrect username or password")
    def set_username(self, new_username):
        self.username = new_username
    def set_password(self, new_pass):
        self.password = new_pass
    
    
    
    
    def get_person(self, index):
        return self.userdata[index]
    def activate_person(self, person):
        self.userdata[self.active_person]["active"] = False
        self.userdata[person]["active"] = True
        self.active_person = person
        print(person)
        self.get_msgs()
