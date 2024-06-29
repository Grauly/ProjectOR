# ProjectOR

## Discontinued untill further notice
Basically, IntelliJ did not understand what I wanted it to do and I found a way to solve my particular problem with IntelliJ. having multiple jdks for it.
The workaround that works for me, is to write the jdks to the `~/.jdks/` folder.

Solves my particular problem with having IDE's (IntelliJ) which cannot really handle nix based envs.
It does this by remembering what IDE's projects are supposed to have, and then launch those IDE's in the context of a nix environment, Taking care that IDE's that cannot handle switching envs get killed and restarted.

#Known issues
if there is no flake on the current branch of the project, then it does not know what to do
