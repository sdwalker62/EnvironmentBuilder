#         _    
#   _____| |_  
#  |_ (_-< ' \ 
#  /__/__/_||_|
             
from ..utilities import run, print_header, install_pkg                    


def exec_stage():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #
    install_pkg('shutil')
    import shutil

    # ========================================================== #
    #                      Section 1: Main                       #
    # ========================================================== #
    print_header('Installing zsh')

    # -- Stage 0: Install zsh -- #
    run('sudo apt-get -y install zsh')
    
    # -- Stage 1: Install Oh-My-Zsh -- #
    run('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

    # -- Stage 2: Install Powerlevel10k -- #
    run('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')

    # -- Stage 3: Install Plugins -- #
    run('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    run('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')

    # -- Stage 4: Move Dotfiles -- #
    shutil.copy(src='./dotfiles/.zshrc', dst='$HOME/')
    shutil.copy(src='./dotfiles/.p10k.zsh', dst='$HOME/')

    # -- Stage 5: Change Shell -- #
    run('sudo chsh -s $(which zsh)')
    run('source $SHELL')