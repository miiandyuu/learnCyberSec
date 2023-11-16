# Bug Bounty Report

## Bug Details
- **Target:** [https://app.hackthebox.com/tracks/OWASP-Top-10](https://app.hackthebox.com/tracks/OWASP-Top-10) (baby boneChewerCon)

## Bug Description
A security vulnerability has been identified in the email newsletter subscription submission box, allowing for Cross-Site Scripting (XSS) attacks.

## Steps to Reproduce
1. Navigate to the email newsletter subscription submission box on the target website.
2. Enter the following payload into the input field:
    ```html
    <script>alert('1')</script>
    ```
3. Submit the payload by completing the subscription process.

## Expected Behavior
The website's email newsletter subscription submission box should validate and sanitize input to prevent the execution of malicious scripts, ensuring a secure user experience.

## Actual Behavior
The input field is vulnerable to XSS attacks, allowing the execution of arbitrary scripts. In this case, the payload `<script>alert('1')</script>` successfully triggers an alert dialog.

## Vulnerability Impact
The XSS vulnerability in the email newsletter subscription submission box poses a risk of executing malicious scripts within the context of users' browsers, potentially leading to session theft, defacement, or other forms of client-side attacks.

## Proof of Concept
```html
<script>alert('1')</script>
```

## Affected Components
- Email newsletter subscription submission box.

## Recommendations
1. **Input Validation and Sanitization:**
- Implement robust input validation and sanitization mechanisms to prevent XSS attacks.
2. **Content Security Policy (CSP):**
- Enforce a strict Content Security Policy to mitigate the impact of potential XSS vulnerabilities.
3. **Security Awareness Training:**
- Train development and security teams to recognize and prevent common web application security vulnerabilities, including XSS.