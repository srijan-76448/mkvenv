# mkvenv - Python Coding Virtual Environment Creator Bot

`mkvenv` is a Python-based tool to create a basic Python coding virtual environment with the specified name and path. It automates the setup process by creating the necessary files and directories for the virtual environment, including a main.py file, setpy.py file, dependencies.json file, and settings.json file.

## Getting Started
### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SrijanBhattacharyya/mkvenv.git
2. First run:
    ```bash
    python3 mkvenv/main.py
## Usage
1. Run the mkvenv script:
    ```bash
    mkvenv
2. Follow the on-screen instructions to provide the project name/path, and other details.
3. mkvenv will create the project directory, generate the necessary files, and set up the basic Python coding virtual environment.

## Directory Structure
- `compiler.sh`: Shell script to compile and run the `program.c` file
- `program.c`: Sample C program to print "Hello, World!"
- `settings.json`: Project settings file

## Configuration
The `settings.json` file in the virtual environment directory contains the configuration settings for the project. If you want, you can modify the following properties in the settings.json file:

- `"project-name"`: The name of the project [Default ""]
- `"version"`: The version number of the project [Default "0.0.1"]
- `"creator-name"`: Your name or the creator's name [Default my name, "Srijan Bhattacharyya"]


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions to the `cbot` project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## NOTE:
- Please make sure to change the `"creator-name"` tag which is present at `mkvenv/defaults/settings.json` to your name. By default it has my name "Srijan Bhattacharyya".
