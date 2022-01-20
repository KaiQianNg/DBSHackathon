import sys, subprocess

install_output = subprocess.check_output([sys.executable,'-m', 'pip', 'install', '-r', 'requirements.txt'])
print(install_output)