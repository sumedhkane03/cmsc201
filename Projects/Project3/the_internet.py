"""
File:    the_internet.py
Author:  Sumedh Kane
Date:    12/10/21
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  remaking the internet from scratch
"""
def create_server(name,address,internet):
    '''

    :param name: name of server
    :param address: ip of server
    :param internet: full internet dict
    :return: updated internet
    '''
    #print('create-server')
    address = address.split('.')
    correct_address = []
    for i in address:
        i = int(i)
        if i > 255 or i < 0:
            print('Invalid IP address please try again.')
            return 0,internet
        i = str(i)
        correct_address.append(i)
    correct_address = '.'.join(correct_address)

    #print('Server Created: ',internet[name])
    if not check_dupe(internet,name,correct_address):
        internet[name] = correct_address
        return correct_address,internet
    else:
        print("UNABLE TO CREATE SERVER {IP OR NAME ALREADY IN USE}")
        return 'UNABLE TO CREATE SERVER',internet


def traceroute(start_1, internet_1, end_1, visited_1, route=[]):
    '''

    :param start_1: starting server
    :param internet_1: internet dict
    :param end_1: ending server
    :param visited_1: visited list
    :param route: route list
    :return: route of travel
    '''
    route += [start_1]
    prev = start_1
    for i in visited_1:
        for j in range(len(visited_1[i])):
            if visited_1[i][j][0] == start_1:
                visited_1[i][j][0] = 'visited'

    #print(len(visited[start]))
    count = 0
    while count < len(visited_1[start_1]):
        if start_1 == end_1:
            return route
        elif visited_1[start_1][count][0] != 'visited':
            start_1 = visited_1[start_1][count][0]
            route += traceroute(start_1, internet_1, end_1, visited_1)
            start_1 = prev
        count += 1
    return route
'''
def traceroute(list_connections, server_destination, current_server, list_visited=[]):  # recursive
    # if(current_server != ""):
    # print(list_connections)
    #list_visited.update(current_server)
    list_visited.append(current_server)
    #print(list_visited)
    if (current_server == server_destination):
        list_visited.append()
        #print(list_visited)
        return list_visited
    else:
        for i in list(list_connections[current_server].keys()):
            if i == server_destination:
                list_visited.append(current_server)
            if (i not in list_visited):
                return traceroute(list_connections, server_destination, i, list_visited)
    return list_visited
'''
def ping(route,connections):
    '''

    :param route: list of route
    :param connections: connections dict
    :return:  total time
    '''
    ms = 0
    print(route,connections)
    '''
    for i,j in enumerate(route):
        for k in connections[i]:
            if j+1 < len(route):
                if k[0] == route[j+1]:
                    ms += k[1]
    '''

    return ms



def check_dupe(internet,name,addy):
    '''

    :param internet: full internet dict
    :param name: name of server
    :param addy: ip of server
    :return: true or false
    '''
    for i in internet.keys():
        if internet[i] == addy or i == name:
            return True
    return False


def create_connection(internet,start,to,pingtime,connections):
    '''

    :param internet: full internet dict
    :param start: starting server
    :param to: ending server
    :param pingtime: ping time in ms
    :param connections: full connections dict
    :return: updated connections dict
    '''
    if start in connections.keys():
        if to not in connections[start]:

            if start in internet.keys() and to in internet.keys():
                connections[start].append([to,pingtime])
                connections[to].append([start,pingtime])
                print('Connection Created.')
            else:
                print('one or more servers dont exist')
    elif to in connections.keys():
        if start not in connections[to]:
            if start in internet.keys() and to in internet.keys():
                connections[start].append([to,pingtime])
                connections[to].append([start,pingtime])
                print('Connection Created.')
            else:
                print('one or more servers dont exist')
    else:
        if start in internet.keys() and to in internet.keys():
            connections[start].append([to, pingtime])
            connections[to].append([start, pingtime])
            print('Connection Created.')
        else:
            print('one or more servers dont exist')

    return connections

# def set_server(internet):
#     print('set-server')


def ip_config(internet,internetvalues,current_server):
    '''

    :param internet: full internet dict
    :param internetvalues: values in internet dict
    :param current_server: current server name or IP
    :return: nothing
    '''
    if current_server in internet:
        print('Current Server: \n Name:',current_server,'\n IP: ',internet[current_server])
    elif current_server in internetvalues:
        for i in internet:
            if internet[i] == current_server:
                a = i
        print('Current Server: \n Name:', a, '\n IP: ', current_server)

def display_servers(internet):
    '''

    :param internet: full internet dict
    :return: nothing
    '''
    print(' ')
    for i in internet:
        print(f"Server Name: {i} \nServer IP: {internet[i]} \n")
    #print('display-servers')
    return 'done'



def pick_command(command):
    '''

    :param command: the command given by the user
    :return: the command to pick
    '''
    command = command.split()
    valid = False
    while valid == False:
        if command[0].lower() == 'create-server' or command[0].lower() == 'cs':
            return 1, command
            valid = True
        elif command[0].lower() == 'create-connection' or command[0].lower() == 'cc':
            return 2, command
            valid = True
        elif command[0].lower() == 'set-server' or command[0].lower() == 'ss':
            return 3, command
            valid = True
        elif command[0].lower() == 'traceroute' or command[0].lower() == 'tr' or command[0].lower() == 'tracert':
            return 4, command
            valid = True
        elif command[0].lower() == 'ip-config' or command[0].lower() == 'ipconfig':
            return 5, command
            valid = True
        elif command[0].lower() == 'display-servers' or command[0].lower() == 'ds':
            return 6, command
            valid = True
        elif command[0].lower() == 'ping':
            return 7, command
            valid = True
        else:
            return 'invalid'

def blankConnections(internet,connections):
    '''

    :param internet: whole internet dict
    :param connections: all the connections in the internet dictionary
    :return: updated connections
    '''
    for i in internet:
        if i not in connections:
            connections[i] = []
    return connections

def displayRoute(fullRoute):
    '''

    :param fullRoute: full route given from traceroute function
    :return: printable route
    '''
    printRoute = [fullRoute[0]]
    del fullRoute[0]
    for i in fullRoute:
        if i not in printRoute:
            printRoute.append(i)
    print(*printRoute,sep=' --> ')
    return printRoute

def convertIPtoName(ip,internet):
    '''

    :param ip: the ip address to convert
    :param internet: whole internet dict
    :return: name of server
    '''
    keys = list(internet.keys())
    addresses = list(internet.values())
    for i in range((len(addresses))):
        if addresses[i] == ip:
            return keys[i]

def run_the_internet():
    '''

    :return: runs the whole internet
    '''
    internet = {'sumedh': '0.5.1.7', 'avadhoot': '0.8.0.7', 'aai': '0.9.0.3', 'baba': '1.0.2.4', 'parle': '4.0.5.7', 'deonar': '1.1.1.1'}
    connections = {'sumedh': [['avadhoot', '1']], 'avadhoot': [['sumedh', '1'], ['aai', '1']], 'aai': [['avadhoot', '1'], ['baba', '1'], ['deonar', '1']], 'baba': [['aai', '1'], ['parle', '1']], 'parle': [['baba', '1']], 'deonar': [['aai', '1']]}

    valid = False
    #print(pick_command(input("Enter command: ")))
    current_server = ''
    given = input("Enter command: ")
    if given!= 'quit' and pick_command(given) == 'invalid:':
        given = input("Enter command: ")

    while given.lower() != 'quit':
        internetvalues = []
        for i in internet.keys():
            internetvalues.append(internet[i])
        picked = pick_command(given)
        #picked = pick_command('create-server sumedh.com 144.100.32.5')
        command = picked[1]
        if picked[0] == 1:
            #create_server(command[1], command[2], internet)
            internet = (create_server(command[1], command[2], internet))[1]
            connections = blankConnections(internet,connections)
            #print(internet)
            given = input("Enter command: ")
        elif picked[0] == 2:
            #print(command)
            create_connection(internet,command[1],command[2],command[3],connections)
            given = input("Enter command: ")
        elif picked[0] == 3:
            #set_server(internet)
            #print(picked)
            if len(internet) > 1:
                if picked[1][1] in internet.keys():
                    current_server = picked[1][1]
                    print(f"Current Server: {current_server}")
                elif picked[1][1] in internetvalues:
                    current_server = convertIPtoName(picked[1][1],internet)
                    print(f"Current Server: {current_server}")
                else:
                    print(f"Server does not exist")
            else:
                print(f"Server does not exist")


            given = input("Enter command: ")
        elif picked[0] == 4:

            if picked[1][1] in connections or picked[1][1] in internet.values():
                if picked[1][1] in internet.values():
                    end = convertIPtoName(picked[1][1],internet)
                else:
                    end = picked[1][1]
                visited = dict(connections)
                copyofinternet = dict(internet)
                fullRoute = traceroute(current_server,copyofinternet,end,visited)
                displayRoute(fullRoute)
                visited = dict(connections)
                fullRoute = []
            given = input("Enter command: ")
        elif picked[0] == 5:
            if current_server in internet.keys() or current_server in internetvalues:
                ip_config(internet,internetvalues,current_server)
            else:
                print('Please set an existing current server')
            given = input("Enter command: ")
        elif picked[0] == 6:
            display_servers(internet)
            print(connections)
            given = input("Enter command: ")
        elif picked[0] == 7:
            print(picked)
            if picked[1][1] in connections:
                visited = dict(connections)
                copyofinternet = dict(internet)
                ping(displayRoute(traceroute(current_server,copyofinternet,picked[1][1],visited)),connections)
            given = input("Enter command: ")
        else:
            given = input("Enter command: ")
    print('INTERNET: ',internet)
    print('CONNECTIONS: ',connections)



if __name__ == '__main__':
    run_the_internet()
