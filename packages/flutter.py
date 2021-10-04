#   ___ _      _   _           
#  | __| |_  _| |_| |_ ___ _ _ 
#  | _|| | || |  _|  _/ -_) '_|
#  |_| |_|\_,_|\__|\__\___|_|  
                                                                    
from ..utilities import run, print_header                 


def install():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #
    
    # -- Stage 0: Install Necessary Packages -- #
    run('sudo apt-get -y install libglu1-mesa clang cmake ninja-build pkg-config libgtk-3-dev')


    # ========================================================== #
    #                      Section 1: Main                       #
    # ========================================================== #
    print_header('Installing Flutter')

    # -- Stage 0: Clone the Latest Stable Version -- #
    run('git clone -b stable https://github.com/flutter/flutter.git $HOME/Development')

    # -- Stage 1: Update .bashrc -- #
    # Note that if you are using zsh this will still work since .zshrc sources .bashrc 
    run('echo export PATH="$PATH:$HOME/Development/flutter/bin" >> $HOME/.bashrc')

    # -- Stage 2: Enable Linux Desktop Support -- #
    run('flutter config --enable-linux-desktop')

    # -- Stage 3: Download Dependencies -- #
    run('flutter doctor')