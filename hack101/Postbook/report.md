# Bug Bounty Report

**Reported by:** miiandyuu
**Date:** 10/20/2023
**Website URL:** [https://6e17828e65720c02ea0fd05b94db0583.ctf.hacker101.com/]

## Summary

I have identified multiple security vulnerabilities on the website [https://6e17828e65720c02ea0fd05b94db0583.ctf.hacker101.com/], which include IDOR (Insecure Direct Object Reference) issues, weak credentials, hidden/commented important scripts, and session hijacking. Below are the details of each vulnerability.

## Bug Details

### Vulnerability 1: IDOR on the View Page

**Bug Description:**
The website allows unauthorized access to other users' posts by manually changing the 'id' parameter in the URL.

**Steps to Reproduce:**
1. Visit the following URL: `/index.php?page=view.php&id=2`.
2. Manually change the 'id' parameter to view other user's posts.

**Expected Behavior:**
Users should only be able to view their own posts.

**Actual Behavior:**
Unauthorized access to other users' posts is possible.

### Vulnerability 2: IDOR on the Edit Page

**Bug Description:**
The 'id' parameter on the edit page can be manipulated to edit posts from different accounts.

**Steps to Reproduce:**
1. Visit the following URL: `/index.php?page=edit.php&id=2`.
2. Manually change the 'id' parameter to edit posts from other accounts.

**Expected Behavior:**
Users should only be able to edit their own posts.

**Actual Behavior:**
Unauthorized access to edit posts from different accounts is possible.

### Vulnerability 3: Weak Credentials

**Bug Description:**
The default password for the 'user' account is 'password,' which is a weak and easily guessable password.

**Steps to Reproduce:**
No specific steps are required as this is a known issue.

**Expected Behavior:**
User accounts should have strong and unique passwords by default.

**Actual Behavior:**
The 'user' account has a weak default password.

### Vulnerability 4: Hidden/Commented Important Scripts

**Bug Description:**
There are hidden/commented script elements in the HTML source code that can be accessed using the browser's inspect element feature.

**Steps to Reproduce:**
1. Use the browser's inspect element feature to view hidden/commented script elements.

**Expected Behavior:**
Sensitive scripts should not be accessible to the public.

**Actual Behavior:**
Sensitive scripts can be accessed by the public.

### Vulnerability 5: Bruteforcing on the View Page

**Bug Description:**
A hidden post (ID 945) is discovered through a bruteforce attack on the 'id' parameter in the URL.

**Steps to Reproduce:**
1. Use a tool like Burp Suite to bruteforce the 'id' parameter in the URL.

**Expected Behavior:**
Hidden posts should not be discoverable through bruteforce.

**Actual Behavior:**
A hidden post (ID 945) is discoverable through bruteforce.

### Vulnerability 6: IDOR on the Delete Function

**Bug Description:**
The 'id' parameter on the delete page uses md5 encoding, and it can be manipulated to delete posts from different accounts.

**Steps to Reproduce:**
1. Visit the following URL: `/index.php?page=delete.php&id=c9f0f895fb98ab9159f51fd0297e236d`.
2. Reverse the encoded 'id' to discover the original number.
3. Manually change the 'id' parameter to delete posts from different accounts.

**Expected Behavior:**
Users should only be able to delete their own posts.

**Actual Behavior:**
Unauthorized access to delete posts from different accounts is possible.

### Vulnerability 7: Session Hijacking using Cookie

**Bug Description:**
Session cookies use basic numbers (e.g., 1, 2) that can be easily decoded. Attackers can exploit this to hijack sessions.

**Steps to Reproduce:**
1. Decode the session cookie to reveal basic numbers.
2. Encode a different number using md5 and replace it in the cookie.

**Expected Behavior:**
Session cookies should be securely encrypted and not susceptible to easy tampering.

**Actual Behavior:**
Session hijacking is possible by manipulating the session cookie.

## Vulnerability Impact

These vulnerabilities pose significant security risks, including unauthorized access to user data, manipulation of posts, and session hijacking.

## Proof of Concept

To demonstrate the vulnerabilities, I have prepared proof of concept (PoC) examples for each issue. Due to ethical considerations, I am not disclosing the full PoC in this report.

## Affected Components

The vulnerabilities affect the following components of the website:

- View Page
- Edit Page
- Default User Credentials
- Hidden/Commented Scripts
- Delete Function
- Session Cookies

## Recommendations

I recommend the following actions to address these vulnerabilities:

1. Implement proper access control to prevent IDOR vulnerabilities.
2. Enforce strong and unique passwords for user accounts.
3. Remove or secure hidden/commented scripts.
4. Improve session management to prevent session hijacking.

## Additional Information

Additional information or technical details about the vulnerabilities can be provided upon request.

## Contact Information

Please feel free to contact me for further details or clarification regarding these findings:


- https://github.com/miiandyuu

## Terms and Conditions

I have followed responsible disclosure guidelines by reporting these vulnerabilities to the website's owner. I am not disclosing any sensitive information or PoC that could harm the website's integrity. I expect to work collaboratively with the website owner to address these issues.

Please take these findings seriously, as they have the potential to compromise the security and privacy of users on the website.

Thank you for your attention to this matter.

Sincerely,

miiandyuu