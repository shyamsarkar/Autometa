import requests
import pyautogui
import time
import subprocess
import random


class Autometa:
    def __init__(self):
        print("-----Running ShyamSarkar Autometa-----")
        try:
            # command_to_execute = ["google-chrome", "https://www.bing.com"]
            command_to_execute = ["google-chrome"]
            run = subprocess.run(command_to_execute, capture_output=True)
        except:
            # command_to_execute = ["start", "chrome", "https://www.bing.com"]
            command_to_execute = ["start", "chrome"]
            run = subprocess.run(command_to_execute, capture_output=True)
        print(run.stdout)
        print(run.stderr)

    def mouse_pointer_position(self):
        """-----(x=35, y=1955) Window Key Position"""
        time.sleep(2)
        return pyautogui.position() # position tracker of mouse

    def open_website(self, site_url):
        """-----Running for the first time-----"""
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.typewrite(site_url)
        pyautogui.press('enter')

    def hit_link(self, random_text):
        pyautogui.typewrite(random_text)
        pyautogui.press('enter')
        time.sleep(1)

    def get_random_text(self):
        methods_list = [self.string_one, self.string_two, self.string_three, self.string_four, self.string_five]
        random_method = random.choice(methods_list)
        return random_method()
            
    def string_one(self):
        try:
            resp = requests.get('https://random-word-api.herokuapp.com/word')
            return f"What is the meaning of {resp.json()[0]} in hindi"
        except:
            return None

    def string_two(self):
        try:
            resp = requests.get('https://www.boredapi.com/api/activity')
            return resp.json()['activity']
        except:
            return None

    def string_three(self):
        try:
            resp = requests.get('https://official-joke-api.appspot.com/random_joke')
            return resp.json()['setup']
        except:
            return None

    def string_four(self):
        try:
            resp = requests.get('https://randomuser.me/api/')
            details = resp.json()["results"][0]
            return f"Who is {details['name']['first']} {details['name']['last']} from {details['location']['country']}"
        except:
            return None

    def string_five(self):
        try:
            resp = requests.get('https://catfact.ninja/fact')
            return resp.json()['fact']
        except:
            return None

    # def search_begin(self, random_word):
    #     """-----Searching On Searchbar-----"""
    #     time.sleep(1)
    #     # pyautogui.click(x=1343, y=661)
    #     pyautogui.typewrite(f"what is the meaning of {random_word} in hindi")
    #     pyautogui.press('enter')

    #     if resp.status_code == 200:
    #         return resp.json()[0]
    #     else:
    #         return None

    # def search_again(self, random_word):
    #     pyautogui.typewrite(f"what is the meaning of {random_word} in hindi")
    #     pyautogui.press('enter')

    #     time.sleep(1)
    #     """-----Again Search-----"""
    #     pyautogui.click(x=820, y=355) #select the text search box
    #     pyautogui.hotkey('ctrl', 'a')

    # def open_url(self, site_url):
    #     pyautogui.hotkey('ctrl', 'l')
    #     pyautogui.typewrite(site_url)
    #     pyautogui.press('enter')

    
