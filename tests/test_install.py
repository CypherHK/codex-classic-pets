"""Real copy/refusal behavior in isolated temporary directories."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/install.py"
IDS = ("lahm-classic-orange", "super-lahm-classic", "super-nono")


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="codex-pets-test-")
        self.base = Path(self.temp.name)
        self.target = self.base / "data with spaces" / "pets"

    def tearDown(self):
        self.temp.cleanup()

    def run_installer(self, *args, script=SCRIPT, target=None):
        return subprocess.run(
            [sys.executable, str(script), *args, "--target", str(target or self.target)],
            capture_output=True, text=True,
        )

    def test_all_installs_exact_runtime_bytes_only(self):
        result = self.run_installer("all")
        self.assertEqual(result.returncode, 0, result.stderr)
        for pet_id in IDS:
            self.assertEqual(sorted(p.name for p in (self.target / pet_id).iterdir()),
                             ["pet.json", "spritesheet.webp"])
            for filename in ("pet.json", "spritesheet.webp"):
                self.assertEqual((ROOT / "pets" / pet_id / filename).read_bytes(),
                                 (self.target / pet_id / filename).read_bytes())

    def test_selected_only_and_duplicate_id(self):
        result = self.run_installer(IDS[1], IDS[1])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([p.name for p in self.target.iterdir()], [IDS[1]])

    def test_conflict_blocks_whole_batch_without_overwriting(self):
        occupied = self.target / IDS[1]
        occupied.mkdir(parents=True)
        marker = occupied / "existing.txt"
        marker.write_text("keep")
        result = self.run_installer("all")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), "keep")
        self.assertFalse((self.target / IDS[0]).exists())
        self.assertFalse((self.target / IDS[2]).exists())

    def test_unknown_id_writes_nothing(self):
        result = self.run_installer("../other")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.target.exists())

    def test_checksum_mismatch_writes_nothing(self):
        clone = self.base / "bad-release"
        (clone / "scripts").mkdir(parents=True)
        shutil.copy2(SCRIPT, clone / "scripts/install.py")
        shutil.copy2(ROOT / "checksums.json", clone / "checksums.json")
        shutil.copytree(ROOT / "pets" / IDS[0], clone / "pets" / IDS[0])
        bad = clone / "pets" / IDS[0] / "spritesheet.webp"
        with bad.open("ab") as file:
            file.write(b"corrupt")
        result = self.run_installer(IDS[0], script=clone / "scripts/install.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Checksum mismatch", result.stderr)
        self.assertFalse(self.target.exists())

    def test_dangling_symlink_destination_is_not_replaced(self):
        self.target.mkdir(parents=True)
        link = self.target / IDS[0]
        link.symlink_to(self.base / "absent", target_is_directory=True)
        result = self.run_installer(IDS[0])
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(link.is_symlink())

    def test_codex_home_is_respected_without_explicit_target(self):
        env = dict(os.environ, CODEX_HOME=str(self.base / "custom data"))
        result = subprocess.run([sys.executable, str(SCRIPT), IDS[2]],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.base / "custom data/pets" / IDS[2] / "pet.json").is_file())


if __name__ == "__main__":
    unittest.main()
