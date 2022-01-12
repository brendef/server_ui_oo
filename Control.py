import shlex
import subprocess
import paramiko

class Control:

    # Constructor
	# ------------------------------------------------------------------------------------ #

    def __init__(self, database):
        self.database = database

    # ------------------------------------------------------------------------------------ #

    def System(Command):
        Cmds = shlex.split(Command," ")

        Output = "~output~"
        p = subprocess.Popen(
            Cmds,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        Output = p.communicate()

        try:
            Output = Output[0].decode()
        except:
            pass

        return str(Output)
    
    # ------------------------------------------------------------------------------------ #

def SystemRemote(command):
    host = str(data.get_host()[0])
    user = str(data.get_user()[0])
    pem = str(data.get_pem_address()[0])
    output = ''
    client = ssh(host, user, pem)
    stdin , stdout, stderr = client.exec_command(command)
    for line in stdout:
        output=output+line
    return output

# Firewall functions

def get_open_ports():
    Status = dict()
    Sl = System("sudo ufw status")[104:].split("\n")

    for S in Sl:
        S2 = S.split()
        try:
            Sport = S2[0].split("/")[0]
        except:
            Sport = ""
        try:
                Sopen = S2[1]
        except:
            Sopen= ""
       
        if not "(v6)" in S and len(Sport)>1:
            if Sopen in ["ALLOW"]:
                Open = 1
            else:
                Open = 0
            Status[Sport] = Open

    return Status

def boolean_firewall(firewallStatus):
    if firewallStatus == 'active':
        return True
    else:
        return False
    
def enable_firewall():
        System("echo y | sudo ufw enable")

def disable_firewall():
        System("sudo ufw disable")

def get_ufw_status():
    return System("sudo ufw status").split()[1]

def get_ufw_status_boolean():
    return System("sudo ufw status").split()[1]

def enable_port(port):
    System("sudo ufw allow {}".format(port))

def disable_port(port):
    System("sudo ufw deny {}".format(port))

def is_ufw_enabled():
    if System("sudo ufw status").split()[1] == 'active':
        return True
    else:
        return False

def is_ufw_disabled():
    if System("sudo ufw status").split()[1] == 'inactive':
        return True
    else:
        return False

# PIP Package install functions
def pip_install(Package):  
	System("pip3 install --upgrade " + Package)
	System("pip3 show "+Package)

# APT Package install functions
def apt_install(Package):  
	System("sudo apt-get -y install " + Package)

# SSH
# def ssh(host, user, pem):
#     System("sudo ssh -t {} {}@{}".format(pem, user, host))

def ssh(host, user, pem):
    key = paramiko.RSAKey.from_private_key_file(pem)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = host, username = user, pkey = key)
    return client

def mkdir(filename):
    System("mkdir {}".format(filename))