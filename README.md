Project mkvenv
==============
It is a modified version of `venv` module of python.

Aditional Features:
-----------------
 • While creating venv, it will also create some aditional files like `main.py`, `dependencies.json`, `setup.py` which comes handy for high level coding.<br>
 • It also creats a directory named `.vscode` with a file with the same name as the name of your project with an extention `.code-workspace`.

Brief Explanation on each extra file:
-------------------------------------
 • `dependencies.json`<br>
This is a json file where you need to put all the dependencies of your project in a specific order. For example:<br>
{
    "cv2": "opencv-python"
}<br>
In the above example, for importing you need to write `cv2` but wile installing you need to write `opencv-python`.<br>

 • `setup.py`<br>
This file will take the dependencies from the json file named `dependencies.json` and go through a try and except loop for each and every dependencies mentioned in it. It will try to import the module first, if it can't then it will install it using pip.<br>
For examle, in case of importing opencv, it will try to import opencv using the command `import cv2`, if it fails, it will raise an `ImportError`, hence it will install opencv using the command `pip install opencv-python`.<br>

 • `main.py`<br>
This is the main file where it will write some default codes, like importing the `setup.py` file and instructing it to install the dependencies.

 • `.vscode`<br>
It is only for vscode uers it will make a workspace config file with the same name as the name of your project with an extention `.code-workspace`.

How to install and set everything up ?
--------------------------------------
 • At first install the program using `git clone` or downloading it as zip and unzipping it.<br>
 • Then run the `main.py` file for once. On the first run, it will add a line in your .bashrc file which will allow to run this whole script with a single command [default command: `mkvenv`]. It will also show the help section by default.

NOTE:
-----
 • PLEASE DON'T EDIT THE SOURCE CODE IF DON'T KNOW ANYTHING ABOUT IT.<BR>
 • THIS PROGRAM IS NOT DESIGNED FOR WINDOWS, SO PLEASE USE IT ON LINUX ONLY.

Credits
-------
This program is created by Srijan Bhattacharyya. This program was created to automate some basic things and educational purpose only.
