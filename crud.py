#!/usr/bin/python

from flask import Flask, request, Response, json, abort
from sqlalchemy import *
import requests
import re
from TSP_LYFT import *
from TSP_UBER import *
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#db = SQLAlchemy(app)

#load sql db
db = create_engine('mysql://root:lucky20511@localhost/mysql', echo=True)
metadata = MetaData(db)

def DBGetTableByName(table_name) :
    try :
        table = Table(table_name, metadata, autoload=True)
        return True
    except :
        return False

if not DBGetTableByName('273PROJECT'):
    sql = "CREATE TABLE `mysql`.`273PROJECT` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT,`name` TEXT,`address` TEXT,`city` TEXT,`state` TEXT,`zip` TEXT,`lat` FLOAT,`lng` FLOAT, PRIMARY KEY(`id`))"
    result = db.engine.execute(sql)

def wrapUpJSON(dic_s) :
    js = {  "id" : dic_s['id'],
            "name" : dic_s['name'],
            "address" : dic_s['address'],
            "city" : dic_s['city'],
            "state" : dic_s['state'],
            "zip" : dic_s['zip'],
            "coordinate" : { "lat" : dic_s['lat'], 
                            "lng" : dic_s['lng'] }
            }
    return json.dumps(js)


@app.route('/locations/<int:postID>', methods = ['GET', 'PUT', 'DELETE'])
def api_GET_PUT_DELETE(postID):
    if request.method == 'GET':

        sql = "SELECT * FROM 273PROJECT WHERE id='%d' " %postID

        result = db.engine.execute(sql)

        dic = [(dict(row.items())) for row in result]

        if len(dic) < 1: 
            abort(404)   


        resp = Response(wrapUpJSON(dic[0]), status=200, mimetype='application/json')
        return resp


    elif request.method == 'PUT':
        #if request.headers['Content-Type'] == 'text/plain':
        #    js = request.data
        
        #check if the type is json
        #if request.headers['Content-Type'] == 'application/json':
        resp_dict = json.loads(request.data)
        #else:
        #    abort(404)

        sql = "UPDATE 273PROJECT SET " 
        count = 0
        for i in resp_dict:
            if count != 0:
                sql = sql + ", "
            # only can modify the name
            if i != 'name':
                abort(404)
            sql = sql + "%s='%s' " %(i, resp_dict[i])
            count = count + 1
            
        sql = sql + " WHERE id = '%d';" %postID
        #print sql
        result = db.engine.execute(sql)
        resp = Response(status=202)
        return resp
        


    elif request.method == 'DELETE':
        resp = Response(status=204)
        sql = "DELETE FROM 273PROJECT WHERE id=%d;" % postID 
        result = db.engine.execute(sql)
        return resp


@app.route('/locations', methods = ['POST'])
def api_POST():
    if request.method == 'POST':    

        #if request.headers['Content-Type'] == 'text/plain':
        #   js = request.data
        #check if the type is json
        #if request.headers['Content-Type'] == 'application/json':
        resp_dict = json.loads(request.data)
        #else:
        #    abort(404)
  

        key = "AIzaSyDKhnvZjbr8lthcJs4BXDWYqEpwiu6uvu0"
        address = resp_dict["address"] + resp_dict["city"] + resp_dict["state"] + resp_dict["zip"]
        google_api_url = "https://maps.googleapis.com/maps/api/geocode/json?key=%s&address=%s" %(key, address)

        r = requests.get(google_api_url)
        
        google_ret = json.loads(r.text)

        #print r.text

        #print str(google_ret['results'][0]['geometry']['location']['lat']) +"\n";
        #print str(google_ret['results'][0]['geometry']['location']['lng']) +"\n";
        lat = google_ret['results'][0]['geometry']['location']['lat']
        lng = google_ret['results'][0]['geometry']['location']['lng']


        sql = "INSERT INTO 273PROJECT (name, address, city, state, zip, lat, lng) VALUES('%s', '%s', '%s', '%s', '%s', '%f', '%f');" %(resp_dict['name'], resp_dict['address'], resp_dict['city'], resp_dict['state'], resp_dict['zip'], lat, lng)
        #print sql
        result = db.engine.execute(sql)


        #sql = "SELECT * FROM 273PROJECT WHERE name='%s' AND address = '%s' AND city='%s' AND state='%s' AND zip='%s' AND lat='%f' AND lng='%f';" %(resp_dict['name'], resp_dict['address'], resp_dict['city'], resp_dict['state'], resp_dict['zip'], lat, lng)
        sql = "SELECT * FROM 273PROJECT WHERE name='%s' AND address = '%s' AND city='%s' AND state='%s' AND zip='%s';" %(resp_dict['name'], resp_dict['address'], resp_dict['city'], resp_dict['state'], resp_dict['zip'])
        result = db.engine.execute(sql)
        #print sql
        #print result
        dic = [(dict(row.items())) for row in result]
        #print dic[0]
           
        dic_s = dic[len(dic)-1]

       
        resp = Response(wrapUpJSON(dic_s), status=201, mimetype='application/json')

        return resp

@app.route('/trips', methods = ['POST'])
def trip_POST():
    if request.method == 'POST': 
        #resp_dict = json.loads(request.data)
        resp_dict = json.loads(request.data)
        start_place = resp_dict['start']
        end_place = resp_dict['end']
        mid_place = resp_dict['others']

        print start_place
        print end_place
        print mid_place
 
        #######  start  ######
        searchObj = re.search( r'(locations/)(.*)', start_place, re.M|re.I)
        if(searchObj):
            start_id = searchObj.group(2)
            #print start_id
        else:
            abort(404)

        sql = "SELECT * FROM 273PROJECT WHERE id='%d' " %int(start_id)
        result = db.engine.execute(sql)
        start_coordinate = [(dict(row.items())) for row in result]
        if len(start_coordinate) < 1: 
            abort(404) 

        # print "????????start"
        # for  i in range(0, len(start_coordinate)):
        #     print start_coordinate[i]['lat']
        #     print start_coordinate[i]['lng']    
        
        #print start_coordinate

        #######  end  ######    
        searchObj = re.search( r'(locations/)(.*)', end_place, re.M|re.I)
        if(searchObj):
            end_id = searchObj.group(2)
            #print end_id
        else:
            abort(404)


        sql = "SELECT * FROM 273PROJECT WHERE id='%d' " %int(end_id)
        result = db.engine.execute(sql)
        end_coordinate = [(dict(row.items())) for row in result]
        if len(end_coordinate) < 1: 
            abort(404)    

        # print "????????end" 
        # for  i in range(0, len(end_coordinate)):
        #     print end_coordinate[i]['lat']
        #     print end_coordinate[i]['lng']


           
        #print end_coordinate

        #######  mid  ######  
        index = 0  
        mid_id = []
        sql = "SELECT * FROM 273PROJECT WHERE"
        for mid in mid_place:
            #print mid
            searchObj = re.search( r'(locations/)(.*)', mid, re.M|re.I)
            if(searchObj):
                if(index == 0):
                    sql += " id='%d'" %int(searchObj.group(2))
                else:
                    sql += " OR id='%d'" %int(searchObj.group(2))
                mid_id.append(searchObj.group(2))
            else:
                abort(404)
            index = index + 1
        sql += ";"

        result = db.engine.execute(sql)
        mid_coordinate = [(dict(row.items())) for row in result]
        if len(mid_coordinate) < 1: 
            abort(404)

        # print "????????mid"   
        # for  i in range(0, len(mid_coordinate)):
        #     print mid_coordinate[i]['lat']
        #     print mid_coordinate[i]['lng']


        #for i in range(0, )

        coord = []
        coord.append((start_coordinate[0]['lat'], start_coordinate[0]['lng']))
        for i in range(0, len(mid_coordinate)):
            coord.append((mid_coordinate[i]['lat'], mid_coordinate[i]['lng']))    
        coord.append((end_coordinate[0]['lat'], end_coordinate[0]['lng'])) 

        print " === Input Coordinate === "
        print coord
        print " ======================== "
        #result_uber = run_uber([(37.770,-122.441),(37.781,-122.331),(37.791,-122.405),(37.100,-122.000),(37.999,-122.511)])
        #result_uber = run_uber([(37.770,-122.441),(37.781,-122.331),(37.791,-122.405),(37.999,-122.511)])
        (result_uber, uber_tour) = run_uber(coord)
        
        (result_lyft, lyft_tour) = run_lyft(coord)
        #start_place
        #end_place
        print uber_tour
        uber_mid_array = []
        for i in range(1,len(uber_tour)-1):
            uber_mid_array.append(mid_place[i-1])
        Uber_best = {"UBER":{"start":start_place, "end":end_place, "mid":uber_mid_array}}    

        print lyft_tour
        lyft_mid_array = []
        for i in range(1,len(lyft_tour)-1):
            lyft_mid_array.append(mid_place[i-1])
        Lyft_best = {"LYFT":{"start":start_place, "end":end_place, "mid":lyft_mid_array}}    


        print {"provider" : [result_uber, result_lyft], "best_route_by_costs":[Uber_best, Lyft_best]}
        
        #js = {"provider" : [result_uber, run_lyft]}
        #print lyft_tour
        js = {"provider" : [result_uber, result_lyft], "best_route_by_costs":[Uber_best, Lyft_best]}
        #js = json.dumps(js)
        #print {"provider": [result_uber, result_lyft]}
        #print "======tour_uber======"
        #print tour_uber
        #print "======tour_lyft======"
        #print tour_lyft

        resp = Response(json.dumps(js), status=201, mimetype='application/json')

        return resp




if __name__ == '__main__':
   #app.run(host='0.0.0.0',port=1314, debug=True)
   app.run(host='0.0.0.0', port=1314, debug=True)