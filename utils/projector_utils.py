#!/usr/bin/env python
import subprocess
import importlib
import json
import os
from tabulate import tabulate


def launch_project(projectdir, editor, terminal):
    try:
        editor_handler = importlib.import_module(
            f"utils.editors.{editor}", package=__name__
        )
    except ImportError as e:
        print(f"could not find module for editor: {editor} {e}")
        exit(-1)
    if terminal is not None:
        try:
            terminal_handler = importlib.import_module(
                f"utils.terminals.{terminal}", package=__name__
            )
        except ImportError:
            print(f"could not find module for terminal: {terminal}")
            exit(-1)
    if editor_handler.needs_kill():
        editor_handler.kill()
    flake = open(f"{projectdir}flake.nix")
    launch_command = (
        ["nix", "develop", f"{projectdir}", "--command"]
        + editor_handler.launch_command(projectdir)
        + ["return"]
    )
    if terminal is not None:
        launch_command = terminal_handler.generate_launch(launch_command)
    subprocess.run(launch_command)


def ensureFile(save_path):
    if not os.path.exists(save_path):
        with open(save_path, "w") as new_file:
            new_file.write("[]")


def load_projects(save_path):
    ensureFile(save_path)
    with open(save_path, "r") as projects:
        try:
            return json.load(projects)
        except JSONDecodeError:
            print("could not parse save file, backing up old one, and defaulting")
            exit(-1)


def save_projects(save_path, save_data):
    sorted_list = sorted(save_data, key=lambda d: d["name"])
    with open(save_path, "w") as projects:
        json.dump(save_data, projects)


def retrive_project(projects_data, project_name):
    for project in projects_data:
        if project["name"] == project_name:
            return project
    return None


def add_project(save_path, projectdir, editor, terminal, name):
    data = load_projects(save_path)
    project = retrive_project(data, name)
    if project is not None:
        print(f'Project "{name}" already exists, editing instead')
        project["path"] = projectdir
        project["editor"] = editor
        project["terminal"] = terminal
    else:
        data.append(
            {"name": name, "path": projectdir, "editor": editor, "terminal": terminal}
        )
    save_projects(save_path, data)


def list_projects(save_path):
    data = load_projects(save_path)
    table = [["Project", "Editor", "Terminal", "Path"]]
    for project in data:
        table.append(
            [project["name"], project["editor"], project["terminal"], project["path"]]
        )
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


def list_project_names(save_path):
    data = load_projects(save_path)
    for project in data:
        print(project["name"])


def launch_project_by_name(save_path, project_name):
    data = load_projects(save_path)
    project = retrive_project(data, project_name)
    if project is None:
        print(f'Could not locate project "{project_name}", it does not exist')
        exit(-1)
    launch_project(project["path"], project["editor"], project["terminal"])


def delete_project(save_path, project_name):
    data = load_projects(save_path)
    foundIndex = -1
    for index, project in data:
        if project["name"] == project_name:
            foundIndex = index
            break
    data.remove(data[foundIndex])
    save_projects(save_path, data)
