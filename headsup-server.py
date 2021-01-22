import json
import re
import random

from arena import *



# GLOBALS ---------------------------------------------------------------------

headsup_ui_cams = list()

arena = Arena( "arena.andrew.cmu.edu",
               "realm",
               "public",
               "headsup-dev-17" )





# TODO : update for 0.1.0 refactor --v
#        Catches all scene-specific MQTT messages
#def scene_callback(msg):
#  print( msg )
#  jsonMsg = json.loads(msg)
#
#  if re.match("camera_.*", jsonMsg["object_id"]):
#    cam_id = jsonMsg["object_id"]
#    print(cam_id + " matches!")
#    if headsup_ui_cams.count(cam_id) == 0:
#      print(cam_id + " added to list of all user cams")
#      headsup_ui_cams.append(cam_id)
#      # Add headsup ui to newly found cam
#      new_headsup_ui(cam_id)

# TODO : update function for 0.1.0 refactor ---v
# Adds testUI to dynamically acquired user cam ---v
#def new_headsup_ui(cam_object_id):
#  # test: create test object mounted to user cam
#  testUI = arena.Object(
#    objName="a-testUI",
#    objType=arena.Shape.circle,
#    parent=cam_object_id,
#    location=(-0.5, 0, -0.5),
#    scale=(0.1, 0.1, 0.1),
#  )



# MAIN ------------------------------------------------------------------------

@arena.run_once # make this function a task that runs once at startup
def main():
    cube1 = Cube( object_id="a-cube1",
                 color=Color(255, 100, 255),
                 position=Position(0, 50, -140),
                 scale=Scale(25, 25, 25),
                 persist=True )
    arena.add_object(cube1)



# THREADS ---------------------------------------------------------------------

arena.run_tasks()

