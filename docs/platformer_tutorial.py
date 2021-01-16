# Start by importing ursina and creating a window.
from ursina import *
app = Ursina()

# ## Using the built in platformer controller
#
# A simple way to get stared is to use the built in platformer controller.
# It's pretty basic, so you might want to write your own at a later point.
# It is however a good starting point, so let's import it like this:
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)

# You can change settings like jump_height, walk_speed, and gravity.
# If you want to larn more about how it works you can read its code here:
# https://github.com/pokepetter/ursina/blob/master/ursina/prefabs/platformer_controller_2d.py
#
# If we try to play the game right now, you'll fall for all infinity, so let's add a ground:
ground = Entity(model='quad', scale_x=10, collider='box', color=color.black)

# ## Making a level editor
#
# Now, it works, but it's a pretty boring game, so let's make a more interesting level.
# There are many ways to go about making a level, but for this we'll make an image
# where we can simply draw the level and then generate a level based on that.
#
# # image platformer_tutorial_level.png
#
#
#
# To generate the level we'll loop thrugh all the pixels in the image and do
# something based on the color of the pixel.
#
# If it's white, it's air, so we'll skip it.
level_parent = Entity()
def make_level(texture):
    # destroy every child of the level parent.
    # This doesn't do anything the first time the level is generated, but if we want to update it several times
    # this will ensure it doesn't just create a bunch of overlapping entities.
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)

            # If it's black, it's solid, so we'll place a tile there.
            if col == color.black:
                Entity(parent=level_parent, position=(x,y), model='cube', origin=(-.5,-.5), color=color.gray, texture='white_cube', visible=True)
                if not collider:
                    collider = Entity(parent=level_parent, position=(x,y), model='cube', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    collider.scale_x += 1
            else:
                collider = None

            # If it's green, we'll place the player there
            if col == color.green:
                player.position = (x, y)

# ## Positioning the camera
#
# Set the camera to orthographic so there's no perspective
# Move the camera to the middle of the level and set the fov so the level fits nicely.
# Setting the fov on an orthigraphic camera means setting hoe many units vetically the camera can see.
camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16

# generate the level
make_level(load_texture('platformer_tutorial_level'))

# start the game
app.run()


# Optimizing colliders
# Adding playter graphics and animations
# Adding level graphics
