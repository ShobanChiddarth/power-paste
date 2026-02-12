import subprocess

def type_in_vm(string, VMname="Mint"):
    subprocess.run(["VBoxManage", "controlvm", VMname,'keyboardputstring', string])

def get_content(filepath=".content.txt"):
    with open(filepath, "r") as fh:
        return fh.read().strip()

type_in_vm(get_content())
