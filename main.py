import os, sys, venv, time, json, setup

setup.setup (os.path.abspath (__file__))

mainDir = os.path.dirname (os.path.abspath (__file__))


def get_path (flag_only: bool = False):
    args = sys.argv [1::]

    if args == []:
        help ()

    if flag_only:
        for arg in args:
            if arg [0] == '-':
                return arg

    else:
        for arg in args:
            if arg [0] != '-':
                if "/" not in arg:
                    arg = os.path.join (os.getcwd (), arg)

                return arg


def get_dir_name (dir_path: os.path):
    dir_name = os.path.split (dir_path)

    return dir_name [-1]


def make_venv (path_to_dir: os.path):
    if os.path.exists (path_to_dir):
        print (f"\033[1;31m[-] PathAlreadyExistsError: Can't create venv '{path_to_dir}': File already exists.\033[0m")
        exit ()

    else:
        venv.create (path_to_dir, system_site_packages = False)


def check_if_created (path_to_dir: os.path):
    default_sub_dirs_in_venv = ['include', 'lib', 'lib64', 'bin', 'pyvenv.cfg']
    found = {'include': False, 'lib': False, 'lib64': False, 'bin': False, 'pyvenv.cfg': False}

    if os.path.exists (path_to_dir):
        ld = os.listdir (path_to_dir)

    for i in ld:
        if i in default_sub_dirs_in_venv:
            found [i] = True

        else:
            found [i] = False

    else:
        if found ['include'] and found ['lib'] and found ['lib64'] and found ['bin'] and found ['pyvenv.cfg']: return True
        else: return False


def check_flag (cmd: str, path: os.path):
    if cmd == '-t' or cmd == '-test':
        time.sleep (10)
        os.system (f"rm -r '{path}'")
        print (f"\033[1;31m[+] Removed '{get_path ()}' successfully.\033[0m")

    if cmd == '-h' or cmd == 'help':
        help ()


def get_data  (mainDir: os.path) -> dict:
    default_cfg_files_dir = os.path.join (mainDir, "defaults")
    list_dir = os.listdir (default_cfg_files_dir)
    data = {}

    os.chdir (default_cfg_files_dir)

    for elem in list_dir:
        with open (elem, "r") as data_file:
            if "code-workspace" in elem:
                elem = os.path.join (".vscode", elem)

            if ".json" in elem:
                data [elem] = json.load (data_file)

            else:
                data [elem] = data_file.readlines ()

    return data


def make_default_cfg (data: dict, workingDir: os.path):
    os.chdir (workingDir)

    for file_path in data.keys ():
        file = file_path
        try:
            os.makedirs (os.path.dirname (file_path))
            file = os.path.join (os.path.dirname (file_path), f"{os.path.split (workingDir)[1]}.code-workspace")

        except FileNotFoundError:
            pass

        with open (file, "w") as f:
            if ".json" in file_path:
                json.dump (data [file_path], f, indent = 4)

            else:
                f.writelines (data [file_path])


# modifying the code-workspace file for the new venv
def mod_cfg (data: dict, workingDir: os.path):
    cfg = data [".vscode/code-workspace.json"]

    cfg ["folders"]["path"]                             = workingDir
    cfg ["settings"]["terminal.integrated.cwd"]         = workingDir
    cfg ["settings"]["python.defaultInterpreterPath"]   = os.path.join (workingDir, 'bin', "python3")

    return data


def help ():
    h = '''syntax: mkvenv -flag path-to-venv

FLAGS:
  -h, -help        help
  -t, -test        test

Made by Srijan Bhattacharyya.'''

    print (h)
    exit ()


def main ():
    path = get_path ()
    data = mod_cfg (get_data (mainDir), path)

    make_venv (path)

    if check_if_created (path):
        check_if_created (path)
        make_default_cfg (data, path)

    print (f'\033[1;32m[+] Venv created successfully.\033[0m')
    print (f"\033[1mPath to venv: {path}\033[0m")

    check_flag (get_path (True), path)


if __name__ == "__main__":
    try:
        main ()

    except Exception as e:
        print (f'\033[1;31m[-] {e}\033[0m')