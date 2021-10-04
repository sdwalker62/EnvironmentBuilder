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
    print_header('Installing fonts')

    # -- Stage 0: Make Directories -- #
    run('mkdir firacode_nf')
    run('mkdir firamono_nf')
    run('mkdir $HOME/.local/share/fonts')

    # -- Stage 1: Install FiraCode NerdFont -- #
    run('wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraCode.zip -P firacode_nf')
    run('unzip firacode_nf/FiraCode.zip -d firacode_nf')

    run('cp firacode_nf/Fira\ Code\ Bold\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp firacode_nf/Fira\ Code\ Light\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp firacode_nf/Fira\ Code\ Medium\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp firacode_nf/Fira\ Code\ Regular\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')
    run('cp firacode_nf/Fira\ Code\ Retina\ Nerd\ Font\ Complete.otf $HOME/.local/share/fonts/')

    run('sudo fc-cache -fv')

    # -- Stage 2: Clean-up -- #
    run('rm -r firacode_nf')
    run('rm -r firamono_nf')