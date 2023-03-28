import os

def update_system():
    # Running apt-get
    os.system("sudo apt-get update && sudo apt-get upgrade -y")

# It will run the commands inside the function to update the Linux system.
update_system()
