import os, sys

def setup() -> None:
    # Define the alias in ~/.bashrc
    mainDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main.py')
    cmd = f"alias mkvenv='/usr/bin/python3 {mainDir}'"

    os.system(f"grep -qxF '{cmd}' ~/.bashrc || echo '{cmd}' >> ~/.bashrc")