{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShellNoCC {
  packages = with pkgs; [
    (pkgs.python314.withPackages (ps: [ ps.tkinter ]))
  ];
}
