import arena
import json
import random


# TODO : investigate whether GM can give input from this callback...
def scene_callback(msg):
  jsonMsg = json.loads(msg)



arena.init(
  "arena.andrew.cmu.edu",
  "realm",
  "heads-up-testing",
  scene_callback
)


# TODO : create minigame HUD



# Create objects
sceneLight = arena.Object(
  objName="a-sceneLight",
  objType=arena.Shape.light,
  location=(0, 50, -115),
  persist=True,
)



arena.handle_events()
