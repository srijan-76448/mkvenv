import os, sys, venv, time, json, setup

setup.setup()

mainDir = os.path.dirname(os.path.abspath(__file__))
man_file = os.path.join(mainDir, "man.txt")
app_info_file = os.path.join(mainDir, "settings.json")


def get_app_info() -> dict:
    with open(app_info_file) as f:
        return dict(json.load(f))["App-Settings"]


def get_env_path(flag_only: bool = False) ->(str|None):
    args = sys.argv [1::]

    if args == []:
        help()

    if flag_only:
        for arg in args:
            if arg [0] == '-':
                return arg

    else:
        for arg in args:
            if arg [0] != '-':
                if "/" not in arg:
                    arg = os.path.join(os.getcwd(), arg)

                return arg


def check_flag(cmd: str) -> None:
    if cmd == '-t' or cmd == '-test':
        time.sleep(10)
        os.system(f"rm -r '{env_path}'")
        print(f"\033[1;31m[+] Removed '{get_env_path()}' successfully.\033[0m")

    if cmd == '-h' or cmd == '--help':
        help()

    if cmd == '-v' or cmd == '--version':
        version()


def mk_code_env() -> None:
    if os.path.exists(env_path):
        print(f"\033[1;31m[-] PathAlreadyExistsError: Can't create venv '{env_path}': File already exists.\033[0m")
        exit()

    else: venv.create(env_path, system_site_packages = False)


def check_if_created() -> bool:
    req = [
        'include',
        'lib',
        'lib64',
        'bin',
        'pyvenv.cfg'
    ]
    found = {}

    for r in req:
        found [r] = False

    if os.path.exists(env_path):
        ld = os.listdir(env_path)

        for i in ld:
            if i in req:
                found [i] = True

            else:
                found [i] = False

    if found ['include'] and found ['lib'] and found ['lib64'] and found ['bin'] and found ['pyvenv.cfg']: return True
    else: return False


def get_default_code (mainDir: os.path) -> dict:
    default_cfg_files_dir = os.path.join(mainDir, "defaults")
    list_dir = os.listdir(default_cfg_files_dir)
    data = {}

    os.chdir(default_cfg_files_dir)

    for elem in list_dir:
        with open(elem, "r") as data_file:
            if "code-workspace" in elem:
                elem = os.path.join(".vscode", elem)

            if ".json" in elem:
                data [elem] = json.load(data_file)

            else:
                data [elem] = data_file.readlines()

    return data


def mod_cfg(data: dict):
    # modifying the code-workspace file for the new venv
    cfg = data [".vscode/code-workspace.json"]

    cfg ["folders"]["path"]                             = env_path
    cfg ["settings"]["terminal.integrated.cwd"]         = env_path
    cfg ["settings"]["python.defaultInterpreterPath"]   = os.path.join(env_path, 'bin', "python3")

    cfg = data ["settings.json"]

    cfg ["App-Settings"]["project-name"] = os.path.split(env_path)[1]

    return data


def config_code_env(data: dict):
    os.chdir(env_path)

    for file_path in data.keys():
        file = file_path
        try:
            os.makedirs(os.path.dirname(file_path))
            file = os.path.join(os.path.dirname(file_path), f"{os.path.split(env_path)[1]}.code-workspace")

        except FileNotFoundError:
            pass

        with open(file, "w") as f:
            if ".json" in file_path:
                json.dump(data [file_path], f, indent = 4)

            else:
                f.writelines(data [file_path])


def help() -> None:
    # with open(man_file) as f:
    #     man = f.read().replace("<CREATOR-NAME>", app_info ["creator-name"])

    # print(man)

    print("can't provide manual page")
    exit()


def version() -> None:
    print(f"{app_info ['name']} {app_info ['version']}")
    exit()


def main():
    global env_path, data, app_info

    env_path = get_env_path()
    data = mod_cfg(get_default_code(mainDir))
    app_info = get_app_info()

    mk_code_env()

    if check_if_created(): config_code_env(data)
    else: print(f'\033[1;31m[-] Venv not created.\033[0m'); exit()

    print(f'\033[1;32m[+] Venv created successfully.\033[0m')
    print(f"\033[1mPath to venv: {env_path}\033[0m")

    check_flag(get_env_path(True))


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f'\033[1;31m[-] {e}\033[0m')
