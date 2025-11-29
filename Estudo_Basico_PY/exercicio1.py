import random
import time

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

while True:
    linha = ""
    for _ in range(100000):
        bit = random.choice(["0", "1"])
        if bit == "0":
            linha += f"{red}0{reset}"
        else:
            linha += f"{green}1{reset}"
    print(linha)
    time.sleep(0.1)
