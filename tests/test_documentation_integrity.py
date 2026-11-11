"""Repository documentation integrity checks for local Markdown links and text."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"!?[[^]]*](([^)]+))")


class DocumentationIntegrityTests(unittest.TestCase):
    def markdown_files(self):
        return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)

    def test_markdown_contains_no_unexpected_control_characters(self):
        unexpected = []
        for path in self.markdown_files():
            text = path.read_text(encoding="utf-8")
            for line_number, line in enumerate(text.splitlines(), start=1):
                for character in line:
                    code = ord(character)
                    if code < 32 and character not in "\t":
                        unexpected.append(f"{path.relative_to(ROOT)}:{line_number} U+{code:04X}")
        self.assertEqual(unexpected, [], "Unexpected control characters: " + ", ".join(unexpected))

    def test_relative_markdown_links_resolve_inside_repository(self):
        missing = []
        for source in self.markdown_files():
            text = source.read_text(encoding="utf-8")
            for match in LINK_PATTERN.finditer(text):
                raw = match.group(1).strip()
                if raw.startswith("<"):
                    angle_match = re.match(r"<([^>]+)>", raw)
                    destination = angle_match.group(1) if angle_match else raw
                else:
                    destination = raw.split()[0]

                if not destination or destination.startswith("#"):
                    continue

                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc:
                    continue

                relative_path = unquote(parsed.path)
                if not relative_path:
                    continue

                target = (ROOT / relative_path.lstrip("/")) if relative_path.startswith("/") else (source.parent / relative_path)
                target = target.resolve()
                if ROOT not in target.parents and target != ROOT:
                    missing.append(f"{source.relative_to(ROOT)} -> path escapes repository: {destination}")
                elif not target.exists():
                    missing.append(f"{source.relative_to(ROOT)} -> missing: {destination}")

        self.assertEqual(missing, [], "Broken local Markdown links: " + "; ".join(missing))


if __name__ == "__main__":
    unittest.main()
