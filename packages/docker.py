 #   ___          _           
 #  |   \ ___  __| |_____ _ _ 
 #  | |) / _ \/ _| / / -_) '_|
 #  |___/\___/\__|_\_\___|_|  
                                        
from ..utilities import run, print_header                 


def install():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #
    
    # -- Stage 0: Install Necessary Packages -- #
    cmd = """sudo apt-get install\
     apt-transport-https\
     ca-certificates\
     curl\
     gnupg\
     lsb-release"""
    run(cmd)

    # -- Stage 1: Add Docker's Official GPG Key -- #
    run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')

    # -- Stage 2: Add the Stable Docker Repository -- #
    cmd = """echo\
     "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu\
     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"""
    run(cmd)


    # ========================================================== #
    #                      Section 1: Main                       #
    # ========================================================== #
    print_header('Installing Docker')

    # -- Stage 0: Install Docker Engine -- #
    run('sudo apt-get update')
    run('sudo apt-get -y install docker-ce docker-ce-cli containerd.io')

    # -- Stage 1: Install Docker-Compose -- #
    run('sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    run('sudo chmod +x /usr/local/bin/docker-compose')