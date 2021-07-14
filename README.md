# Access_Control_-AC-_Security_Domain

Purpose:
dfadf

Description:
dfadf

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
 - PIP: apt install python3-pip
 - UPDATE S/W Source: apt-get update 
 
RUNNING
-------
python3 AC.py


Future Work:
dfasdf

