

# Transform 2d to 3d Images!

2d to 3d Image Transformer README

Created by Christopher Wycoff

This project takes 2d .jpeg images and transforms them to 3d displayable models.

Depending on the configuration it can do the following:

1.  Make raw STL files
    
2.  Demo full textured models of the transformed 2d >> 3d image.
    
3.  Make animated mp4 files of the 3d models.
    
4.  Make animated mp4 files of the 3d models affected by an audio file.
    
5.  Run a server and a web/browser interface to interact via a GUI with the program
    

  

Installation:

Requirements Python 3

  

To install:

-   Make sure Python 3 is installed on the machine.
    
-   If you do not want initially start the server comment out “python main.py” on line 10 of “install.sh”
    
-   Execute the file “install.sh”. This creates a virtual environment and installs the necessary packages. It also sets up the appropriate directory structure for the image processing pipeline. If line 10 is left uncommented it will also spin up the back end server of the GUI.
    
-   To create a new shell that has access to the virtual environment execute: “source tutorial-env/bin/activate” (on unix based system)
    
-   For more information on virtual environments see: [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
    
-   If you wish to start the front-end GUI start a new shell and execute the “start.sh” script and navigate to “[http://localhost:8000/](http://localhost:8000/)” in a browser.
    

  

To run via command line:

Example:

“python3 transform_command.py ./images/images_2d/pipew.jpeg“

  

The argument to transform_command.py should be the desired 2d image.

  

The “transform_command.py” file and specifically the “transform_image_command()” function can be modified (via uncommenting and modifying parameters) to change the configuration of what will be produced. The logic and function calls within the “transform_command.py” shows the pipeline that is created to process the 2d image into a 3d model/animation.

  

Every execution of the program creates a UUID associated with that execution and creates a file structure that belongs to that execution. If the “cleanup = True” parameter is set the files associated with that execution will be removed upon completion of the processing. (The thought behind this is to allow for use on a server with many users.z)

  

The files:

![](https://lh3.googleusercontent.com/6J2oDhEqGB-vOEsZYdMkuf8vgV020Rh3a3WZ0qRR007tyM50vxPYtxVQtzS-R0Y8its41JO8UAXQwC6v_xutlrTWQtWsL0fq5_KOXCyMkFwFF8xnzR-kHaqRvaVeIn1VAedf42DR)

-   transform_command.py is the hub that holds all the other files together.
    

  

-   transform_image.py is the hub for the GUI/server and can be configured similarly to how transform_command.py can be. However the result must be a .mp4 file unlike transform_command.py
    

  

-   Makestl.py, meshcreator.py, imageprep.py imageutils.py are used to make the STL file.
    

  

-   add_effects.py contains multiple functions that allow for different displays/animations of the 3d image
    

  

-   moviefy.py creates mp4 files from a series of .png files that are created in add_effects.py
    

  

-   main.py contains the logic for the back end of the GUI
    

  

-   The front_end directory contain the logic and html script for the front end of the GUI
    

  

Some of what I learned:

-   Gained greater perspective on what a model is and the data behind graphics.
    
-   Learned about STL files.
    
-   Better understood camera position and how graphic transformations work.
    
-   Discovered how to pass images and video files over the internet. For example base64 encoding.
    
-   Sharpened the skill of creating usable products.
    
-   Learned how audio encoding works and how to map audio amplitudes to graphic transformations

