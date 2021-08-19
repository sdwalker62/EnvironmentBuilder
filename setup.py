# -- Imports -- #
from termcolor import colored

version = 1.0

# -- Introduction -- #
title = """
  ___      _   _               ___      _               ___         _      _   
 | _ \_  _| |_| |_  ___ _ _   / __| ___| |_ _  _ _ __  / __| __ _ _(_)_ __| |_ 
 |  _/ || |  _| ' \/ _ \ ' \  \__ \/ -_)  _| || | '_ \ \__ \/ _| '_| | '_ \  _|
 |_|  \_, |\__|_||_\___/_||_| |___/\___|\__|\_,_| .__/ |___/\__|_| |_| .__/\__|
      |__/                                      |_|                  |_|             
"""

intro_text = """
This script will download and install the following items: \n
1. zsh \n
2. oh-my-zsh \n
3. pyenv \n
4. fonts \n
5. VS Code \n
6. Docker \n
7. Flutter \n
8. Jetbrains Toolbox \n
9. Google Chrome \n
10. kde \n\n
11. necessary tools \n

The script will ask for some basic information to generate the necessary ssh keys for git. 
After that information is provided it will proceed without user input. 

"""
print(colored(title, 'green'))
print(colored('version: ' + str(version), 'blue', attrs=['bold']))
print(intro_text)

# -- Gather necessary user information for Github ssh keys -- #