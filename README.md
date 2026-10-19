# Clean Vexed packs

The 48 level packs of Vexed for Windows (2,878 levels), cleaned up so any parser can read them without special cases.

## Credits

The levels are from **Vexed** by James A. McCombe and the Vexed Development Team (Classic II Levels by Steve Haynal), as released in the PuzzlePacks of **Vexed for Windows** by John G. Zvonar. Each pack names its author in its `[General]` section.

## License

GNU General Public License, version 2: see [LICENSE](LICENSE). The cleaned packs are a modified version of the originals.

## What was cleaned

Compared with the packs in the Vexed for Windows `PuzzlePack1–4.zip`:
- Every file is UTF-8 with LF line endings.
- Lines damaged in the Windows release are repaired: broken `key=value` separators, misspelt keys, stray spaces, a board row missing its right wall, and two solutions (one illegal, one replaced by the Palm 2.2 pack's shorter one).
- Titles damaged in the Windows release are restored as they are in the Palm Vexed 2.2 packs.

Every pack parses with no warnings, and every level's solution clears its board.

## Format

Each pack is an INI file: a `[General]` section (`Author`, `URL`, `Description`), then one `[Level]` section per level with `board`, `solution` and `title`.

## Playing them

The packs can be imported into Vexed-style games that read this format, such as Baffled.
