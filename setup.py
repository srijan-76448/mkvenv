import os, sys

def setup () -> None:
    # Define the alias in ~/.bashrc
    mainDir = os.path.abspath (__file__)
    cmd = f"/usr/bin/python3 {mainDir}"

    os.system (f"grep -qxF '{cmd}' ~/.bashrc || echo '{cmd}' >> ~/.bashrc")
