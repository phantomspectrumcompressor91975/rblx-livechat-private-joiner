import re
from getytchat import ytchat

chat = ytchat("")
class ServerJoiner():
    def __init__(self) -> None:
        self.isFound = False
        while True:
            nextC = chat.NextChat()
            if nextC:
                author, msg = nextC
                regex = self.hasRegex(msg.decode())
                if regex:
                    self.isFound = True
                    URL = regex.group()
                else:
                    print(f"{author} said: {msg}")
    
    def hasRegex(self, string):
        if self.isFound:
            print("Not Gonna Try Joining A Private Server Twice")
        else:
            regex = re.search(r"https:\/\/www.roblox\.com\/share.code=[a-z0-9-]+&type=Server", string)
            if regex:
                self.isFound = True
                return regex
            else: return False

s=ServerJoiner()
