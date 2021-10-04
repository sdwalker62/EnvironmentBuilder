#   ___           _   _  __      
#  / __|_ __  ___| |_(_)/ _|_  _ 
#  \__ \ '_ \/ _ \  _| |  _| || |
#  |___/ .__/\___/\__|_|_|  \_, |
#      |_|                  |__/                                         
                                                                                                            
from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #                      Section 0: Main                       #
    # ========================================================== #
    print_header('Installing Spotify')

    # -- Stage 0: Add GPG & Repository -- #
    run("""sudo curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
    echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list""")

    # -- Stage 1: Install Spotify -- #
    run('sudo apt-get update')
    run('sudo apt-get -y install spotify-client')