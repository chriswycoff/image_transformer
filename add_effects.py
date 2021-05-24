# from matplotlib import markers
from matplotlib.pyplot import colormaps
from pyvista import examples
import vtkplotlib as vpl
from stl.mesh import Mesh
# from mpl_toolkits.mplot3d import Axes3D
import math
import sys
import numpy as np
import pyvista as pv
# from matplotlib import cm

def find_mins_maxs(obj):
    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()
    return minx, maxx, miny, maxy, minz, maxz


def make_images(double = False, demo = False ):

    # path = sys.argv[1]
    path = "acs.stl"
    # Read the STL using numpy-stl
    mesh = Mesh.from_file(path)
    mesh.rotate([0.0, 0.0, 0.5], math.radians(180))
    if double:
        mesh2 = Mesh.from_file(path)
        mesh2.rotate([0.0, 0.0, 0.5], math.radians(180))
        dim2 = find_mins_maxs(mesh2)
        mesh2.translate([dim2[1]-dim2[0],0,0])

    # for i in range(360,10):
    #     mesh.rotate([0.0, 0.5, 0.0], math.radians(i))
    #     # Plot the mesh
    #     vpl.mesh_plot(mesh)

    #     vpl.mesh_plot(mesh, color="blue")

    #     # Show the figure
    #     image_name = "hopeitworks" + i +".jpg"
    #     vpl.save_fig(image_name)
    #     # vpl.show()

    # Plot the mesh
    # vpl.mesh_plot(mesh)
    mesh.rotate([0.0, 0.5, 0.0], math.radians(180))


    if double:
        if demo:
            vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
            vpl.mesh_plot(mesh2, scalars=mesh.x, cmap="rainbow")

            vpl.show()

        if not demo: 
            for i in range(1):
                mesh.rotate([0.0, 0.5, 0.0], math.radians(30))
                mesh.rotate([0.5, 0.0, 0.0], math.radians(2.5))
                mesh2.rotate([0.0, 0.5, 0.0], math.radians(30))
                mesh2.rotate([0.5, 0.0, 0.0], math.radians(2.5))
                # Plot the mesh
                # vpl.mesh_plot(mesh)
                # vpl.mesh_plot(mesh, color="green")
                vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
                vpl.mesh_plot(mesh2, scalars=mesh.x, cmap="rainbow")

                # Show the figure
                if len(str(i)) == 1:
                    image_name = "testimages/hopeitworks" + "00" + str(i) +".png"
                elif len(str(i)) == 1:
                    image_name = "testimages/hopeitworks" + "0" + str(i) +".png"
                else:
                    image_name = "testimages/hopeitworks" + str(i) +".png"
                
                vpl.save_fig(image_name,magnification=2)
                vpl.close()
    else:
        if demo:
            path = vpl.data.ICONS["Right"]
            texture_map = vpl.TextureMap(path, interpolate=True)
            vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
            
            vpl.surface(1,2,3,texture_map=texture_map)
            
            
            vpl.show()

        if not demo: 
            for i in range(1):
                mesh.rotate([0.0, 0.5, 0.0], math.radians(30))
                mesh.rotate([0.5, 0.0, 0.0], math.radians(2.5))
                # Plot the mesh
                # vpl.mesh_plot(mesh)
                # vpl.mesh_plot(mesh, color="green")
                vpl.mesh_plot(mesh, scalars=mesh.x, cmap="rainbow")
                # Show the figure
                if len(str(i)) == 1:
                    image_name = "testimages/hopeitworks" + "00" + str(i) +".png"
                elif len(str(i)) == 1:
                    image_name = "testimages/hopeitworks" + "0" + str(i) +".png"
                else:
                    image_name = "testimages/hopeitworks" + str(i) +".png"
                
                vpl.save_fig(image_name,magnification=2)
                vpl.close()
                

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

    


def main():
    # make_images(demo=True)
    
    pyvista_test()
    pass

main()