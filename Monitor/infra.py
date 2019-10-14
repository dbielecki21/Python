# Dumb script to check machines for hardrive, memory, cpu issues. Notify via rocketchat.
# @author pmullen
import paramiko
import requests
import json

rocketchatUser = "sysmon"
rocketchatPw = "$yst3m-m0n!t0r"
# Recommend moving this to general when fully functioning.
rocketChatChannel = "#machine_monitor"

# Machine configs.
# example of path: '/Users/patrick.mullen/.ssh/id_rsa'
pathToKey = '/home/uberboss/.ssh/id_rsa'
# List of machine tuples with box, username, password.
# If machine uses key and not username/pw place None in username/pw sections.
machines = [("pxbox-alpha", "planx", "ChangeMe!"),
            ("pxbox-stable", "planx", "ChangeMe!"),
            ("10.0.191.192", "planx", "ChangeMe!"),
            ("centos-pxbox-dev.px.ftw", "planx", "ChangeMe!"),
            ("docker.px.ftw", "uberboss", None),
            ("ap2.px.ftw", "uberboss", None),
            # busted things is just to test ssh connection failures.
            ("bustedthings", "asad","asd")]

# Minimum thresholds to warn if things exceed.
# Note that you want to lower these thresholds to test output.
hddThreshold = 90
ramThreshold = 98
cpuThreshold = 98
memThreshold = 90

def composeMessage(machines, machineProblems, memThreshold,
                   cpuThreshold, ramThreshold, connectionFailures):
    session = requests.Session()
    # TODO hardcoded rocketchat location for blue rocketchat.
    url = "http://rocketchat.px.ftw:3000/api/v1/"
    # TODO user credentials for rocketchat.
    auth = (rocketchatUser, rocketchatPw)

    auth = session.post("{}login".format(url),
                                  data={'user': auth[0],
                                        'password': auth[1]},
                                  verify=False).text

    auth = json.load(auth)
    authToken = auth['data']['authToken']
    userId = auth['data']['userId']
    headers = {
        "X-Auth-Token": authToken,
        "X-User-Id": userId
    }

    # Make the message here.
    text = "@here"
    for machine in machineProblems:
        issues = machineProblems[machine]
        text += "\n`"+machine + "` Issues: "
        if 'hdd' in issues:
            text += "Hardrive directory:" + str(issues['hdd']['directory']) + "  at " + str(issues['hdd']['memoryUsage']) + "% capacity. "
        if 'ram' in issues:
            text += "Memory at " + str(issues['ram']) + "%. "
        if 'cpu' in issues:
            text += "CPU at " + str(issues['cpu']) + "%."
    text += "\n Machine Monitor Summary:"
    # TODO could goldplate by making the list output nicer but who cares.
    text += "\nMachines checked: `" + '` `'.join([x[0] for x in machines]) + "`\n"
    if connectionFailures:
        text += "Failed to connect to `" + ', '.join(connectionFailures) + "`\n"
    text += "Thresholds Applied: `Hdd Threshold:" + str(memThreshold) + "%` `Memory Threshold:" + str(ramThreshold) + "%` `CPU Threshold:" + str(cpuThreshold) + "%`"
    data = {
            'text': text,
            'channel': "#machine_monitor",
            'alias': "Machine Monitor",
            'emoji': ":fire:",
            'attatchments': None
        }

    r = "{}chat.postMessage".format(url)
    response = session.post(r,data, verify=False, headers = headers)







# if __name__ == "__main__":
machineProblems = {}
connectionFailures = []
for login in machines:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    currentMachine = login[0]
    currentUser = login[1]
    currentPw = login[2]
    try:
        if currentUser and currentPw:
            ssh.connect(currentMachine, username=currentUser, password=currentPw)
        else:
            ssh.connect(currentMachine,username=currentUser, key_filename=pathToKey)
        ssh_stdin,ssh_stdout, ssh_stderr = ssh.exec_command("df -h")
    except:
        print("Failed to connection to: " + currentMachine)
        connectionFailures.append(currentMachine)
        continue
    #ssh into machine
    #first line of the output is the header skip it.
    for line in ssh_stdout.readlines()[1:]:
        arrayString = line.split()
        usePercent = int(arrayString[4][:-1])
        directory = str(arrayString[5])
        if usePercent >= hddThreshold:
            # memoryProblems is a list of tuples: machine, directory, memory usage
            # need setdefault for empty list.
            memoryProblem = machineProblems.setdefault(currentMachine, {})
            memoryProblem["hdd"] = {
                "directory": directory,
                "memoryUsage": usePercent}
    cpu_command = "vmstat -S M"
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cpu_command)
    vmstatLines = ssh_stdout.readlines()
    # filter out empty strings because "" is falsey.
    vmstats = [int(x) for x in vmstatLines[2].split(" ") if x]
    # in megabyres where 1 mb = 1024 kb
    freeMemory = vmstats[3]
    usedMemory = vmstats[4]

    usedMemoryPercent = int(float(usedMemory / float(freeMemory + usedMemory)))
    cpuPercent = vmstats[12] + vmstats[13] + sum(vmstats[-2:])
    if usedMemoryPercent >= ramThreshold:
        ramProblem = machineProblems.setdefault(currentMachine, {})
        ramProblem["ram"] = usedMemoryPercent
    if cpuPercent >= cpuThreshold:
        cpuProblem = machineProblems.setdefault(currentMachine, {})
        cpuProblem["cpu"] = cpuPercent

# empty dictionaries are falsey.
if machineProblems:
    composeMessage(machines, machineProblems, memThreshold,
                   cpuThreshold, ramThreshold, connectionFailures)

