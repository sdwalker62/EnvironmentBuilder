 #   _ __ _  _ ___ _ ___ __
 #  | '_ \ || / -_) ' \ V /
 #  | .__/\_, \___|_||_\_/ 
 #  |_|   |__/             

from ..utilities import run, print_header                 


def exec_stage():

    # ========================================================== #
    #              Section 0: Install Prerequisites              #
    # ========================================================== #
    cmd = """sudo apt-get -y install\
    make\ 
    build-essential\ 
    libssl-dev\
    zlib1g-dev\
    libbz2-dev\
    libreadline-dev\
    libsqlite3-dev\
    wget\
    curl\
    llvm\
    libncursesw5-dev\
    xz-utils\
    tk-dev\
    libxml2-dev\
    libxmlsec1-dev\
    libffi-dev\
    liblzma-dev"""
    run(cmd)
    run('sudo apt-get -y install curl')


    # ========================================================== #
    #                      Section 1: Main                       #
    # ========================================================== #
    print_header('Installing pyenv')
    run('curl https://pyenv.run | bash')