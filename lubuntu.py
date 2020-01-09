import requests
import random
import xml.etree.cElementTree as et
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller, Button
from pynput import keyboard

class Farm(object):
    """Basic farm Class for dwar Cheat"""
    def __init__(self):
        self.zanoz_msg = 'личич заноз плиз !!'
        self.mouse = Controller()
        self.keyboard = keyboard.Controller()
        self.instance = 'http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id=156&instance_id=0' # Instance url where to farm resources
        self.farm_request = 'http://w1.dwar.ru/hunt_conf.php?mode=farm&action=chek&xy=0&sig=f20b74978cd88fb679656725cfa09e7b&num={}&t=1' # i think this field requiere User Token, it must be change for various usrers
        self.nums = []
        self.dwar_url = 'http://w1.dwar.ru' 
        self.driver = webdriver.Firefox()
        self.login()
        self.execute()


    def login(self):
        'This function simply calls webbrowser and get dwar url Than sleep 100 seconds to give user time for authentication'
        self.driver.get(self.dwar_url)
        # We have 100 second for authentication
    
        sleep(100)
    def mouse_event(self, sleep_timer, another_sleep=0, position=(), controller=Controller()):
        controller.position = position
        sleep(sleep_timer)
        controller.click(Button.left, 1)
        sleep(another_sleep)
    def fight(self):
        """Programa am funqcias idzaxebs im shemtxvevashi tu Users-s yvalvilebis
        grovebis dro Mobi daesxmeva Tavs"""
        counter = 0 
        first_tab = (120, 40)
        self.mouse_event(2, position=first_tab, another_sleep=2)
        
        hunt_position = (663, 137)
        self.mouse_event(2, 6, position=hunt_position)
        self.keyboard.press('r')
        self.keyboard.press('5')
        for _ in range(17):
            counter += 1
            
            sleep(1)
            self.keyboard.press("q")
            sleep(4)
            if counter == 3:
                self.keyboard.press('1')
            elif counter == 7:
                self.keyboard.press('2')
            elif counter == 11:
                self.keyboard.press('3')
            elif counter == 14:
                self.keyboard.press('4')
    def zanoz(self):
        """Tu useri aikidebs Zanozs programa idaxebs am funqcias romelic chatshi itxovs zanozis Gankurnvas,
            shemdeg 200 wami elodeba vinme tu ar gankurnavs tavidan aketebs motxvonas da ase izams sanam
            romelime motamashe ar zanoz-s ar mogxsnis"""
        sleep(3)
        first_tab = (120, 40)
        self.mouse.position = first_tab
        sleep(0.9)
        self.mouse.click(Button.left, 1)
        sleep(1)
        self.mouse.position = (619, 148)
        self.mouse.click(Button.left, 1)
        sleep(4)
        msg = 'lichi zanoz pls !! :mol:'
        start_y = 597
        diff = 14
        for _ in range(9):
            people = (1087, start_y)
            start_y += diff
            sleep(0.5)
            self.mouse.position = people
            self.mouse.click(Button.left, 1)
            sleep(0.5)
        self.mouse.position = (946, 725)
        sleep(0.4)
        self.mouse.click(Button.left, 1)
        for attar in msg:
            self.keyboard.press(attar)
            sleep(0.3)
        sleep(1.3)
        send_position = (1039, 724)
        sleep(1.3)
        self.mouse.position = send_position
        self.mouse.click(Button.left, 1)
        sleep(1.3) 
        sleep(200)
        backpack_position = (561,135)
        self.mouse.position = backpack_position
        sleep(1.1)
        self.mouse.click(Button.left, 1)
        sleep(9)
        veshi_pozicion = (730,236)
        self.mouse.position = veshi_pozicion
        self.mouse.click(Button.left, 1)
        sleep(7)
        serp_nadet = (597, 323)
        self.mouse.position = serp_nadet
        self.mouse.click(Button.left, 1)
        sleep(8)
        location_pos = (606, 147)
        self.mouse.position = location_pos
        self.mouse.click(Button.left, 1)
        sleep(9)

    def parse(self):
        """Suli da guli methodi Mteli sofits 
        romelic parasavs Instac-s resursis Num-ebs da amatebs list-shi"""
        self.nums.clear()
        req = requests.get(self.instance)
        with open('data.xml', 'w') as e:
            e.write(req.text)

        tree = et.parse("data.xml")
        root = tree.getroot()
        
        for item in root.findall('farm'):
            for child in item:
                if child.attrib['name'] == "Клевер":
                    
                    self.nums.append(child.attrib['num'])

    def pick(self): # IT worksssssss !!!
        # Wavedii Boti Cheteroba da ase shemdg :))))))
        sleep(1)
        choice = random.choice(self.nums)
        self.driver.execute_script(f'''window.open("{self.farm_request.format(choice)}","_blank");''')
        
        window_after = self.driver.window_handles[1]
       
        self.driver.switch_to_window(window_after)
        sleep(1)
        source_code = self.driver.page_source
        
        if 'first_farmer="1"' in source_code:
            sleep(20)
            print("Farm finished Finished")
        
        if r'msg="Вы находитесь в бою!"' in source_code:
            self.fight()
        if r'msg="У Вас нет необходимого инструмента!"' in source_code:
            self.zanoz()
        self.driver.switch_to_window(self.driver.window_handles[0])

        self.mouse.position = (433, 46)
        self.mouse.click(Button.left, 1)

    def execute(self):
        while 1:
            self.parse()
            self.pick()

we_did_it = Farm()
we_did_it
