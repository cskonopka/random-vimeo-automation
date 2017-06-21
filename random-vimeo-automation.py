import re
import vimeo
import json
import random 
from twython import Twython

# Twitter setup
APP_KEY = 'twitter-customerkey' 
APP_SECRET = 'twitter-customersecret' 
OAUTH_TOKEN = 'twitter-accesstoken'  # Access Token here
OAUTH_TOKEN_SECRET = 'twitter-accesstokensecret'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 

vimeotoken = "vimeo-token"
vimeoclientid = "vimeo-clientid"
vimeosecret = "vimeo-secret"

v = vimeo.VimeoClient(
    token=vimeotoken,
    key=vimeoclientid,
    secret=vimeosecret)

def randomizeVideo():
	randomPage 		= 	random.randint(1,100)
	randomVid 		= 	random.randint(1,50)	
	about_me 		= 	v.get('/me/videos?page='+str(randomPage)+'&per_page=50')
	unparsed 		= 	about_me.json()
	jack 			= 	[]
	kkkk 			= 	unparsed['data'][randomVid]['link']
	mmmm 			= 	unparsed['data'][randomVid]['name']	
	links 			= 	json.dumps(kkkk)
	names 			= 	json.dumps(mmmm)
	links 			= 	links[1:-1]
	completeLink 	= 	names + " " + links + " #schwwaaa #videosynth #boston"
	var_status		=	completeLink; 
	print completeLink

	twitter.update_status(status=var_status)
	random.seed((randomPage+randomVid)*10000)
	
randomizeVideo()
