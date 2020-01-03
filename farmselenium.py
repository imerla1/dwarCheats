import requests
import random
import xml.etree.cElementTree as et
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller, Button
from pynput import keyboard

class Farm(object):

    def __init__(self):
        self.mouse = Controller()
        self.keyboard = keyboard.Controller()
        self.instance = 'http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id=155&instance_id=0'
        self.farm_request = 'http://w1.dwar.ru/hunt_conf.php?mode=farm&action=chek&xy=0&sig=f20b74978cd88fb679656725cfa09e7b&num={}&t=1' 
        self.nums = []
        self.dwar_url = 'http://w1.dwar.ru'
        self.driver = webdriver.Firefox()
        self.login()
        self.execute()


    def login(self):
        self.driver.get(self.dwar_url)
        # We have 100 second for authentication
    
        sleep(100)
    def fight(self):
        counter = 0
        first_tab = (184, 78)
        self.mouse.position = first_tab
        sleep(0.5)
        self.mouse.click(Button.left, 1)
        sleep(3)
        hunt_position = (696, 154)
        self.mouse.position = hunt_position
        sleep(4)
        self.mouse.click(Button.left, 1)
        for _ in range(9):
            counter += 1
            self.keyboard.press("q")
            sleep(4)
            if counter == 2:
                self.keyboard.press('1')
            elif counter == 5:
                self.keyboard.press('2')
    def parse(self):
        self.nums.clear()
        req = requests.get(self.instance)
        with open('data.xml', 'w') as e:
            e.write(req.text)

        tree = et.parse("data.xml")
        root = tree.getroot()
        
        for item in root.findall('farm'):
            for child in item:
                if child.attrib['name'] == "Тысячелистник" or child.attrib['name'] == "Розмарин":
                    
                    self.nums.append(child.attrib['num'])

    def pick(self): # IT worksssssss !!!

        sleep(1)
        choice = random.choice(self.nums)
        self.driver.execute_script(f'''window.open("{self.farm_request.format(choice)}","_blank");''')
        
        window_after = self.driver.window_handles[1]
       
        self.driver.switch_to_window(window_after)
        sleep(1)
        source_code = self.driver.page_source
        
        if 'first_farmer="1"' in source_code:
            sleep(42)
            print("Farm finished Finished")
        
        if r'msg="Вы находитесь в бою!"' in source_code:
            self.fight()

        self.driver.switch_to_window(self.driver.window_handles[0])

        self.mouse.position = (502, 78)
        self.mouse.click(Button.left, 1)

    def execute(self):
        while 1:
            self.parse()
            self.pick()

we_did_it = Farm()
we_did_it