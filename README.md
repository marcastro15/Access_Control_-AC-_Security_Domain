# Access_Control_-AC-_Security_Domain

Purpose:
--------
This is an Access Control (AC) security tool that will enable to determine the authorized personnel. All authorized personnel are stored and managed by Human Resources (HR). All employees must be entered to the HR Systems after hiring process. The HR system database list all the employees who will specific access to an specific systems. That means, it's the only authorized individual. The sole authority is the HR System, not the Linux/Windows or any OS Administrators. This will prevent rogue employees to make entries into the systems without authorization from HR. This is relevant in the real world because Security Operation Center (SOC) should constantly watch and oversee all the activities of the employees regardless of their roles in the company. 


Required Knowledge/Pre-requisites/Installation:
-------------------
- Linux Admin (Ubuntu)- basic network administration and commands
- Windows Admin (Windows 10) - basic network administration and commands
- SSH instruction: install SSH Server on each hosts you're interested in
    + https://www.cyberciti.biz/faq/ubuntu-linux-install-openssh-server/
- Python3 Syntax - This is not compatible to Python version 2
- Public/private key SSH setup Instruction: 
    + https://www.ssh.com/academy/ssh/keygen for setup instruction 
    + How to copy keys? ssh-copy-id -i ~/.ssh/id_rsa.pub username(s)@ip(s)
- MySQL Server and SQL
    + How to install MySQL Tutorial: 
        - https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
        - https://www.mysqltutorial.org/mysql-create-database/
    + Test your MySQL to make sure it's running: systemctl status mysql.service
        - CREATE DATABASE AND TABLES:
          1. sudo mysql
          2. create user 'username' identified by 'password'
          3. GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'username' WITH GRANT OPTION;
          4. mysql -u 'username' -p 'password'
          5. DATABASE: create database HR_DB;
          6. SPECIFY DATABASE TO USE: use HR_DB;
          7. TABLE: create table HR_EMPLOYEES(username varchar(100), primary key(username));
          8. INSERT AUTHORIZED USER DATA: insert into HR_EMPLOYEES(username) values ('mar');

 INSTALL MODULES
 ---------------
 Note that pip3 means install it in python version 3
 - UPDATE S/W Source: apt-get update 
- PIP: 
    + PIP for python3: apt install python3-pip
    + COLOR: pip install string-color
    + MYSQL CONNECTOR: pip3 install mysql-connector-python


DESIGN:
------
 This is a multi-tier (2) application that requires database and an application.
 DATABASE <-------------->PYTHON APPLICATION

RUNNING
-------
python3 AC.py

Demo: https://youtu.be/3MQxS6LhAGc

Future Work:
-----------
1. This program is designed to compare authorized users on Linux systems only. It would be extended to Windows and other operating systems.
2. The results will be sent to Security Operation Center (SOC)
3. Create GUI web interface to display data. 
4. Redesign the DB to identify which employees are supposed to have access to specific hosts.

