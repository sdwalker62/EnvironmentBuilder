# version = 1.0
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
#                     Section 2: Stages                      #
# ========================================================== #

# -- Stage 0: zsh -- #
import stages.zsh
stages.zsh.exec_stage()

# -- Stage 1: pyenv -- #
import stages.pyenv
stages.pyenv.exec_stage()

# -- Stage 2: Fonts -- #
import stages.fonts
stages.fonts.exec_stage()





# -- Install pyenv -- #

run(cmd)
#run(" git clone https://github.com/pyenv/pyenv.git " + home + "/.pyenv")



# -- Install fonts -- #
print_header('Installing fonts', 1, 'green')
check_and_install_pkg('wget')
run('mkdir firacode_nf')
run('mkdir firamono_nf')
run('mkdir ' + home + '/.local/share/fonts')

# Install FiraCode NerdFont
url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraCode.zip"
cmd = 'wget ' + url
run(cmd)
run('unzip FiraCode.zip -d firacode_nf')
run('cp firacode_nf/Fira\ Code\ Bold\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firacode_nf/Fira\ Code\ Light\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firacode_nf/Fira\ Code\ Medium\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firacode_nf/Fira\ Code\ Regular\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firacode_nf/Fira\ Code\ Retina\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')

# Install FiraMono NerdFont
url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraMono.zip"
cmd = 'wget ' + url
run(cmd)
run('unzip FiraMono.zip -d firamono_nf')
run('cp firamono_nf/Fira\ Mono\ Bold\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firamono_nf/Fira\ Mono\ Medium\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')
run('cp firamono_nf/Fira\ Mono\ Regular\ Nerd\ Font\ Complete.otf ' + home + '/.local/share/fonts/')

# Clean up
run('rm FiraCode.zip')
run('rm FiraMono.zip')
run('rm -r firacode_nf')
run('rm -r firamono_nf')


# -- Install zsh -- #
print_header('Installing zsh', 2, 'green')
check_and_install_pkg('zsh')
#run('mkdir ' + home + '.pyenv/shims')
#run('mkdir ' + home + '.pyenv/versions')
run('cp .zshrc ' + home)

# -- Install oh-my-zsh -- #
print_header('Installing oh-my-zsh', 3, 'green')
check_and_install_pkg('curl')
run("git clone https://github.com/ohmyzsh/ohmyzsh.git " + home + "/.oh-my-zsh")
#install_cmd = "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sed 's:env zsh::g' | sed 's:chsh -s .*$::g')\""
#run(install_cmd)


# -- Install powerlevel10k -- #
print_header('Installing powerlevel10k', 4, 'green')
run("apt-get -y install zsh-syntax-highlighting zsh-autosuggestions")
install_cmd = "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-" + home + "/.oh-my-zsh/custom}/themes/powerlevel10k"
run(install_cmd)
run('cp .p10k.zsh ' + home)


# -- Install Docker -- #
print_header('Installing Docker', 5, 'green')
run("apt-get remove docker docker-engine docker.io containerd runc")
cmd = """
 sudo apt-get -y update
 sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
"""

run(cmd)
run(" curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")

cmd = """
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
"""
run(cmd)

cmd = """
 sudo apt-get -y update
 sudo apt-get install -y docker-ce docker-ce-cli containerd.io
"""
run (cmd)

cmd = """
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
"""
run(cmd)
run("sudo chmod +x /usr/local/bin/docker-compose")


# -- Install Jetbrains Toolbox -- #
print_header('Installing Jetbrains Toolbox', 6, 'green')
run("wget https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.21.9712.tar.gz")
run("tar -xf jetbrains-toolbox-1.21.9712.tar.gz")
run("./jebtrains-toolbox-1.21.9712/jetbrains-toolbox")


# -- Install Google Chrome -- # 
print_header('Installing Google Chrome', 7, 'green')
run("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
run("sudo dpkg -i google-chrome-stable_current_amd64.deb")


# -- Install VS Code -- #
print_header('Installing VS Code', 8, 'green')
run("sudo apt install -y software-properties-common apt-transport-https wget")
run("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
run("echo | sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")
run("sudo apt -y install code")


# -- Install Flutter -- #
print_header('Installing Flutter', 9, 'green')
run("sudo apt-get -y install libglu1-mesa")
run("wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_2.2.3-stable.tar.xz")
run("mkdir " + home + "/dev")
run("sudo tar -xf flutter_linux_2.2.3-stable.tar.xz -C " + home + "/dev")
run("export PATH=\"$PATH:`pwd`/flutter/bin\"")
run("sudo chmod -R 777 " + home + "/dev")
run("flutter doctor")


# -- Generate SSH Keys for Github -- #
print_header('Generating SSH Keys For Github', 9, 'green')
run("echo | ssh-keygen -t ed25519 -C " + github_email)


# -- Install Gnome -- #
print_header('Install Gnome', 10, 'green')
run("sudo add-apt-repository ppa:shemgp/gnome-40")
run("sudo apt full-upgrade")
run("sudo apt install gnome-session adwaita-icon-theme-full fonts-cantarell")


# -- Install Discord -- #
print_header('Install Discord', 11, 'green')
run("wget -O discord-0.0.15.deb https://discordapp.com/api/download?platform=linux&format=deb")
run("sudo apt install ./discord-0.0.15.deb")


# -- Install latte-dock -- #
print_header('Install Latte Dock', 12, 'green')
run("sudo apt-get -y install latte-dock")

# -- Install spotify -- #
print_header('Install Spotify', 13, 'green')
run("""sudo curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list""")
run("sudo apt-get update && sudo apt-get install spotify-client")

# -- Install Hyper -- #
print_header('Install Hyper', 14, 'green')
run("wget -O hyper.deb https://releases.hyper.is/download/deb")
run("sudo apt install ./hyper.deb")
