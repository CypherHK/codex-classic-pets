# Codex Classic Pets

[中文（默认）](README.md) · English

Bring Lahm from *Mole Manor* and Super NONO from *Seer* to your Codex desktop.

This pack includes three animated pets with blinking, greetings, jumps, and expressions for working, waiting for input, and reviewing results. You can install the finished assets without any image-generation tools.

## Meet the pets

### Classic Lahm

A round orange body with two soft green leaves.

![Classic Lahm animation](previews/lahm-classic-orange/all-states.gif)

<details>
<summary>See jumping and turning</summary>

Jump transition:

![Classic Lahm jumping](previews/lahm-classic-orange/idle-jump-idle.gif)

Sixteen look directions:

![Classic Lahm turning](previews/lahm-classic-orange/look-loop.gif)

</details>

### Classic Super Lahm · softened

A yellow body with three gently curved golden leaves.

![Classic Super Lahm · softened animation](previews/super-lahm-classic/all-states.gif)

<details>
<summary>See jumping and turning</summary>

Jump transition:

![Classic Super Lahm · softened jumping](previews/super-lahm-classic/idle-jump-idle.gif)

Sixteen look directions:

![Classic Super Lahm · softened turning](previews/super-lahm-classic/look-loop.gif)

</details>

### Super NONO

A blue-and-white floating robot with cyan electronic expressions.

![Super NONO animation](previews/super-nono/all-states.gif)

<details>
<summary>See jumping and turning</summary>

Jump transition:

![Super NONO jumping](previews/super-nono/idle-jump-idle.gif)

Sixteen look directions:

![Super NONO turning](previews/super-nono/look-loop.gif)

</details>

These GIFs show the full state sequence. Individual states, jump transitions, direction loops, and MP4 copies are available in [previews](previews/README.md).

## Install

Download and extract the repository ZIP, or clone the repository. From its root, run:

```sh
python3 scripts/install.py all
```

To install only one pet:

```sh
python3 scripts/install.py lahm-classic-orange
```

The installer uses only the Python standard library, verifies file hashes, and **refuses to overwrite existing pets**. It does not change Codex settings, select an active pet, or download anything.

For manual installation, copy the selected complete folder from `pets/` into `~/.codex/pets/`. See [installation details](docs/installation.md) for custom data directories, Windows, and name conflicts.

After installation, choose the pet in Codex's pet picker. Restarting the app may help refresh newly added files. The entry point and animation triggers depend on the client version. The maintainer has tested the pets in their own Codex client and reports that they work correctly. See [validation notes](docs/validation.md) for the scope of resource and installer checks.

## Included files

- `pets/`: runtime `pet.json` files and transparent `spritesheet.webp` files.
- `previews/`: GIFs, MP4s, contact sheets, and stills encoded from these exact release sheets.
- `source-art/`: high-resolution base portraits for the two Lahm pets; not required to install.
- `qa/`: validation records with personal paths removed. Runtime hashes are in `checksums.json`.

## Characters and licensing

This is an unofficial character-redraw and animation pack, not an official release from the games or OpenAI. The characters originate in *Mole Manor* and *Seer*. AI-assisted redrawing does not establish ownership of the underlying characters.

The original installer and tests use the [MIT License](LICENSE). The underlying characters, names, and related assets belong to their respective rights holders and are not covered by that code license. This project does not claim official authorization or grant commercial-use or redistribution rights for those assets. See [credits](CREDITS.md) and [asset rights](ASSET_RIGHTS.md).

[GitHub repository](https://github.com/CypherHK/codex-classic-pets) · [Publication record](docs/release-checklist.md)
