import os, json, pip


def get_dependencies (dependencies_file_path: os.path) -> dict:
    with open (dependencies_file_path) as f:
        return json.load (f)


def main (mainDir: os.path):
    requirements_file_path = os.path.join (mainDir, "dependencies.json")

    pkgs = get_dependencies (requirements_file_path)

    for pkg in pkgs.keys ():
        try:
            exec (f"import {pkg}")

        except ImportError:
            pip.main (['install', pkgs [pkg]])
