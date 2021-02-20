import json
import re
import random

from arena import *



# GLOBALS ---------------------------------------------------------------------

headsup_ui_cams = list()

arena = Arena()





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

@arena.run_once
def main():
    box1 = Box( object_id="a-box1",
                 color=Color(255, 100, 255),
                 position=Position(0, 0, 0),
                 scale=Scale(1, 1, 1),
                 persist=False )
    arena.add_object(box1)



# THREADS ---------------------------------------------------------------------

arena.run_tasks()

