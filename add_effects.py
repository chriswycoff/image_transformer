# from matplotlib import markers
from pyvista import examples
# import vtkplotlib as vpl
# from stl.mesh import Mesh
# from mpl_toolkits.mplot3d import Axes3D
import math
import sys
import numpy as np
import pyvista as pv
# import uuid
import os

from pyvista.plotting import camera
from pyvista.utilities.helpers import row_array

### code below using vtkplotlib DOES work. however using was my first attempt however 
### as I continued to add features it became clunkier and I found pyvista 
### was a superior (and in my opinion more pythonic) API
# from matplotlib import cm

# def find_mins_maxs(obj):
#     minx = obj.x.min()
#     maxx = obj.x.max()
#     miny = obj.y.min()
#     maxy = obj.y.max()
#     minz = obj.z.min()
#     maxz = obj.z.max()
#     return minx, maxx, miny, maxy, minz, maxz


# def make_images(double = False, demo = False ):

#     # path = sys.argv[1]
#     path = "acs.stl"
#     # Read the STL using numpy-stl
#     mesh = Mesh.from_file(path)
#     mesh.rotate([0.0, 0.0, 0.5], math.radians(180))
#     if double:
#         mesh2 = Mesh.from_file(path)
#         mesh2.rotate([0.0, 0.0, 0.5], math.radians(180))
#         dim2 = find_mins_maxs(mesh2)
#         mesh2.translate([dim2[1]-dim2[0],0,0])

#     # for i in range(360,10):
#     #     mesh.rotate([0.0, 0.5, 0.0], math.radians(i))
#     #     # Plot the mesh
#     #     vpl.mesh_plot(mesh)

#     #     vpl.mesh_plot(mesh, color="blue")

#     #     # Show the figure
#     #     image_name = "hopeitworks" + i +".jpg"
#     #     vpl.save_fig(image_name)
#     #     # vpl.show()

#     # Plot the mesh
#     # vpl.mesh_plot(mesh)
#     mesh.rotate([0.0, 0.5, 0.0], math.radians(180))

#     if double:
#         if demo:
#             vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
#             vpl.mesh_plot(mesh2, scalars=mesh.x, cmap="rainbow")

#             vpl.show()

#         if not demo: 
#             for i in range(1):
#                 mesh.rotate([0.0, 0.5, 0.0], math.radians(30))
#                 mesh.rotate([0.5, 0.0, 0.0], math.radians(2.5))
#                 mesh2.rotate([0.0, 0.5, 0.0], math.radians(30))
#                 mesh2.rotate([0.5, 0.0, 0.0], math.radians(2.5))
#                 # Plot the mesh
#                 # vpl.mesh_plot(mesh)
#                 # vpl.mesh_plot(mesh, color="green")
#                 vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
#                 vpl.mesh_plot(mesh2, scalars=mesh.x, cmap="rainbow")

#                 # Show the figure
#                 if len(str(i)) == 1:
#                     image_name = "testimages/hopeitworks" + "00" + str(i) +".png"
#                 elif len(str(i)) == 1:
#                     image_name = "testimages/hopeitworks" + "0" + str(i) +".png"
#                 else:
#                     image_name = "testimages/hopeitworks" + str(i) +".png"
                
#                 vpl.save_fig(image_name,magnification=2)
#                 vpl.close()
#     else:
#         if demo:
#             path = vpl.data.ICONS["Right"]
#             texture_map = vpl.TextureMap(path, interpolate=True)
#             vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
            
#             vpl.surface(1,2,3,texture_map=texture_map)
            
            
#             vpl.show()

#         if not demo: 
#             for i in range(1):
#                 mesh.rotate([0.0, 0.5, 0.0], math.radians(30))
#                 mesh.rotate([0.5, 0.0, 0.0], math.radians(2.5))
#                 # Plot the mesh
#                 # vpl.mesh_plot(mesh)
#                 # vpl.mesh_plot(mesh, color="green")
#                 vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
#                 # Show the figure
#                 if len(str(i)) == 1:
#                     image_name = "testimages/hopeitworks" + "00" + str(i) +".png"
#                 elif len(str(i)) == 1:
#                     image_name = "testimages/hopeitworks" + "0" + str(i) +".png"
#                 else:
#                     image_name = "testimages/hopeitworks" + str(i) +".png"
                
#                 vpl.save_fig(image_name,magnification=2)
#                 vpl.close()
                

def pyvista_test():
    plotter = pv.Plotter(lighting='none')
    mesh = pv.read("acs.stl")
    plotter.background_color = 'brown'
    mesh.rotate_z(180)
    texacs = pv.read_texture("../images/acs.jpg")
    
    mesh.texture_map_to_plane(inplace=True)
    tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    plotter.add_mesh(mesh, texture=texacs)
    
    plotter.show()
    # mesh.save("acs2.vtk")
    # might have better way

def pyvista_test2():
    plotter = pv.Plotter(off_screen=False)
    mesh = pv.read("./images/images_3d/cool_lion.stl")
    plotter.background_color = 'brown'
    mesh.rotate_x(0)
    texlion = pv.read_texture("./images/images_2d/cool_lion.jpeg")
    texlion.flip(1)
    mesh.texture_map_to_plane(inplace=True)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    # plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh, texture=texlion)
    
    cam = plotter.camera

    cam.azimuth = 100
    # 
    plotter.show()
    # for i in range(10):
    #     plotter = pv.Plotter(lighting='none',off_screen=True)
    #     mesh.rotate_x(10)
    #     plotter.add_mesh(mesh, texture=texlion)
    #     plotter.show(screenshot='./images/images_effected/lion' + str(i) + '.png')
    #     # plotter.remove_actor(actor)

def pyvista_test3():
    plotter = pv.Plotter(off_screen=False)
    mesh = pv.read("./images/images_3d/snake.stl")
    plotter.background_color = 'brown'
    # mesh.rotate_x(0)
    texlion = pv.read_texture("./images/images_2d/snake.jpeg")
    texlion.flip(1)
    texlion.flip(0)
    mesh.texture_map_to_plane(inplace=True)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    # plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh, texture=texlion)
    
    cam = plotter.camera

    cam.azimuth = 100
    # 
    plotter.show()

def pyvista_test4():
    plotter = pv.Plotter(off_screen=False)
    mesh = pv.read("./images/images_3d/lion.stl")
    mesh2 = pv.read("./images/images_3d/lion.stl")
    plotter.background_color = 'brown'
    # mesh.rotate_x(0)
    # print(mesh2._get_attrs())
    # above prints attributes to know how much to translate
    mesh2.rotate_y(180)
    mesh2.translate((140,0,0))
    mesh2.texture_map_to_plane(inplace=True)
    texlion = pv.read_texture("./images/images_2d/cool_lion.jpeg")
    texlion.flip(1)
    texlion.flip(0)
    mesh.texture_map_to_plane(inplace=True)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    # plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh2, texture=texlion)
    
    cam = plotter.camera

    cam.roll = 240 
    cam.azimuth = 45
    cam.elevation = 40
    # 
    plotter.show()

def pyvista_test5(imagefile,newfile):
    plotter = pv.Plotter(off_screen=False)
    mesh = pv.read("./images/images_3d/lion.stl")
    mesh2 = pv.read("./images/images_3d/lion.stl")
    plotter.background_color = 'brown'
    # mesh.rotate_x(0)
    # print(mesh2._get_attrs())
    # above prints attributes to know how much to translate
    mesh2.rotate_y(180)
    mesh2.translate((140,0,0))
    mesh2.texture_map_to_plane(inplace=True)
    texlion = pv.read_texture("./images/images_2d/cool_lion.jpeg")
    texlion.flip(1)
    texlion.flip(0)
    mesh.texture_map_to_plane(inplace=True)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    # plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh2, texture=texlion)
    
    cam = plotter.camera

    cam.roll = 240 
    cam.azimuth = 45
    cam.elevation = 40
    # 
    plotter.show()

def add_image():
    plotter = pv.Plotter(lighting='none')
    mesh = pv.read("acs.stl")
    plotter.background_color = 'brown'
    mesh.rotate_z(180)
    texacs = pv.read_texture("../images/acs.jpg")
    mesh.texture_map_to_plane(inplace=True)
    tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    plotter.add_mesh(mesh, texture=texacs)
    
    plotter.show()

def create_movie_old(two_d_image,three_d_image,double=False,texture_img=None, \
    background_image=None, background_color=None,lighting=None,unique_id = 1, \
    frames=10):
    plotter = pv.Plotter(off_screen=True)
    mesh = pv.read(three_d_image)
    plotter.background_color = 'brown'
    # mesh.rotate_z(180)
    the_tex = pv.read_texture(two_d_image)
    the_tex.flip(0)
    the_tex.flip(1)
    mesh.texture_map_to_plane(inplace=True)
    # mesh.rotate_y(30)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    actor = plotter.add_mesh(mesh, texture=the_tex)
    
    # plotter.show()
    # unique_id = uuid.uuid4()
    os.mkdir('./images/images_effected/'+ str(unique_id))
    counter = 0
    increment = 360/frames
    for i in range(frames):
        plotter = pv.Plotter(off_screen=True)
        plotter.background_color = "white"
        # mesh.rotate_x(360/frames)
        plotter.add_mesh(mesh, texture=the_tex)
        cam = plotter.camera
        counter += increment
        cam.azimuth = counter
        if len(str(i)) == 1:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "00" + str(i) + '.png'
        elif len(str(i)) == 2:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "0" + str(i) + '.png'
        else:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + str(i) + '.png'
        plotter.show(screenshot=image_name)
        # plotter.remove_actor(actor)

def create_movie(two_d_image,three_d_image,double=False,texture_img=None, \
    background_image=None, background_color=None,lighting=None,unique_id = 1, \
    frames=10):
    plotter = pv.Plotter(off_screen=True)
    mesh = pv.read(three_d_image)
    plotter.background_color = 'brown'
    # mesh.rotate_z(180)
    the_tex = pv.read_texture(two_d_image)
    the_tex.flip(0)
    the_tex.flip(1)
    mesh.texture_map_to_plane(inplace=True)
    # mesh.rotate_y(30)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    actor = plotter.add_mesh(mesh, texture=the_tex)
    
    # plotter.show()
    # unique_id = uuid.uuid4()
    os.mkdir('./images/images_effected/'+ str(unique_id))
    counter = 0
    increment = 360/frames
    # to make face forward
    # cam.roll = 240 
    # cam.azimuth = 45
    # cam.elevation = 40
    azimuth_array = [240]
    roll_array = [45]
    elevation_array = [40]
    for i in range(frames//2):
        azimuth_array.append(azimuth_array[i]+1)

    for i in range(frames//2,frames):
        azimuth_array.append(azimuth_array[i])

    for i in range(frames//2):
        elevation_array.append(40)

    for i in range(frames//2,frames):
        elevation_array.append(elevation_array[i]+1)
    az_counter = 1
    elevation_counter = 1
    for i in range(frames):
        plotter = pv.Plotter(off_screen=True)
        plotter.background_color = "white"
        # mesh.rotate_x(360/frames)
        plotter.add_mesh(mesh, texture=the_tex)
        cam = plotter.camera
        counter += increment
        # cam.azimuth = azimuth_array[i]
        # cam.roll = 240 
        # cam.elevation = elevation_array[i]
        
        cam.roll = 240 
        cam.azimuth = 45
        cam.elevation = 40

        if i < frames* (1/4):
            cam.azimuth += az_counter
            az_counter += 1
        elif i < frames * (1/2):
            cam.azimuth += az_counter
            az_counter -= 1
        elif i < frames * (3/4):
            # print("herer")
            cam.elevation += elevation_counter
            elevation_counter += 1
        else:
            cam.elevation += elevation_counter
            elevation_counter -= 1

        if len(str(i)) == 1:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "00" + str(i) + '.png'
        elif len(str(i)) == 2:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "0" + str(i) + '.png'
        else:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + str(i) + '.png'
        plotter.show(screenshot=image_name)

# nice spinning effect
def create_movie2(two_d_image,three_d_image,double=False,texture_img=None, \
    background_image=None, background_color=None,lighting=None,unique_id = 1, \
    frames=10):
    plotter = pv.Plotter(off_screen=True)
    mesh = pv.read(three_d_image)
    plotter.background_color = 'brown'
    # mesh.rotate_z(180)
    the_tex = pv.read_texture(two_d_image)
    the_tex.flip(0)
    the_tex.flip(1)
    mesh.texture_map_to_plane(inplace=True)
    # mesh.rotate_y(30)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    actor = plotter.add_mesh(mesh, texture=the_tex)
    
    # plotter.show()
    # unique_id = uuid.uuid4()
    os.mkdir('./images/images_effected/'+ str(unique_id))
    counter = 0
    increment = 360/frames

    az_counter = 45
    elevation_counter = 40
    roll_counter = 240
    counter = 1
    for i in range(frames):
        plotter = pv.Plotter(off_screen=True)
        plotter.background_color = "white"
        # mesh.rotate_x(360/frames)
        plotter.add_mesh(mesh, texture=the_tex)
        cam = plotter.camera
        # az_counter += 1
        roll_counter += 1
        
        cam.roll = roll_counter 
        cam.azimuth = az_counter
        cam.elevation = elevation_counter
        



        if len(str(i)) == 1:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "00" + str(i) + '.png'
        elif len(str(i)) == 2:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "0" + str(i) + '.png'
        else:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + str(i) + '.png'
        plotter.show(screenshot=image_name)

# nice spinning effect
# double sided
def create_movie3(two_d_image,three_d_image,double=False,texture_img=None, \
    background_image=None, background_color=None,lighting=None,unique_id = 1, \
    frames=10):
    plotter = pv.Plotter(off_screen=True)
    mesh = pv.read(three_d_image)
    plotter.background_color = 'brown'
    # mesh.rotate_z(180)
    the_tex = pv.read_texture(two_d_image)
    the_tex2 = pv.read_texture(two_d_image)
    the_tex.flip(0)
    the_tex.flip(1)
    mesh.texture_map_to_plane(inplace=True)

    mesh2 = pv.read(three_d_image)
    mesh2.rotate_y(180)
    mesh2.translate((140,0,0))
    mesh2.texture_map_to_plane(inplace=True)
    # mesh.rotate_y(30)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    plotter.add_mesh(mesh, texture=the_tex)
    the_tex2.flip(1)
    plotter.add_mesh(mesh2, texture=the_tex2)
    # plotter.show()
    # unique_id = uuid.uuid4()
    os.mkdir('./images/images_effected/'+ str(unique_id))
    counter = 0
    increment = 360/frames

    az_counter = 45
    elevation_counter = 40
    roll_counter = 240
    counter = 1
    for i in range(frames):
        plotter = pv.Plotter(off_screen=True)
        plotter.background_color = "white"
        # mesh.rotate_x(360/frames)
        plotter.add_mesh(mesh, texture=the_tex)
        plotter.add_mesh(mesh2, texture=the_tex2)
        cam = plotter.camera
        # az_counter += 1
        roll_counter += 1
        
        cam.roll = roll_counter 
        cam.azimuth = az_counter
        cam.elevation = elevation_counter
        



        if len(str(i)) == 1:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "00" + str(i) + '.png'
        elif len(str(i)) == 2:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + "0" + str(i) + '.png'
        else:
            image_name = './images/images_effected/'+ str(unique_id)+"/" + "movie" + str(i) + '.png'
        plotter.show(screenshot=image_name)


def pyvista_command(stl_image,two_d_image):
    plotter = pv.Plotter(off_screen=False)
    mesh = pv.read(stl_image)
    mesh2 = pv.read(stl_image)
    plotter.background_color = 'brown'
    # mesh.rotate_x(0)
    # print(mesh2._get_attrs())
    # above prints attributes to know how much to translate
    mesh2.rotate_y(180)
    mesh2.translate((140,0,0))
    mesh2.texture_map_to_plane(inplace=True)
    texlion = pv.read_texture(two_d_image)
    texlion2 = pv.read_texture(two_d_image)
    texlion.flip(1)
    texlion.flip(0)
    mesh.texture_map_to_plane(inplace=True)
    # tex = examples.download_masonry_texture()
    # mesh.plot(texture=texacs)
    # plotter.add_mesh(mesh, texture=texlion)
    plotter.add_mesh(mesh, texture=texlion)
    texlion2.flip(1)
    plotter.add_mesh(mesh2,texture=texlion2)
    
    cam = plotter.camera

    cam.roll = 240 
    cam.azimuth = 45
    cam.elevation = 40
    # 
    plotter.show()

# def main():
#     # make_images(demo=True)
#     # pyvista_test2()
#     two_d_image = "./images/images_2d/cool_lion.jpeg"
#     three_d_image = "./images/images_3d/cool_lion.stl"
#     create_movie(two_d_image,three_d_image)

#     pass

# main()
# pyvista_test2()
# pyvista_test3()
if __name__ == "__main__":
    pyvista_test4()
