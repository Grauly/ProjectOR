import configargparse
import subprocess

import projector_utils as utils

p = configargparse.ArgParser()
p.add('-p', '--project', help='launch the specified project by name')
p.add('-l', '--list', help='list all projects')
p.add('-a', '--add', help='add a project')
p.add('-lp', '--launch-project', help='launch project by dir')
p.add('-e', '--editor', help='set editor to launch with')
p.add('-t', '--terminal', help='set terminal to use')

options = p.parse_args()

if options.launch_project is not None:
    if options.editor is None:
        print(f'trying to launch a project without a editor specified')
        exit(-1)
    utils.launch_project(options.launch_project, options.editor, options.terminal)
