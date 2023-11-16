# Bug Bounty Report

## Bug Details
- **Target:** [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby todo or not todo)

## Bug Description
Upon thorough investigation of the target web application, several security vulnerabilities have been identified:

1. **Unpatched Warning in Page Source:**
    - **Details:** The page source includes a warning against using `getstatus('all')` until `getverify_integrity()` is patched.
    - **Severity:** Medium
    - **Recommendation:** Immediate patching of `getverify_integrity()` to prevent potential security risks.

2. **Exposed Hashed Value in Input Field:**
    - **Details:** The `main.js` file contains a hashed value of `data-secret` in the input field.
    - **Severity:** Low
    - **Recommendation:** Hashed values should not be exposed on the client side. Consider storing sensitive information securely on the server side.

3. **Exposed Backend Functionality in main.js:**
    - **Details:** The `main.js` file reveals variables named `complete` and `delete` that indicate backend actions when the user clicks the button.
    - **Severity:** Medium
    - **Recommendation:** Conceal backend functionality to avoid potential exploitation.

4. **API Endpoint Enumeration via Fuzzing:**
    - **Details:** Successful enumeration of API endpoints using fuzzing techniques.
    - **Severity:** High
    - **Recommendation:** Implement proper input validation and security controls to restrict unauthorized access to API endpoints.

5. **SessionID Exposure in Request Parameters:**
    - **Details:** The Burp tool identified the presence of a `sessionID` in the request parameters.
    - **Severity:** High
    - **Recommendation:** Ensure that session management is secure and follows best practices to prevent session hijacking.

6. **Unauthorized Access to API POST Requests:**
    - **Details:** Successful access to all API POST requests, including those made by admin users, after discovering the correct payload.
    - **Severity:** Critical
    - **Recommendation:** Implement access controls and authentication mechanisms to prevent unauthorized access to sensitive API functions.

## Steps to Reproduce
1. Observe the warning in the page source regarding the unpatched function.
2. Identify the hashed value of `data-secret` in the input field.
3. Analyze the `main.js` file for exposed backend functionality.
4. Enumerate API endpoints using fuzzing techniques.
5. Use Burp to inspect request parameters and identify the presence of `sessionID`.
6. Utilize the identified sessionID with the appropriate payload in wfuzz.
7. Gain unauthorized access to API POST requests, including those made by admin users.

## Expected Behavior
The application should ensure that sensitive information is not exposed, backend functionality is concealed, and proper access controls are in place to prevent unauthorized access to API endpoints and actions.

## Actual Behavior
The application exposes warnings, hashed values, and backend functionality. Additionally, inadequate access controls allow unauthorized access to API POST requests, compromising the security of the application.

## Vulnerability Impact
The identified vulnerabilities pose a risk of unauthorized access, potential data leakage, and exploitation of backend functionality, compromising the overall security of the web application.

## Proof of Concept
- Utilized wfuzz to enumerate API endpoints and identify potential vulnerabilities.
- Successfully accessed API POST requests, including those of admin users, by exploiting identified vulnerabilities.

## Affected Components
- `getverify_integrity()` function.
- Hashed value of `data-secret` in input fields.
- Exposed backend functionality in `main.js`.
- Inadequate access controls on API endpoints.

## Recommendations
1. **Patch `getverify_integrity()`:**
    - Implement a patch for the `getverify_integrity()` function to address the warning in the page source.

2. **Secure Hashed Values:**
    - Avoid exposing hashed values on the client side. Store sensitive information securely on the server.

3. **Conceal Backend Functionality:**
    - Conceal backend functionality in the `main.js` file to prevent potential exploitation.

4. **Implement Input Validation and Security Controls:**
    - Implement proper input validation and security controls to restrict unauthorized access to API endpoints.

5. **Secure Session Management:**
    - Review and enhance session management mechanisms to prevent session hijacking.

6. **Enhance Access Controls:**
    - Implement robust access controls and authentication mechanisms to prevent unauthorized access to API POST requests.