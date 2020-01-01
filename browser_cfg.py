import webbrowser
from pynput.mouse import Controller, Button
from time import sleep
import random
import requests
import xml.etree.cElementTree as et

mouse = Controller()
url = "http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id=155&instance_id=0"
post_request = "http://w1.dwar.ru/hunt_conf.php?mode=farm&action=chek&xy=0&sig=f20b74978cd88fb679656725cfa09e7b&num={}&t=1"

webbrowser.open_new("http://w1.dwar.ru")
sleep(7)
mouse.position = (450, 435)
mouse.click(Button.left, 1)
sleep(4)
mouse.position = (450, 435)
mouse.click(Button.left, 1)
sleep(5)
while True: # 22:48 31 jamhshi
    
    req = requests.get(url)
    with open('data.xml', 'w') as e:
        e.write(req.text)

    tree = et.parse("data.xml")
    root = tree.getroot()
    data = []
    for item in root.findall('farm'):
        data.clear()
        for child in item:
            if child.attrib['name'] == "Тысячелистник" or child.attrib['name'] == "Розмарин":
                
                data.append(child.attrib['num'])

    choice = random.choice(data)
    webbrowser.open_new_tab(post_request.format(choice))
    sleep(42)
    
    mouse.position = (542, 45)
    mouse.click(Button.left, 1)
    sleep(0.5)