 #   _  _                    
 #  | || |_  _ _ __  ___ _ _ 
 #  | __ | || | '_ \/ -_) '_|
 #  |_||_|\_, | .__/\___|_|  
 #        |__/|_|                                          
                                                                                                            
from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #                      Section 0: Main                       #
    # ========================================================== #
    print_header('Installing Hyper')
    run('wget https://releases.hyper.is/download/deb -O tmp/hyper.deb')
    run('sudo apt-get -y install tmp/hyper.deb')