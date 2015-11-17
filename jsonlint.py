import sys
import json
import traceback

def read_stdin():
    
    try:
        json.loads(sys.stdin.read())
        return True
    except Exception as e:
        print e.args
        print traceback.format_exc()
        return False


if read_stdin() is True:
    print 'Json is valid'
else:
    print 'Json is invalid'
