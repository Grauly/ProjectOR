import subprocess
import importlib

def launch_project(projectdir, editor, terminal):
    try:
        editor_handler = importlib.import_module(f'editors.{editor}', package=__name__)
    except ImportError as e:
        print(f'could not find module for editor: {editor} {e}')
        exit(-1)
    if terminal is not None:
        try:
            terminal_handler = importlib.import_module(f'terminals.{terminal}', package=__name__)
        except ImportError:
            print(f'could not find module for terminal: {terminal}')
            exit(-1)
    if editor_handler.needs_kill():
        editor_handler.kill()
    flake = open(f'{projectdir}flake.nix')
    launch_command = ['nix', 'develop', f'{projectdir}', '--command'] + editor_handler.launch_command(projectdir) + ['return']
    if terminal is not None:
        launch_command = terminal_handler.generate_launch(launch_command)
    print(launch_command)
    subprocess.run(launch_command)
