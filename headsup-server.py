import arena
import json
import re

import random



# Global vars --v
headsup_ui_cams = list()



# Catches all scene-specific MQTT messages (I think) ...
def scene_callback(msg):
  print( msg )
  jsonMsg = json.loads(msg)

  if re.match("camera_.*", jsonMsg["object_id"]):
    cam_id = jsonMsg["object_id"]
    print(cam_id + " matches!")
    if headsup_ui_cams.count(cam_id) == 0:
      print(cam_id + " added to list of all user cams")
      headsup_ui_cams.append(cam_id)
      # Add headsup ui to newly found cam
      new_headsup_ui(cam_id)


# Adds testUI to dynamically acquired user cam ---v
def new_headsup_ui(cam_object_id):
  # test: create test object mounted to user cam
  testUI = arena.Object(
    objName="a-testUI",
    objType=arena.Shape.circle,
    parent=cam_object_id,
    location=(-0.5, 0, -0.5),
    scale=(0.1, 0.1, 0.1),
  )



arena.init(
  "arena.andrew.cmu.edu",
  "realm",
  "headsup-dev-test",
  scene_callback
)


# Create objects ...
## ... Light is typically useful --v
sceneLight = arena.Object(
  objName="a-sceneLight",
  objType=arena.Shape.light,
  location=(0, 50, -115),
  persist=True,
)


# Listens for relevant events --v
arena.handle_events()
