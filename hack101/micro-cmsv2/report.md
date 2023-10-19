# Bug Bounty Report - Micro-CMS v2

## Introduction

I conducted a bug bounty assessment on the Micro-CMS v2 website, which is available at [https://ctf.hacker101.com/ctf](https://ctf.hacker101.com/ctf). The website is a basic CMS where users can create and edit pages, with certain actions restricted to logged-in users. The focus of the assessment was to identify and report security vulnerabilities.

## Scope

The assessment was conducted on a specific subdomain of the website: [https://4a21f259872b8aa6429dd5cb2dd8c0dd.ctf.hacker101.com](https://4a21f259872b8aa6429dd5cb2dd8c0dd.ctf.hacker101.com). The limited scope allowed for directory enumeration and manual testing of specific website features.

## Directory Enumeration

I performed directory enumeration using the `ffuf` tool with the common wordlist. The following directories were identified:

- `/home`
- `/login`
- `/logout`

Additional manual enumeration revealed existing pages at `/page/1` and `/page/2`, each containing text and a link to edit the page. However, lacking credentials, clicking the edit link redirected me to the `/login` page.

## Vulnerabilities Identified

### SQL Injection

#### Description

I identified a SQL Injection vulnerability in the login form. By using the payload `'admin ' UNION SELECT 'x' AS password FROM admins WHERE '1' = '1'` in the username field and 'x' in the password field, I was able to successfully log in as an administrator.

#### Impact

This vulnerability allows an attacker to bypass authentication and log in as an administrator, potentially gaining unauthorized access to sensitive information and perform administrative actions.

### Insecure Direct Object Reference (IDOR)

#### Description

I discovered an Insecure Direct Object Reference (IDOR) vulnerability that allowed unauthorized access to restricted pages. The vulnerability was exploited using the following `curl` command: `curl -v -X POST https://4a21f259872b8aa6429dd5cb2dd8c0dd.ctf.hacker101.com/page/edit/1`.

#### Impact

The IDOR vulnerability enables an attacker to access and modify pages and data that should be restricted. This can lead to data leakage, unauthorized editing, and other unauthorized actions.

### Bruteforce via BurpSuite

#### Description

I used BurpSuite to perform a brute force attack to uncover valid usernames and passwords. I began by finding the length of the credentials using the payloads `{' or LENGTH(username)=1#}` and `{' or LENGTH(password)=1#}`. Then, I employed the payloads `admin ' or username LIKE '§_§§_§§_§§_§§_§§_§#'` and `admin ' or password LIKE '§_§§_§§_§§_§§_§§_§#'` to determine the characters in each credential, where the length of the credentials influenced the number of '§_§' placeholders.

#### Impact

The ability to perform brute force attacks can lead to the disclosure of valid usernames and passwords, posing a risk to the confidentiality and security of user accounts.

## Conclusion

The Micro-CMS v2 website exhibits several security vulnerabilities, including SQL Injection, Insecure Direct Object Reference (IDOR), and the potential for brute force attacks. These vulnerabilities can lead to unauthorized access, data leakage, and other security risks.

I recommend that the website owner addresses these vulnerabilities promptly to enhance the security of their platform.

## Disclosure Timeline

- [10/05/2023]: Vulnerabilities discovered.
- [10/05/2023]: Initial contact with the website owner to report findings.
- [10/05/2023]: Follow-up communication with the website owner.
- [10/05/2023]: Vulnerabilities confirmed as fixed by the website owner.

## Disclaimer

This report is intended for informational purposes only, and the vulnerabilities were identified and reported in compliance with responsible disclosure practices. I did not engage in any malicious or unauthorized actions during this assessment.

