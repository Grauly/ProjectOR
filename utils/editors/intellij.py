#!/usr/bin/env python
import subprocess

def needs_kill():
    return True

def kill():
    subprocess.run(['ps', '-x', '|' ,'grep' ,'"idea"' ,'|' ,'grep' ,'-v' ,'"grep"' ,'|' ,'sed' ,'"s/' ,'*\([0-9]*\)' ,'.*/\1/"' ,'|' ,'xargs' ,'kill'])

def launch_command(project_dir):
    return [f"idea-community", f"{project_dir}"]
