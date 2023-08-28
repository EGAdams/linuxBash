import os
import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode('utf-8').strip()
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output.decode('utf-8').strip()}")


def remove_submodule(submodule_name):
    # Step 1: Remove the submodule entry from the index
    run_command(f"git rm --cached {submodule_name}")

    # Step 2: Remove the submodule configuration from .gitmodules
    with open(".gitmodules", "r") as f:
        lines = f.readlines()

    with open(".gitmodules", "w") as f:
        in_submodule_section = False
        for line in lines:
            if line.strip().startswith(f"[submodule \"{submodule_name}\"]"):
                in_submodule_section = True
            elif line.strip() == "" and in_submodule_section:
                in_submodule_section = False
            elif not in_submodule_section:
                f.write(line)

    # Step 3: Remove the submodule configuration from .git/config
    if os.path.exists(".git/config"):
        with open(".git/config", "r") as f:
            lines = f.readlines()

        with open(".git/config", "w") as f:
            in_submodule_section = False
            for line in lines:
                if line.strip().startswith(f"[submodule \"{submodule_name}\"]"):
                    in_submodule_section = True
                elif line.strip() == "" and in_submodule_section:
                    in_submodule_section = False
                elif not in_submodule_section:
                    f.write(line)

    # Step 4: Commit the changes
    run_command("git add .gitmodules")
    run_command(f"git commit -m \"Removed {submodule_name} submodule\"")

    print(f"Submodule {submodule_name} has been removed. You can now re-add it if desired.")


if __name__ == "__main__":
    submodule_name = "project-management"
    remove_submodule(submodule_name)

