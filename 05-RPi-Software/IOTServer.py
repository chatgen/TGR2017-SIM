#!/usr/bin/python2.7

import os
import json, requests, base64
import urllib

# curl -i http://0.0.0.0:5000/LINEtoPI -X POST -u ProjectMAR:animations -H "Content-Type:application/json" -d '{"a":"animations"}'

#HEROKU_Server = 'https://projectmar-bridge.herokuapp.com/PItoLINE'
HEROKU_Server = 'http://localhost:5000/PItoLINE'

usernameDB = os.environ.get('LoginDB')
passwordDB = os.environ.get('PasswordDB')

usernameDB = 'ProjectMAR'
passwordDB = 'animations'

authMSG = (usernameDB, passwordDB)
#print('authMSG: ',authMSG)


def PItoLINE(url, payload, payloadType='text'):
	
	global authMSG
	headerMSG = {'content-type': 'application/json'}

	messageToLINE = {
		'Type'    :payloadType,
		'Payload' : payload 
	}

	resp = requests.post(url, auth=authMSG, data=json.dumps(messageToLINE), headers=headerMSG)
	print(resp)
	return resp


PItoLINE(HEROKU_Server, 'animations', payloadType='text')


messageToLINE = {
		'Type'    :"payloadType",
		'Payload' : "payload" 
	}

tempJSON = json.dumps(messageToLINE)
#print(tempJSON)

tempDict = json.loads(tempJSON)
#print(tempDict['Type'])

#data = img_file.read()        

# build JSON object
#outjson = {}
#outjson['img'] = data.encode('base64')   # data has to be encoded base64

#outjson['leaf'] = "leaf"
#json_data = json.dumps(outjson)

# close file pointer and send data
#img_file.close()

#print(json_data)

#PItoLINE(HEROKU_Server, 'payload')


'''
projectDir = os.path.dirname(__file__)
img_file = open(projectDir + '/img/test.jpg', "r")
print(projectDir + '/img/test.jpg')

'''