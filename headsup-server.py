import arena
import json
import random



# Catches all scene-specific MQTT messages (I think) ...
def scene_callback(msg):
  print( msg )
  jsonMsg = json.loads(msg)

# TODO : create function to add UI to user cam



arena.init(
  "arena.andrew.cmu.edu",
  "realm",
  "headsup-dev-test",
  scene_callback
)



# Create objects
## Light is typically useful --v
sceneLight = arena.Object(
  objName="a-sceneLight",
  objType=arena.Shape.light,
  location=(0, 50, -115),
  persist=True,
)

# test: create test object mounted to user cam
testUI = arena.Object(
  objName="a-testUI",
  objType=arena.Shape.circle,
  parent="camera_64_LukeJones",
  location=(-0.5, 0, -0.5),
  #scale=(0.1, 0.1, 0.1),
)



# Listens for relevant events --v
arena.handle_events()
