# -- Imports -- #
import os 
import sys
import subprocess

version = 1.0

def print_header(msg, index):
  print('\n')
  print(str(index) + '. ' + msg)
  print ('\n')


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
print(title)
print('version: ' + str(version))
print(intro_text)


# -- Check for root privileges -- # 
#if os.geteuid() != 0: 
#  print(colored('This script requires root privileges to operate properly.', 'red', attrs=['bold'])) 
#  sys.exit()


# -- Gather necessary user information for Github ssh keys -- #
print('Your GitHub email is required for setting up ssh properly. Enter the email you use for your GitHub account:')
#github_email = input()


# -- Install zsh -- #
print_header('Installing zsh', 1)

print('Gathering prerequisites ...')
cmd = ['apt', 'list', '--installed', '|', 'grep', 'curl']
shell_out = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
print(shell_out)


