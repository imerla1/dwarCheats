from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller, Button
from pynput import keyboard
import re
import webbrowser
import requests
import random
import xml.etree.cElementTree as et

class Ognevnik(object):

    def __init__(self):
        self.zanoz_msg = 'личич заноз плиз !!'
        self.driver = webdriver.Firefox()
        self.mouse = Controller()
        self.keyboard = keyboard.Controller()
        self.instance = "http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id=229&instance_id=0" # ognevnik istance
        self.ogn_request = "http://w1.dwar.ru/hunt_conf.php?mode=farm&action=chek&xy=0&sig=f20b74978cd88fb679656725cfa09e7b&num={}&t=1"
        self.dwar_url = 'http://w1.dwar.ru'
        self.nunb_list = []
        self.index = 0
        self.name = "Огневик"
        self.ogn_ids = [12,11,18] # mgoni su es id aqvt da ar icvleba
        self.login()
        self.execute()

    def login(self):
        self.driver.get(self.dwar_url)
        # We have 100 second for authentication
    
        sleep(100)

    def fight(self):
        first_tab = (184, 78)
        self.mouse.position = first_tab
        sleep(0.5)
        self.mouse.click(Button.left, 1)
        sleep(3)
        hunt_position = (696, 154)
        self.mouse.position = hunt_position
        sleep(4)
        self.mouse.click(Button.left, 1)
        for _ in range(7):
            self.keyboard.press("q")
            sleep(4)

    def heal_zanoz(self): # TODO 
        pass
    def pick(self): # IT worksssssss !!!

        sleep(1)
        choice = self.ogn_ids[self.index]
        # print(choice)
        self.driver.execute_script(f'''window.open("{self.ogn_request.format(choice)}","_blank");''')
        self.index += 1
        window_after = self.driver.window_handles[1]
        # print(window_after)
        self.driver.switch_to_window(window_after)
        sleep(1)
        source_code = self.driver.page_source
        # print(source_code)
        if 'first_farmer="1"' in source_code:
            sleep(98)
            print("Ognevnik Finished")
        if self.index > 2:
            self.index = 0
        if r'msg="Вы находитесь в бою!"' in source_code:
            self.fight()

        self.driver.switch_to_window(self.driver.window_handles[0])

        self.mouse.position = (502, 78)
        self.mouse.click(Button.left, 1)
              

        sleep(0.5)
    
    def execute(self):
        while True:
            self.pick()

Ognevnik()