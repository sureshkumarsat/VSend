'''
PROBLEM 1
'''
def insert_number(lst, elem):
    lst.append(elem)
    return lst

def remove_number(lst, elem):
    for i in lst:
        if i==elem:
            lst.remove(elem)
            break
    return lst

def state(lst):
    homo_flag=0
    hetero_flag=0
    for i in lst:
        if lst.count(i)>=2:
            homo_flag=1
            break
    for i in lst:
        if i!=lst[0]:
            hetero_flag=1
            break
    if hetero_flag==0 and homo_flag==0:
        return "neither"
    elif hetero_flag==1 and homo_flag==0:
        return "hetero"
    elif hetero_flag==0 and homo_flag==1:
        return "homo"
    else:
        return "both"

def IsValidCommand(cmd):
    cmds = cmd.split()
    if cmds[0].lower() in ["insert", "delete"]:
        try:
            inte = int(cmds[1])
            return 1
        except:
            return "INVALID INTEGER"
    else:
        return "ENTER VALID COMMAND"

def operation(lst, lst_main):
    if lst[0].lower() == "insert":
        lst_main = insert_number(lst_main, lst[1])
    else:
        lst_main = remove_number(lst_main, lst[1])
    return lst_main

list_main = []
commands = []

n = int(input("ENTER NUMBER OF OPERATIONS : "))
i=0
res = 1
while i<n and res == 1:
    command = input("ENTER COMMAND : ")
    res = IsValidCommand(command)
    if res==1:
        commands.append([command.split()[0], int(command.split()[1])])
        i+=1
    else:
        print("ENTER VALID INPUT")
        res=1

for i in commands:
    list_main=operation(i, list_main)
    print(f"{i[0]} {i[1]}     |     {state(list_main)}")