# Bug Bounty Report

**Reported by:** MiiAndYuu  
**Date:** 2023-10-05

## Summary:

I have identified and successfully exploited vulnerabilities in the target system, resulting in unauthorized access and the retrieval of sensitive data, including user and root flags.

## Vulnerability Details:

### Vulnerability Title: Unauthorized Access and Data Retrieval
- **Severity:** Critical
- **Description:** 
  - I was able to exploit a vulnerability in the Samba service running on ports 139 and 445, using the `exploit/multi/samba/usermap_script` module. This allowed me to gain unauthorized access to the target system.
  - Subsequently, I was able to retrieve the user flag located at `/home/makis/` and the root flag located at `/root/`.
- **Impact:**
  - Unauthorized access to the system.
  - Unauthorized access to sensitive user and root data.

## Steps to Reproduce:

1. Use the Metasploit module `exploit/multi/samba/usermap_script` to exploit the target system.
2. Gain access to the command shell.
3. Navigate to the `/home/makis/` and `/root/` directories to retrieve the user and root flags.

## Additional Information:

- **Affected System:** 
  - Enumeration Result:
    ```
    PORT    STATE SERVICE     VERSION
    21/tcp  open  ftp         vsftpd 2.3.4
    22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
    139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp open  �
                   ^�zU      Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
    ```
- **Proof of Exploitation:** 
  - [Documentation.md](./documentation.md)

## Disclosure Timeline:

- 2023-10-05: Initial discovery of the vulnerability.
- 2023-10-05: Successful exploitation and retrieval of flags.
- 2023-10-05: Submission of this bug bounty report.

## Disclaimer:

This report is submitted as part of a responsible disclosure process. The intention is to assist in improving the security of the affected system. I acknowledge that unauthorized access and exploitation of vulnerabilities can have legal consequences, and I have conducted this assessment within the boundaries of the law and with proper authorization.