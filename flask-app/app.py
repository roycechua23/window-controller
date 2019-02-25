#
# Created by Rui Santos
# Complete project details: http://randomnerdtutorials.com
#

import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

mqttc=mqtt.Client()
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

# Create a dictionary called pins to store the pin number, name, and pin state:
things = {
   1 : {'name' : 'window1', 'board' : 'esp8266', 'topic' : 'esp8266/window1', 'state' : 'False'},
   }

# Put the pin dictionary into the template data dictionary:
templateData = {
   'things' : things
   }

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<board>/<changething>/<action>")

def action(board, changething, action):
   # Convert the pin from the URL into an integer:
   changething = int(changething)
   # Get the device name for the pin being changed:
   devicePin = things[changething]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "1" and board == 'esp8266':
      mqttc.publish(things[changething]['topic'],"1")
      things[changething]['state'] = 'True'

   if action == "0" and board == 'esp8266':
      mqttc.publish(things[changething]['topic'],"0")
      things[changething]['state'] = 'False'

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'things' : things
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8181, debug=True)

