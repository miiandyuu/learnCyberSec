in the page source
there's a warning to not use getstatus('all') until get the verify_integrity() patched.

also there is a hashed value of data-secret in input

in the main.js file, there is a variable complete and delete. where it showed what happen with the backend when the user click the button.

try to enumerate all of the enpoint of the api
-> use fuzzing

using burp, see the request parameter on the target
there is sessionID

wfuzz -w [Wordlist (../SecLists/Discovery/Web-Content/api/objects.txt)] -u URL/api/list/FUZZ/?secret=XX -H "Cookie: session=xxx" --hh 24

success on payload "all"

and then able to see all of api POST made by everyone including the admin