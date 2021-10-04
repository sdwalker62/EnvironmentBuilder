# version = 2.0
# ========================================================== #
#                      Section 0: Setup                      #
# ========================================================== #

# -- Imports -- #
import os
import subprocess 
import sys
from subprocess import CalledProcessError, PIPE
import functools

# -- Custom Functions -- #
from utilities import *
install_pkg('termcolor')
from termcolor import colored

# -- Check for root privileges -- # 
if os.geteuid() != 0: 
  print('This script requires root privileges to operate properly.') 
  sys.exit()

#user = run_and_capture('whoami')
home = run_and_capture('echo $HOME')

# -- Gather necessary user information for Github ssh keys -- #
while True:
  github_email = get_user_input("'Your GitHub email is required for setting up ssh properly. Enter the email you use for your GitHub account:'\n")
  github_email2 = get_user_input("Please repeat that!\n")
  if github_email != github_email2:
    print(colored("\nValues do not match!\n", 'red', attrs=['bold']))
    continue
  else:
    print(colored("\nSetting your github email to " + github_email, 'blue'))
    break

run('sudo apt-get update')
run('sudo apt-get upgrade')
run('mkdir tmp')
run('mkdir $HOME/Development')



# ========================================================== #
#                     Section 1: Preamble                    #
# ========================================================== #
title = """
  _   _ _             _          ___      _               ___         _      _   
 | | | | |__ _  _ _ _| |_ _  _  / __| ___| |_ _  _ _ __  / __| __ _ _(_)_ __| |_ 
 | |_| | '_ \ || | ' \  _| || | \__ \/ -_)  _| || | '_ \ \__ \/ _| '_| | '_ \  _|
  \___/|_.__/\_,_|_||_\__|\_,_| |___/\___|\__|\_,_| .__/ |___/\__|_| |_| .__/\__|                                  
"""

intro_text = """This script will download and install the following items: \n\n
1. zsh \n
2. oh-my-zsh \n
3. pyenv \n
4. fonts \n
5. VS Code \n
6. Docker \n
7. Flutter \n
8. Jetbrains Toolbox \n
9. Google Chrome \n
10. Gnome \n
11. necessary tools \n
12. Spotify \n
13. Hyper \n\n

The script will ask for some basic information to generate the necessary ssh keys for git. 
After that information is provided it will proceed without user input."""

print(colored(title, 'green'))
print(colored('This script requires root privileges to operate properly.', 'red', attrs=['bold'])) 
print(intro_text)


# ========================================================== #
#                    Section 2: Packages                     #
# ========================================================== #

# -- Package 0: zsh -- #
import packages.zsh
packages.zsh.install()

# -- Package 1: pyenv -- #
import packages.pyenv
packages.pyenv.install()

# -- Package 2: Fonts -- #
import packages.fonts
packages.fonts.install()

# -- Package 3: Docker -- #
import packages.docker
packages.docker.install()

# -- Package 4: Google Chrome -- #
import packages.google_chrome
packages.google_chrome.install()

# -- Package 5: VS Code -- #
import packages.vs_code
packages.vs_code.install()

# -- Package 6: Flutter -- #
import packages.flutter
packages.flutter.install()

# -- Package 7: Discord -- #
import packages.discord
packages.discord.install()

# -- Package 8: Hyper -- #
import packages.hyper
packages.hyper.install()

# -- Package 9: Spotify -- #
import packages.spotify
packages.spotify.install()


# TODO:
# 1. Add JetBrains Toolbox
# 2. Add Gnome
# 3. Add KDE
# 4. Add latte-dock
# 5. GitHUb SSH Keys
# 6. GitLab 
# 7. Options
# 8. Update readme (include Linux Information Google Doc)


# ========================================================== #
#                    Section 3: Clean-up                     #
# ========================================================== #
run('sudo rm -r tmp')