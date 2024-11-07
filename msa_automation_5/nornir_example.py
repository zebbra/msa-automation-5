from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result
from nornir_scrapli.tasks import send_command


nr = InitNornir(
    inventory={
        "plugin": "SimpleInventory",
        "options": {
            "host_file": "inventory/hosts.yaml",
            "group_file": "inventory/groups.yaml",
        },
    },
)

print(nr.inventory.hosts)


def hello_world(task: Task) -> Result:
    return Result(host=task.host, result=f"{task.host.name} says hello world!")


result = nr.run(task=hello_world)
print_result(result)

command_results = nr.run(task=send_command, command="show version")
print_result(command_results)
