import napalm
from pprint import pprint

driver = napalm.get_network_driver("ios")


csr1 = driver(
    hostname="clab2.broccoli.rocks",
    username="admin",
    password="2OnthEatwaHoj",
    optional_args={"port": 62002},
)


print()
print("=== setup connection ===")
print()

csr1.open()

print()
print("=== get facts ===")
print()

output = csr1.get_facts()
pprint(output)

print()
print("=== end ===")
print()
