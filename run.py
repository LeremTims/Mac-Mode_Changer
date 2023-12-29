import subprocess

def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)

mac_address_commands = [
    "ifconfig wlan0 down",
    "ifconfig wlan0 hw ether 00:11:22:33:44:55",
    "ifconfig wlan0 up"
]

monitor_mode_commands = [
    "ifconfig wlan0 down",
    "airmon-ng check kill",
    "iwconfig wlan0 mode monitor",
    "ifconfig wlan0 up",
]

# Run the first set of commands
run_commands(mac_address_commands)
print("[+] Changed MAC Address")

# Run the second set of commands
run_commands(monitor_mode_commands)
print("[+] Changed to Monitor Mode")
