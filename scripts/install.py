#!/usr/bin/env python3
"""Install selected, checksum-verified pets without overwriting existing folders."""
import argparse
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PET_IDS = ("lahm-classic-orange", "super-lahm-classic", "super-nono")


def install(selected, target):
    """Preflight every selection before creating any installation directory."""
    checksums = json.loads((ROOT / "checksums.json").read_text(encoding="utf-8"))
    if checksums.get("algorithm") != "sha256":
        raise ValueError("Unsupported checksum format.")
    expected = checksums["files"]
    for pet_id in selected:
        source = ROOT / "pets" / pet_id
        destination = target / pet_id
        if destination.exists() or destination.is_symlink():
            raise ValueError("Refusing to overwrite: " + str(destination))
        if source.is_symlink() or not source.is_dir():
            raise ValueError("Missing or symlinked source folder: " + pet_id)
        for filename in ("pet.json", "spritesheet.webp"):
            path = source / filename
            if path.is_symlink() or not path.is_file():
                raise ValueError("Missing or symlinked asset: " + str(path))
            key = path.relative_to(ROOT).as_posix()
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != expected.get(key):
                raise ValueError("Checksum mismatch: " + key)
        manifest = json.loads((source / "pet.json").read_text(encoding="utf-8"))
        if (manifest.get("id") != pet_id
                or manifest.get("spriteVersionNumber") != 2
                or manifest.get("spritesheetPath") != "spritesheet.webp"):
            raise ValueError("Invalid manifest: " + pet_id)
    target.mkdir(parents=True, exist_ok=True)
    for pet_id in selected:
        destination = target / pet_id
        destination.mkdir(exist_ok=False)
        for filename in ("pet.json", "spritesheet.webp"):
            shutil.copy2(ROOT / "pets" / pet_id / filename, destination / filename)
        print("Installed: " + str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pets", nargs="*", help="Pet IDs, or all (default).")
    parser.add_argument("--target", type=Path, help="Destination pets directory.")
    args = parser.parse_args()
    names = args.pets or ["all"]
    if names == ["all"]:
        selected = list(PET_IDS)
    elif "all" in names or any(name not in PET_IDS for name in names):
        parser.error("Choose all, or IDs from: " + ", ".join(PET_IDS))
    else:
        selected = list(dict.fromkeys(names))
    codex_data = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    target = (args.target or codex_data / "pets").expanduser()
    try:
        install(selected, target)
    except (OSError, ValueError, KeyError) as exc:
        print("Installation failed: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
