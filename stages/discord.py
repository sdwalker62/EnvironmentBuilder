#   ___  _                   _ 
#  |   \(_)___ __ ___ _ _ __| |
#  | |) | (_-</ _/ _ \ '_/ _` |
#  |___/|_/__/\__\___/_| \__,_|                                
                                                                                                            
from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #                      Section 0: Main                       #
    # ========================================================== #
    print_header('Installing Discord')
    run('wget https://discord.com/api/download?platform=linux&format=deb -O tmp/discord.deb')
    run('sudo dpkg -i tmp/discord.deb')