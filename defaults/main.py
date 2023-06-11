import os


mainDir = os.path.abspath (os.path.dirname (__file__))
dependencies_file = os.path.join (mainDir, "dependencies.json")


import setup
setup.setup (setup.get_dependencies (dependencies_file))


if __name__ == "__main__":
    # write your code
    pass
