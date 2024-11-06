from scrapli.driver.core import IOSXEDriver
from pprint import pprint

my_device = {
    "host": "clab2.broccoli.rocks",
    "auth_username": "admin",
    "auth_password": "2OnthEatwaHoj",
    "auth_strict_key": False,
    "port": 62002,
}


csr1 = IOSXEDriver(**my_device)
csr1.open()
response = csr1.send_command("show version")
structured_result = response.textfsm_parse_output()
pprint(structured_result)
