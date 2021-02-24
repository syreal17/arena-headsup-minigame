import json
import re
import random

from arena import *



# GLOBALS ---------------------------------------------------------------------

headsup_ui_cams = list()

scene = Arena()



# CALLBACKS -------------------------------------------------------------------

def user_join_headsup(camera):
   mount_headsup_ui(camera.object_id)



# OTHER DEFS ------------------------------------------------------------------

def mount_headsup_ui(object_id):
   print("Test mount headsup ui to " + object_id)



# MAIN ------------------------------------------------------------------------

@scene.run_once
def main():
   box1 = Box( object_id="a-box1",
               material=Material(color=Color(255, 100, 255)),
               position=Position(0, 0, 0),
               scale=Scale(1, 1, 1),
               persist=False )

   scene.add_object(box1)

   # Add UI to existing users
   for user in scene.users:
      mount_headsup_ui(user.object_id)

   # Callback to add UI to future users who join scene
   scene.user_join_callback = user_join_headsup



# THREADS ---------------------------------------------------------------------

scene.run_tasks()

