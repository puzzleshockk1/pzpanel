from subprocess import call
import time
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    GREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 40)

print(f'''
{bcolors.GREEN}
██████╗░██╗░░░██╗███████╗███████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░██║╚════██║╚════██║██║░░░░░██╔════╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║░░░██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░  ╚█████╗░███████║██║░░██║██║░░╚═╝█████═╝░
██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║░░██║██║░░██╗██╔═██╗░
██║░░░░░╚██████╔╝███████╗███████╗███████╗███████╗  ██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
''')

slowprint(
    f"{bcolors.GREEN}Welcome to PUzHxZ Panel"
)
print("\nPrograms\n---------------")
time.sleep(0.4)
print("1. Ddoser(Layer 7 - POST) │  2. SMS Sender")
time.sleep(0.4)
print("3. Google Account Phisher │  4. Ip pinger")
time.sleep(0.4)
print("5. Discord channel nuker  │  6. Social media Username checker ")
print("7. More\n---------------")



def replux():
    while True:
        command = input(f"{bcolors.GREEN}$ ")
        #sms
        if command == "2":
            call(["python", "programs/sms.py"])
            return replux()
        #ddos
        if command == "1":
            call(["python", "programs/ddos.py"])
        #phisher
        if command == "3":
            call(["python", "programs/phisher/phish.py"])
        #ip ping
        elif command == "4":
            call(["python", "programs/ping.py"])
                    #discord nuker
        elif command == "5":
            call(["python", "programs/nuker.py"])
        elif command == "6":
            call(["python", "programs/usercheck/user.py"])


        #just an enter
        elif command == "":
            replux()
        #when wrong
        else:
            print("no command found: " + command +
                  "'\nUse please try again")


replux()