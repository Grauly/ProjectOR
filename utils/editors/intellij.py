#!/usr/bin/env python
import subsystem

def needs_kill():
    return True

def kill():
    subsystem.run['ps', 'x', '|' ,'grep' ,'"idea"' ,'|' ,'grep' ,'-v' ,'"grep"' ,'|' ,'sed' ,'"s/' ,'*\([0-9]*\)' ,'.*/\1/"' ,'|' ,'xargs' ,'kill']

def launch_command(project_dir):
    return [f"idea-community", "."]
