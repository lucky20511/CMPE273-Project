import pycurl
from StringIO import StringIO
import json

def get_new_lyft_key():
    ans = StringIO()
    c = pycurl.Curl()
    url = 'https://api.lyft.com/oauth/token'
    c.setopt(c.URL, url)
    c.setopt(c.POST, True)
    post_data = json.dumps({"grant_type": "client_credentials", "scope": "public"})
    c.setopt(c.POSTFIELDS, post_data)
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.USERPWD, '%s:%s' % ('DR0wVgWATSHH', 'T0dzP3n7b_-B5ql-GyGDt3AoeY_Xd22X'))
    c.setopt(c.WRITEDATA, ans)
    
    c.perform()   
    result = json.loads(ans.getvalue())
    return result['access_token']
