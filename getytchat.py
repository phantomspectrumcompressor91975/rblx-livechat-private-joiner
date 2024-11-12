from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium_stealth import stealth

options = ChromeOptions()
options.add_argument("-headless")

class ytchat():
    def __init__(self, video_id: str) -> None:
        if video_id:
            print("Opening Webdriver")
            self.driver = webdriver.Chrome(options=options)
            self.url = "https://www.youtube.com/live_chat?v=" + video_id
            stealth(self.driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )
            self.latest_id = None
            print("get live chat webpage")
            self.driver.get(self.url)
            # check if video id is valid
            if "Chat is disabled" in self.driver.page_source:
                raise SystemExit("Invalid Video ID")
            else: pass
        else:
            raise SystemExit("No Video ID")

    def NextChat(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        mydivs = soup.find_all("yt-live-chat-text-message-renderer", {"class": "style-scope yt-live-chat-item-list-renderer"})
        divId = str(mydivs[-1]["id"])
        if divId == self.latest_id:
            return None
        else:
            self.latest_id = divId
            container = self.driver.find_element(By.ID, divId)
            # Get Message
            content = container.find_element(By.ID, "content")
            message = content.find_element(By.ID, "message")
            # Get Author
            authorchip = container.find_element(By.CSS_SELECTOR, "yt-live-chat-author-chip")
            author = authorchip.find_element(By.ID, "author-name")
            return (author.text.encode('ascii', 'ignore'), message.text.encode('ascii', 'ignore'))
