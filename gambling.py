#gambling module of ho man tin sim
import random
import time

colors = {
    "C": "\033[39m",
    "U": "\033[32m", 
    "R": "\033[36m",  
    "E": "\033[35m",  
    "L": "\033[33m", 
    "RESET": "\033[0m"  
}

rarity = {
    1: "C",
    2: "U",
    3: "R",
    4: "E",
    5: "L"
}

chances = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,5]

def rolling():
    show = ['','','','','','','','','']
    for i in range(len(show)):
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[i] = rarity[b]
    print("Rolling for your labubu......")
    print('                ↓')
    for i in range(50):
        c_show = [f"{colors[char]}{char}{colors['RESET']}" if char in colors else char for char in show]
        print('   '.join(c_show), end='\r')
        time.sleep(i/70)
        show = show[-1:] + show[:-1]
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[0] = rarity[b]
    return show[4]

rolling()
