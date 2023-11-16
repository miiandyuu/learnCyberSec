# Bug Bounty Report

## Bug Details
- **Target:** [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby breaking grad)

## Bug Description
While initially unremarkable, a closer examination of the website's source code reveals a critical vulnerability in the `StudentHelper` class, specifically in the handling of user input in the formula evaluation process. This vulnerability can be exploited to execute arbitrary code on the server.

## Steps to Reproduce
1. Navigate to the target website: [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby breaking grad).
2. Inspect the source code and identify the `StudentHelper` class.
3. Notice the conditions for the value to be passed involve the student name not being "isDumb" and `hasPassed` being false.
4. Identify the use of the `static-eval` library in the `StudentHelper` class to evaluate the formula.
5. Exploit the weakness in the `static-eval` library by providing manipulated input.
6. Submit a payload with a student name not in `StudentHelper.isDumb` and set the parameters (assignment, exam, paper) to return false.
7. Craft an arbitrary code execution (RCE) payload and inject it into the formula.

## Expected Behavior
The website should properly validate and sanitize user input, ensuring the secure evaluation of formulas. The `static-eval` library should handle user input securely.

## Actual Behavior
The `static-eval` library used in the `StudentHelper` class has vulnerabilities when handling user input, enabling an attacker to execute arbitrary code by manipulating the formula parameters.

## Vulnerability Impact
The identified vulnerability allows an attacker to execute arbitrary code on the server, leading to potential unauthorized access, data manipulation, and other security breaches.

## Proof of Concept
```javascript
(function myTag(y){return ''[!y?'__proto__':'constructor'][y]})('constructor')('throw new Error(global.process.mainModule.constructor._load(\"child_process\").execSync(\"cat /etc/passwd\").toString())')()
```
After successfully exploiting the vulnerability, the payload returns the content of `/etc/passwd`, indicating a successful penetration into the system.

## Affected Components
- `StudentHelper class`.
- Use of the `static-eval` library for formula evaluation.

## Recommendation
1. **Input Validation and Sanitization:**
- Implement rigorous input validation and sanitization mechanisms to prevent code injection vulnerabilities.
2. **Library Security:**
- Review and update the usage of the static-eval library or consider alternatives with better security measures.
3. **Code Review:**
- Conduct thorough code reviews to identify and mitigate potential security risks in the application.
4. **Security Training:**
- Provide security training for developers to raise awareness of secure coding practices.