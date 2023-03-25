import os
import webbrowser

# will list partitions on your system
partitions = [partition.device for partition in os.popen('lsblk -lnp -o NAME').read().strip().split('\n')[1:]]
print("Partitions on this PC:")
print(partitions)

# will open YouTube
url = "https://www.youtube.com/"
webbrowser.open(url)
