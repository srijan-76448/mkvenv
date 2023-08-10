import os, sys


def setup (mainDir: os.path):
    # Get the user's home directory
    home_dir = os.path.expanduser ("~")

    # Define the alias in ~/.bashrc
    python_path = sys.executable
    cmd = f"{python_path} {mainDir}"
    os.system (f"grep -qxF '{cmd}' ~/.bashrc || echo '{cmd}' >> ~/.bashrc")
