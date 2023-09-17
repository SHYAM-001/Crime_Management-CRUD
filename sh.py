import subprocess
import os

os.chdir('sherlock/sherlock')


# The command to run
# command = f'sherlock --timeout 1 kathirarts'

name="kathirarts"
command=f'python sherlock --timeout 1 {name}'
# Run the command in a subprocess
result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)

# Print the result
print(result.stdout)
path=f'{name}.txt'
os.startfile(path)
