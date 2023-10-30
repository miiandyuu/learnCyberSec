# Bug Bounty Report

## Bug Details
- **Reported by**: miiandyuu
- **Date**: 10/30/2023

## Bug Description
A security vulnerability was discovered on a website still under development, accessible at `http://209.97.140.29:32753`. This report focuses on an Authentication Bypass vulnerability that allows unauthorized access to the system.

## Steps to Reproduce
1. Access the website at `http://209.97.140.29:32753`.
2. Register for an account and log in.
3. Observe the Authentication Bypass, which allows unauthorized access.

## Expected Behavior
After successful login, the user should access the system as an authenticated user with appropriate privileges.

## Actual Behavior
After logging in, unauthorized access is granted due to the Authentication Bypass vulnerability.

## Vulnerability Impact
The Authentication Bypass vulnerability can have a significant impact:
- Unauthorized access to user data.
- Potential data leakage.
- Risk of unauthorized actions on behalf of authenticated users.

## Proof of Concept
1. Investigation revealed an Authentication Bypass vulnerability on the website.
2. An Authentication Bypass in the `jsonwebtoken` package was identified in versions `<4.2.2` (CVE-2015-8315).
3. The following steps were taken to demonstrate the vulnerability:
   - Logged in to the website using Chrome and inspected the JWT token.
   - Decoded the token using [jwt.io](https://jwt.io/) to obtain the public key.
   - Used `jwt_tool` ([GitHub Repository](https://github.com/ticarpi/jwt_tool)) to inject a payload.
   - Executed a payload similar to:
     ```
     python3 ./jwt_tool.py $(cat UnderConstruction/token) -I -pc username -pv "test2' and 1=0 union all select 1, group_concat(sql), 1 from sqlite_master--" -X k -pk UnderConstruction/keyPublic.pem
     ```
   - Due to the lack of sanitation on the backend, the SQL query was successfully injected, potentially exposing database information.

## Recommendations
To address the Authentication Bypass vulnerability, the following steps should be taken:
- Update the `jsonwebtoken` package to a version greater than or equal to `4.2.2` to fix the Authentication Bypass vulnerability.
- Implement proper input validation and sanitation for all raw queries in the code to prevent SQL Injection attacks.
- Review and revise the authentication and authorization processes to ensure secure access control.

## Contact Information
- **Reporter's GitHub**: miiandyuu

## Terms and Conditions
Please note that this report is subject to the terms and conditions of the bug bounty program, and all findings and details are provided in accordance with program policies.
