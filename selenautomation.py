from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller, Button
import re
import webbrowser
import requests
import random
import xml.etree.cElementTree as et

class Ognevnik(object):

    def __init__(self):

        self.mouse = Controller()
        self.msg = None
        self.instance = "http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id=155&instance_id=0"
        self.post_request = "http://w1.dwar.ru/hunt_conf.php?mode=farm&action=chek&xy=0&sig=f20b74978cd88fb679656725cfa09e7b&num={}&t=1"
        self.first_farmer = False
        self.id_numbers = []
        self.prev_id = None
        self.driver = webdriver.Firefox()
        self.login()
        
        self.execute()
        
    def login(self):
        
        self.driver.get("https://w1.dwar.ru")

        
        sleep(45)
        

    def parse(self):
        print("Parse is executing NOw --------")
        self.id_numbers.clear()
        response = requests.get(self.instance)
        with open('data.xml', 'w') as e:
            e.write(response.text)

        tree = et.parse("data.xml")
        root = tree.getroot()
        for item in root.findall('farm'):
        
            for child in item:
                if child.attrib['name'] == "Тысячелистникs":
                    self.id_numbers.append(child.attrib['num'])



    def new_tab(self):
        print("New tab is executing Now --------")
        choice = random.choice(self.id_numbers)
        
        
        self.driver.execute_script(f'''window.open("{self.post_request.format(choice)}","_blank");''')
        
    
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        sleep(1)
        source_code = self.driver.page_source
        if 'first_farmer="1"' in source_code:
            sleep(93)
            print("done picking")
            
        else:
            self.prev_id = choice
            self.first_farmer = False
        
        sleep(0.5)
    def do_staff(self):
        if self.first_farmer:
            print("DOSTAFFF ----")
            choice = random.choice(self.id_numbers)
        
        
            self.driver.execute_script(f'''window.open("{self.post_request.format(choice)}","_blank");''')
        
    
            window_after = self.driver.window_handles[1]
            self.driver.switch_to_window(window_after)
            sleep(42)
            self.mouse.position = (502, 78)
            self.mouse.click(Button.left, 1)
            sleep(0.5)

    def execute(self):
        print("Execute Now")
        while True:
            self.parse()
            self.new_tab()
            self.do_staff()


Ognevnik()