import os

#file name and script name
file_name = "test"
script_name = "test.sh"

# Creating the file and adding the script to it
os.system(f"touch {file_name} && echo '#!/bin/bash\necho \"Hello, world!\"' > {file_name}/{script_name}")
