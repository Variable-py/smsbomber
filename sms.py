import os

os_type = os.name
if os_type != 'nt':
    os.system("pkg install python")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("python smsBomber.py")
else :
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("python smsBomber.py")