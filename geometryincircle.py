import bpy
from math import sin, cos, pi

#geometry_in_circle v0.1

selection = bpy.context.selected_objects

o =[]
j = -1
spacing = 13
radius = 4

for i in selection:
    o.append(str(i.name))
    
for i in range(0,360,spacing):
        angle = pi*i/180
        x = sin(angle)*radius
        y = cos(angle)*radius
        try:
            bpy.data.objects[o[j]].location = [x,y,0]
            bpy.data.objects[o[j]].rotation_euler= [0,0,-angle]
        except IndexError:
            pass
        j-=1