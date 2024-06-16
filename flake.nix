{
  description = "ProjectOR is a project launcher, taking care of handling envs for IDE's that cannot. Murder and Necromancy may be involved.";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        url = "nixpkgs/nixos-24.05";
      };

      build-deps = with pkgs; [
        python311
      ] ++ (with pkgs.python311Packages; [
	configargparse
      ]);

      dev-deps = with pkgs; [
	neovim
      ];
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = build-deps ++ dev-deps;
      };
    };
}
