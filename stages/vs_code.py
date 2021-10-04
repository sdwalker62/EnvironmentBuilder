 #  __   _____    ___         _     
 #  \ \ / / __|  / __|___  __| |___ 
 #   \ V /\__ \ | (__/ _ \/ _` / -_)
 #    \_/ |___/  \___\___/\__,_\___|
                                                                                                                                                           
from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #

    # -- Stage 0: Install Packages -- #
    run("sudo apt install -y software-properties-common apt-transport-https wget")

    # -- Stage 1: Add GPG Key -- #
    run("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")

    # -- Stage 2: Add Repository -- #
    run("echo | sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")


    # ========================================================== #
    #                      Section 0: Main                       #
    # ========================================================== #
    print_header('Installing VS Code')
    run("sudo apt -y install code")
