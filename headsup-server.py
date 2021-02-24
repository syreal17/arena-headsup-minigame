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

def mount_headsup_ui(parent_id):
   print("Test mount headsup ui to " + parent_id)
   button_test1 = Triangle( object_id = parent_id + "__button_test1",
                          parent = parent_id,
                          position = Position(-0.1, 0.0, -0.25),
                          scale = Scale(0.03, 0.03, 0.03),
                          material = Material(color=Color(255, 255, 0), opacity=0.3)
                        )

   scene.add_object(button_test1)



# MAIN ------------------------------------------------------------------------

@scene.run_once
def main():
   box1 = Box( object_id = "a-box1",
               material = Material(color=Color(255, 100, 255)),
               position = Position(0, 0, 0),
               scale = Scale(1, 1, 1),
               persist = False
             )

   scene.add_object(box1)

   # Add UI to existing users
   for user in scene.users:
      mount_headsup_ui(user.object_id)

   # Callback to add UI to future users who join scene
   scene.user_join_callback = user_join_headsup



# THREADS ---------------------------------------------------------------------

scene.run_tasks()

