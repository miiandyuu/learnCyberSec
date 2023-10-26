# Bug Bounty Report

## Bug Details
- **Reported By**: miiandyuu
- **Date**: 10/26/2023
- **Severity**: Critical
- **Status**: Open

## Bug Description
The target system, identified with IP address 10.10.10.152, has multiple security vulnerabilities that could lead to unauthorized access and control over the system. The vulnerabilities include anonymous FTP access, information leakage, and a critical Remote Code Execution (RCE) vulnerability in the PRTG Network Monitor version 18.2.38.

## Steps to Reproduce
1. Use the following Nmap command to scan the target system:
`nmap -sC -sV -A 10.10.10.152`

2. Observe the open ports and services, including:
- FTP with anonymous login enabled.
- HTTP service running PRTG Network Monitor.
- Microsoft Windows RPC, netbios-ssn, and Microsoft Windows Server services.

3. Access the FTP server and list the directory contents. You can find sensitive information, including the PRTG Network Monitor configuration file.

4. Authenticate into the PRTG Network Monitor web application using the credentials:
- Username: prtgadmin
- Password: PrTg@dmin2019 (based on the date of the configuration file)

5. Confirm the version of PRTG Network Monitor as 18.2.38.

6. Exploit the RCE vulnerability using the provided script `netmon-exploit.sh` and cookies. This script creates a new user with credentials pentest:P3nT3st!.

7. After creating the new user, use Impacket to execute remote commands on the target system.

## Expected Behavior
The expected behavior is that the target system should have secure configurations and should not allow unauthorized access via anonymous FTP or contain vulnerabilities that allow RCE.

## Actual Behavior
The actual behavior is that the target system has multiple vulnerabilities, including anonymous FTP access, information leakage, and an RCE vulnerability in the PRTG Network Monitor, which allowed unauthorized access to the Windows system as an admin.

## Vulnerability Impact
The identified vulnerabilities have a severe impact, as they could lead to unauthorized access, data theft, and complete control over the target system. The RCE vulnerability, in particular, poses a significant security risk.

## Proof of Concept
- Proof of concept code and details can be found in the provided script `netmon-exploit.sh`.
- The specific details of the PRTG Network Monitor RCE can be found at [Exploit-DB](https://www.exploit-db.com/exploits/46527).

## Affected Components
- Anonymous FTP
- PRTG Network Monitor version 18.2.38

## Recommendations
1. Disable anonymous FTP access on the target system.
2. Update the PRTG Network Monitor to the latest version to patch the RCE vulnerability.
3. Conduct a thorough security audit of the system to identify and address other potential vulnerabilities.

## Additional Information
- The target system is running Windows Server 2008 R2 - 2012.
- Use caution and obtain proper authorization before attempting any further exploitation.

## Contact Information
- **Reported By**: miiandyuu

## Terms and Conditions
- This report is submitted in compliance with the terms and conditions of the bug bounty program.
- The information provided in this report should be handled confidentially and not disclosed to unauthorized parties.
- The actions performed during the testing were within the scope of the bug bounty program and with the proper authorization.