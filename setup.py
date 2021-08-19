# -- Imports -- #
import os 
import sys
from subprocess import run, PIPE
import yaml

version = 1.0


def print_header(msg, index):
  print('\n')
  print(str(index) + '. ' + msg)
  print ('\n')


def run_cmd(cmd):
  return run(
    cmd, 
    shell=True, 
    stdout=PIPE, 
    stderr=PIPE, 
    check=True).stdout.decode('utf-8')


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
cmd = 'apt-cache policy curl'
res = run_cmd(cmd)
parse_res = yaml.safe_load(res)
print(parse_res['Installed'])
test_for_existence = res.split('Installed:')[1][2:6] == 'none'

if not test_for_existence:
  print('curl is not installed!')


