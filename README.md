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
- Default venv fils and dirs
- `main.py`: It is a default main.py file with some default (basic) code. 
- `dependencies.json`: contains all the dependencies.
- `setup.py`: It is the default automated program to install dependencies from a dependencies.json file.
- `settings.json`: Project settings file

## Configuration
The `settings.json` file in the virtual environment directory contains the configuration settings for the project. If you want, you can modify the following properties in the settings.json file:

- `"project-name"`: The name of the project [Default None]
- `"version"`: The version number of the project [Default "0.0.1"]
- `"creator-name"`: Your name or the creator's name [Default my name, "Srijan Bhattacharyya"]


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions to the `cbot` project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## NOTE:
- Please make sure to change the `"creator-name"` tag which is present at `mkvenv/defaults/settings.json` to your name. By default it has my name "Srijan Bhattacharyya".
