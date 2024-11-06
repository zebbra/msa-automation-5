from netmiko import ConnectHandler
from pprint import pprint

csr1 = {
    "device_type": "cisco_ios",
    "host": "clab2.broccoli.rocks",
    "username": "admin",
    "password": "2OnthEatwaHoj",
    "port": 62002,
    "secret": "2OnthEatwaHoj",
    "session_log": "csr1.log"
}

csr2 = {
    "device_type": "cisco_ios",
    "host": "clab2.broccoli.rocks",
    "username": "admin",
    "password": "2OnthEatwaHoj",
    "port": 62003,
    "secret": "2OnthEatwaHoj",
    "session_log": "csr2.log"
}
print()
print("=== setup connection ===")
print()

net_connect = ConnectHandler(**csr1)

print()
print("=== execute command ===")
print()


output = net_connect.send_command("show ip int brief")

print(output)

print()
print("=== execute command, parsed with textfsm ===")
print()


command = "show ip int brief"
output = net_connect.send_command(command, use_textfsm=True)

pprint(output)

print()
print("=== make configuration ===")
print()


commands = ["logging buffered 100000"]
output = net_connect.send_config_set(commands)
output += net_connect.save_config()

print()
print("=== end ===")
print()