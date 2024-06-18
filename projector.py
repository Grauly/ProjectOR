#!/usr/bin/env python
import configargparse
import subprocess

import projector_utils as utils

DEFAULT_SAVE_PATH = "~/.local/share/ProjectOR/projects.json"

def main():
    p = configargparse.ArgParser()
    p.add("-l", action="store_true", help="list all projects")
    p.add("-ln", action="store_true", help="list all project names")
    p.add("-a", "--add", help="add a project by name")
    p.add("-lp", "--launch-project", help="launch project by dir")
    p.add("-e", "--editor", help="set editor to launch with")
    p.add("-t", "--terminal", help="set terminal to use")
    p.add("-f", "--path", help="set project path")
    p.add("-r", help="launch project by name")
    p.add("-d", help="delete project by name")

    options = p.parse_args()

    if options.r is not None:
    utils.launch_project_by_name(DEFAULT_SAVE_PATH, options.r)
    exit(0)

    if options.launch_project is not None:
    if options.editor is None:
        print(f"trying to launch a project without a editor specified")
        exit(-1)
    utils.launch_project(options.launch_project, options.editor, options.terminal)
    exit(0)

    if options.add is not None:
    if options.editor is None:
        print(f"could not add project, no editor specified")
        exit(-1)
    if options.path is None:
        print(f"could not add project, no path specified")
        exit(-1)
    utils.add_project(
        DEFAULT_SAVE_PATH, options.path, options.editor, options.terminal, options.add
    )
    exit(0)

    if options.l:
    utils.list_projects(DEFAULT_SAVE_PATH)
    exit(0)

    if options.ln:
    utils.list_project_names(DEFAULT_SAVE_PATH)
    exit(0)

    if options.d is not None:
    utils.delete_project(DEFAULT_SAVE_PATH, options.d)
    exit(0)
