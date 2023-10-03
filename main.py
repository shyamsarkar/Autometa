import pyautogui
import time
from autometa_concerns import Autometa
start_time = time.time()


obj = Autometa()
obj.open_website("https://www.bing.com")

for i in range(20):
    random_text = obj.get_random_text()
    if random_text != None:
        obj.hit_link(random_text)


time_elapsed = time.time() - start_time
pyautogui.alert("Developed by Shyam Sarkar\n\n---Code Execution Done---\n\n--Time Elapsed : %.2f--\n\n"%time_elapsed)

