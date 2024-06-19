#!/usr/bin/env python
def generate_launch(launch_command):
    full_command = " ".join(launch_command)
    return ["kitty"] + launch_command
