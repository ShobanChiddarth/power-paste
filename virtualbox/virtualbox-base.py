import os
import subprocess

def type_in_vm(string, VMname="Mint"):
    subprocess.run(["VBoxManage", "controlvm", VMname,'keyboardputstring', string])

def get_content(filepath=".content.txt", remove_indent=bool(int(os.environ.get("REMOVE_INDENT")))):
    data = []
    with open(filepath, "r") as fh:
        data[:] = fh.readlines()
    
    if remove_indent:
        data[:] = [i.lstrip() for i in data]
    
    return "".join(data)

type_in_vm(get_content())
