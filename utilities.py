import functools, subprocess
from subprocess import CalledProcessError


run = functools.partial(subprocess.run, shell=True)


 # check if pip is installed
try: 
  subprocess.run('which pip', shell=True, check=True)
except CalledProcessError:
  run('apt-get -y install python3-pip')
  import pip


# function to check if a package exist, if it doesn't we will install it
# note: ImportError is a subclass of ModuleNotFoundError
def install_pkg(package):
    try:
      __import__(package)
    except ImportError:
      pip.main(['install', package])

install_pkg('termcolor')
from termcolor import colored


def get_user_input(msg):
  while True:
    try:
      ret = input(msg)
    except ValueError:
      print("\nSorry, I didn't understand that!\n")
      continue
    else:
      break
  return ret


def print_header(msg):
  print('\n')
  print(colored(msg, 'green', attrs=['bold']))
  print('\n')


def run_and_capture(cmd):
  ret = subprocess.run(cmd, shell=True, capture_output=True)
  return ret.stdout.decode('utf-8').replace('\n', '')