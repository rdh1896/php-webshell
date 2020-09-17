# Russell's Web_Shell
Basic PHP Webshell for Red Team use. The shell.php file must be placed on the target system and accessible via a URI in order for the script to work. Simply run the Python3 script on your machine and input only the target IP address.

For Example:
  127.0.0.1
  
By default the script will append the correct URI to the address to establish the connection. You are then free to issue commands to the server as if you were locally on the system.

Note that this PHP script utilizes authentication. This means that in order to execute commands you have to input the correct password. The password is stored in plaintext on the client-side Python script and is stored as an MD5 hash on the server-side PHP script.

# Usage Instructions
    1. Run the script using "python3 shell_client.py"
    2. Enter just the IP address/URL of the server (Do not include prefixes or suffixes)
    3. Press enter for HTTP, or enter 1 if the server is running HTTPS.
    4. You can now enter commands as if you were logged in as the Apache user! Try
    commands such as "whoami" or "cat /etc/passwd".
