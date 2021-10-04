#   ___        _      
#  | __|__ _ _| |_ ___
#  | _/ _ \ ' \  _(_-<
#  |_|\___/_||_\__/__/
                    
from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #
    run('sudo apt-get -y install wget')


    # ========================================================== #
    #                      Section 1: Main                       #
    # ========================================================== #
    print_header('Installing Fonts')

    # -- Stage 0: Make Directories -- #
    run('mkdir $HOME/.local/share/fonts')

    # -- Stage 1: Install FiraCode NerdFont -- #
    run('wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraCode.zip -P tmp')
    run('unzip tmp/FiraCode.zip -d tmp')

    run('cp tmp/Fira\ Code\ Bold\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp tmp/Fira\ Code\ Light\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp tmp/Fira\ Code\ Medium\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp tmp/Fira\ Code\ Regular\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp tmp/Fira\ Code\ Retina\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')

    run('sudo fc-cache -fv')