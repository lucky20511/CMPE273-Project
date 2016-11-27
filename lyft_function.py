import pycurl
from StringIO import StringIO 

import json
  
def given_cost(from_p, to_p):
    start = from_p
    end = to_p

    ans = StringIO()
    c = pycurl.Curl()
    url = 'https://api.lyft.com/v1/cost?start_lat='+str(start[0])+'&start_lng='+str(start[1])+ '&end_lat=' + str(end[0]) + '&end_lng='+ str(end[1])
    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, ['Accept: application/json','Authorization: bearer gAAAAABYOe3cIxMYsBwHUhWcIUGy2RLnJ5SEVoOtsa3m6UAcHWdvhZFmFZLxgbLqO7Gpde5nzB9LAkmdJWf5L53tnzspwWirGZGi_8dgmJ2Yrm__Q40aGxWt-z0ZBOtnYE_hhGSahTjQunHOk-YlX99vthacuyEm_eg7KuAxezem-xWN8zQQaFEaMJg9wMa_hG6oTvU0_C1c0dQSAkxjw8LxrrG_knIdng=='])
    c.setopt(c.WRITEDATA, ans)
    c.perform()   
    result = json.loads(ans.getvalue())
    print result
    lists = result['cost_estimates']
    new_ans={}
    for item in lists:
        if item['ride_type'] == 'lyft_line':
            cost = item['estimated_cost_cents_max']
            cost += item['estimated_cost_cents_min']
            new_ans['cost'] = cost / 200
            new_ans['current_code'] = 'USD'
            new_ans['duration'] = item['estimated_duration_seconds']/60
            new_ans['duration_unite'] = 'minutes'
            new_ans['distance'] = item['estimated_distance_miles']
            new_ans['distance_unite'] = 'miles'
    c.close()
    
    return new_ans