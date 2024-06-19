{
  description = "ProjectOR is a project launcher, taking care of handling envs for IDE's that cannot. Murder and Necromancy may be involved.";

  inputs = {
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, treefmt-nix }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        url = "nixpkgs/nixos-24.05";
      };

      treefmtEval = treefmt-nix.lib.evalModule pkgs ./treefmt.nix;

      build-deps = with pkgs; [
        python311
	tree
      ] ++ (with pkgs.python311Packages; [
        configargparse
        tabulate
	setuptools-git
	setuptools
      ]);

      dev-deps = with pkgs; [
        #	neovim
      ];

      projector = pkgs.python311Packages.buildPythonApplication {
        name = "projector";
        src = ./.;
        doCheck = false;
        propagatedBuildInputs = build-deps;
#	buildPhase = ''
#		ls -lsa .
#		echo $out
#	'';
      };
    in
    {
      formatter.${system} = treefmtEval.config.build.wrapper;
      checks.${system}.formatter = treefmtEval.config.build.check self;

      devShells.${system}.default = pkgs.mkShell {
        packages = build-deps ++ dev-deps;
      };

      packages.${system} = {
        default = pkgs.writeShellScriptBin "projector" ''
          	 ${projector}/bin/projector.py "''${@:1}"
          	 '';
      };
    };
}
