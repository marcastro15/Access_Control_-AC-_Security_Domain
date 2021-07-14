import paramiko
import mysql.connector
from stringcolor import *
from mysql.connector import errorcode

#Future work - store these somewhere
hostnames=['192.168.125.130','192.168.125.132','192.168.125.134','192.168.125.133']

# declare testing credentials   
# you can change this to store it that is not accessible by unauthorized users
username = 'fabric'
password = 'r00t'

def initiate_DB(u):
    #print('DB initiated...')
    username=u
    mydb = mysql.connector.connect(user='mar', password='mar', host='127.0.0.1', database='HR_DB')

    cursor = mydb.cursor()
    query = ('SELECT count(*) from HR_EMPLOYEES where username='+'\''+username+'\'')
    cursor.execute(query)
    rows=cursor.fetchone()
    print(rows)
    for rr in rows:
        if rr == 1:
            return cs("AUTHORIZED PERSONNEL...","orchid")
        else:
            return cs("unauthorized user","red")


def get_usernames(host):
    # connect to server   
    con = paramiko.SSHClient()
    con.load_system_host_keys()
    con.connect(host, username=username, password=password)

    # run the command   
    # use the -1 argument so we can split the files by line   
    stdin, stdout, stderr = con.exec_command('awk -F: \'{ print $1}\' /etc/passwd')

    # process the output   
    if stderr.read() == b'':
        for line in stdout.readlines():
            print(host+':'+str(line.strip())+' '+str(initiate_DB(line.strip())))
    else:
        print(stderr.read())

for computers in hostnames:
    print('\n')
    print('---->'+computers)
    get_usernames(computers)
