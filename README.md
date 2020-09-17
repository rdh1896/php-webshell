# Russell's Web_Shell
Basic PHP Webshell for Red Team use. The shell.php file must be placed on the target system and accessible via a URI in order for the script to work. Simply run the Python3 script on your machine and input only the target IP address.

For Example:
  127.0.0.1
  
By default the script will append the correct URL to the address to establish the connection. You are then free to issue commands to the server as if you were locally on the system.

# Installation
    1. Simply download the GitHub repo to your PC, unzip the "php-webshell-master.zip" file
    and navigate to the "php-webshell-master" directory.
    2. From here, locate "shell.php" and "shell_client.py", "shell.php needs to be placed
    on the target machine (see more in Usage Instructions).
    3. You may need to install requests and Beautiful Soup for the "shell_client.py"
    file to run correctly. Try:
      pip3 install requests
      pip3 install beautifulsoup
    4. Success!

# Usage Instructions
    1. Install "shell.php" on to the target web server within the /var/www/html directory (you will need to find an
    exploit or be given access to the server to get this file there).
    2. Run the script using "python3 shell_client.py"
    3. Enter just the IP address/URL of the target server (Do not include prefixes or suffixes).
    4. Press enter for HTTP, or enter 1 if the server is running HTTPS.
    5. You can now enter commands as if you were logged in as the Apache user! Try
    commands such as "whoami" or "cat /etc/passwd".
