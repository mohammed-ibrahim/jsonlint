import sys
import json
import traceback

def read_stdin():
    
    try:
        contents = json.loads(sys.stdin.read())
        return contents
    except Exception as e:
        print e.args
        print traceback.format_exc()
        return None


parsed = read_stdin()
if parsed is not None:
    print ''
    print ''
    print json.dumps(parsed, indent=4)
    print ''
    print 'Json is Valid'
    print ''
else:
    print 'JSON IS INVALID!!!'
