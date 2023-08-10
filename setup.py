import os, sys


def setup () -> None:
    # Get the user's home directory
    home_dir = os.path.expanduser ("~")

    # Define the alias in ~/.bashrc
    mainDir = os.path.abspath (__file__)
    python_path = sys.executable
    cmd = f"{python_path} {mainDir}"
    os.system (f"grep -qxF '{cmd}' ~/.bashrc || echo '{cmd}' >> ~/.bashrc")
