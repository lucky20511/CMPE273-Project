import pycurl
from StringIO import StringIO 

import json 
from Lyft_key import *

def given_cost(from_p, to_p):
    print "-------- Lyft API Call --------"
    start = from_p
    end = to_p
    #print start, end
    ans = StringIO()
    c = pycurl.Curl()
#    url = 'https://api.lyft.com/v1/cost?start_lat='+str(37.77+start[0]/100.0)+'&start_lng='+str(-122.41+start[1]/100.0)+ '&end_lat=' + str(37.77+end[0]/100.0) + '&end_lng='+ str(-122.41+end[1]/100.0)
    url = 'https://api.lyft.com/v1/cost?start_lat='+str(start[0])+'&start_lng='+str(start[1])+ '&end_lat=' + str(end[0]) + '&end_lng='+ str(end[1])
    #print "QQQQQQQ"
    print ([start[0],start[1]],[end[0],end[1]])
    #print (end[0],end[1])
    c.setopt(c.URL, url)

    #print get_new_lyft_key()
    #c.setopt(c.HTTPHEADER, ['Accept: application/json','Authorization: bearer gAAAAABYPAWh08lk7SZizmS6lzkDN7ARrD-UqMaTb9JodjkoVZ_u2xLR9QKMejdv-B5SrK528l0Q6LUBTLWTB5UXiwU4v6EKoRhUzwdZC6Ytta7USr8AidYBIcKS0MyOXheWTeB5goc_2nIBwaxG2RJAr1CaJdScP0X-tkwWtz-w1ne18qCd0qEVvNztuhyp-xhP6_PpON5s3N51_Z-RykN0KcSZXztvmA=='])
    c.setopt(c.HTTPHEADER, ['Accept: application/json','Authorization: bearer '+ get_new_lyft_key()])
    
    c.setopt(c.WRITEDATA, ans)
    c.perform()   
    result = json.loads(ans.getvalue())
    print "-------- Lyft API End--------"
    #print "XXXXXXXXXX"
    #print result
    new_ans={}
    if 'error_description' in result.keys():
        #lyft out for sercvice, so set max float value to support run
        new_ans['cost'] = 100000.0
        new_ans['duration'] = 100000.0
        new_ans['distance'] = 100000.0
        c.close()
        return json.dumps(new_ans)
    lists = result['cost_estimates']
    for item in lists:
        #if item['ride_type'] == 'lyft_line':
        if item['ride_type'] == 'lyft_line':
            cost = item['estimated_cost_cents_max']
            cost += item['estimated_cost_cents_min']
            new_ans['cost'] = cost / 200.0
            #print new_ans['cost']
            #new_ans['current_code'] = 'USD'
            new_ans['duration'] = item['estimated_duration_seconds']/60.0
            #new_ans['duration_unite'] = 'minutes'
            new_ans['distance'] = item['estimated_distance_miles']
            #new_ans['distance_unite'] = 'miles'
            break
        elif item['ride_type'] == 'lyft':
            cost = item['estimated_cost_cents_max']
            cost += item['estimated_cost_cents_min']
            new_ans['cost'] = cost / 200.0
            #print new_ans['cost']
            #new_ans['current_code'] = 'USD'
            new_ans['duration'] = item['estimated_duration_seconds']/60
            #new_ans['duration_unite'] = 'minutes'
            new_ans['distance'] = item['estimated_distance_miles']
            #new_ans['distance_unite'] = 'miles'
            break

    c.close()
    
    return json.dumps(new_ans)
