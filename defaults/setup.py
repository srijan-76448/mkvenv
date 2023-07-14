import os, json, pip


def get_dependencies (dependencies_file_path: os.path) -> dict:
    with open (dependencies_file_path) as f:
        return json.load (f)


def main (mainDir: os.path):
    requirements_file_path = os.path.join (mainDir, "dependencies.json")
    pkgs = get_dependencies (requirements_file_path)

    for pkg, pkg_name in pkgs.items():
        if pkg != "keyword-for-importing":
            try:
                exec (f"import {pkg}")
                print (f"{pkg} is already installed")

            except ImportError:
                print (f"{pkg} is not installed, installing...")

                try:
                    # Use pip to install the package
                    pip.main (["install", pkg_name)
                    print (f"{pkg} has been installed successfully")

                except Exception as e:
                    print (f"Error occurred while installing {pkg}: {str(e)}")
