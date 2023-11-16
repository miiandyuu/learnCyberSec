nothing interesting on the website..

after going deeper into the source code..

in orther to make the value become passed, both of the condition must not be fullfiled (student name isDumb or hasPassed is false)
by looking at the related class (StudentHelper)

in the StudentHelper class, it's using static-eval library to evaluate the formula.
this library have weaknessess when handeling user input (need to be filtered)

on the formula, it will take 3 parameter:
- assignment
- exam
- paper

hence we can interrupt the function when after clicking the submit button with a name that not in StudentHelper.isDumb and make the 3 other parameter will return false (using minimum number), and then rewrite the formula with a rce payload:

(function myTag(y){return ''[!y?'__proto__':'constructor'][y]})('constructor')('throw new Error(global.process.mainModule.constructor._load(\"child_process\").execSync(\"cat /etc/passwd\").toString())')()

aftern the payload successfully return what inside /etc/passwd, change the command to look for the flag

HTB{f33l1ng_4_l1ttl3_blu3_0r_m4yb3_p1nk?...you_n33d_to_b3h4v'eval!!}
