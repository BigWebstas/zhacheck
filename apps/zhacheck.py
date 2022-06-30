import appdaemon.plugins.hass.hassapi as hass
import sys
import json
import time
import datetime

from websocket import create_connection

class zha_check(hass.Hass):

  def initialize(self):
    self.token = self.args['token']      
    self.addr = "ws://" + self.args['ip'] + ":8123/api/websocket"

    self.listen_event(self.ZHAmonitor, "ZHAcheck")
    #call this from an HA automation by action: - event: ZHAcheck

    handle = self.run_every(self.ZHAmonitor, 'now+60', 60*5)
    #run every 5 mins regardless of event
    
    self.ZHAdump()

  def ZHAmonitor (self, event_name, data, kwargs): 
    self.ZHAdump()

  def ZHAdump (self): 
    count = 0
    last_seen = {}
    max_time = 7200 #120 minutes
    now = datetime.datetime.now()

    ws = create_connection(self.addr)
    result =  ws.recv()

    ws.send(json.dumps( {'type': 'auth', 'access_token': self.token} ))
    result =  ws.recv()
    
    ident = 1
    ws.send(json.dumps( {'id': ident, 'type': 'zha/devices'} ))
    result =  ws.recv()    

    # convert the string that came back to JSON
    json_result = json.loads(result)

    # retrieve each device that was returned
    for device in json_result["result"] :
      #self.log("Device: " + str(device["user_given_name"]) + " " + str(device["last_seen"]))

      last_date = str(device["last_seen"])
      last_dat2 = last_date[:19]
      last_dat3 = datetime.datetime.strptime(last_dat2, '%Y-%m-%dT%H:%M:%S')
      diff = (now - last_dat3).seconds
      if diff > max_time:
        last_seen[str(device["user_given_name"])] = last_dat3
        count = count + 1

#    last_seen['friendly_name'] = 'Last Seen ZHA'
#    last_seen['icon'] = 'mdi:message-alert-outline'
    self.set_state('sensor.zha_last_seen', replace=True, state=count, attributes=last_seen)
    #this will create a sensor called sensor.last_seen_zha with a list of attributes containing the name and last_seen time of each sensor not reporting for more then 90 minutes.
    #I then have an automation that emails me an alert when this sensor is greater than 0
