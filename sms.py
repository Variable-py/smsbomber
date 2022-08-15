import os

os_type = os.name
if os_type != 'nt':
    os.system("apt install tor")
    os.system("apt install torsocks")
    os.system("pkg install python")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("torsocks python smsBomber.py")
else :
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("python smsBomber.py")