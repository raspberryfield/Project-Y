# SFTP  

## Links  
- How to setup a SFTP-server in normal cases: [https://linuxhint.com/setup-sftp-server-ubuntu/](https://linuxhint.com/setup-sftp-server-ubuntu/).  

## Tips  
See if the ssh server is running:  
`$ service ssh status`  
List all groups on the system:  
`$ cat /etc/group`  
List all groups of a user:  
`$ groups <user_name>`  
Open a sftp session:  
`$ sftp sftp_user@localhost`
