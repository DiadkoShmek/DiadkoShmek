import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "profile-proof.yml"
PROOF = "https://github.com/DiadkoShmek/evidence-gated-agent-workflows"
HOUSE_BOOK = "https://github.com/DiadkoShmek/DiadkoShmek/blob/main/house/book/uk/README.md"


class ProfileDiscoveryContractTest(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")
        self.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_profile_is_a_plain_bilingual_library_index(self):
        for filename in ("README.md", "README.en.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            lines = [line for line in text.splitlines() if line.strip()]
            self.assertTrue(lines[0].startswith("# "))
            self.assertEqual(len(lines), 6)
            self.assertTrue(all(line.startswith("- [") for line in lines[1:-1]))
            for path in ("/library/movy-1-20/", "/library/ai-ontology/", "/house/book/", "/library/benchmark-lezo/"):
                self.assertEqual(text.count(path), 1)
            self.assertTrue(lines[-1].startswith("["))
            self.assertNotRegex(text, r"mailto:|linkedin[.]com/in/|<picture>|<details>")

    def test_profile_has_no_fixed_offer_or_private_paths(self):
        for sales_fragment in ("$1,500", "Proof Sprint", "fixed-scope", "3–5 working days"):
            self.assertNotIn(sales_fragment, self.readme)
        self.assertNotRegex(self.readme, r"/home/[^/]+")
        self.assertNotIn("file://", self.readme)

    def test_profile_links_are_public_https_targets(self):
        targets = re.findall(r"\[[^]]+\]\(([^)]+)\)", self.readme)
        self.assertTrue(targets)
        self.assertTrue(
            all(target.startswith("https://") or target.startswith("#") for target in targets),
            targets,
        )

    def test_library_local_links_open(self):
        for path in (ROOT / "library").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if link.startswith(("https://", "http://", "#")):
                    continue
                self.assertTrue((path.parent / link.split("#")[0]).is_file(), (path.name, link))
        self.assertEqual(len(list((ROOT / "library/movy-1-20/books").glob("*.md"))), 20)

    def test_profile_proof_workflow_is_exact_and_read_only(self):
        checkout = "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1"
        setup_python = "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97"
        proof = "run: python3 -m unittest -v test_profile_discovery.py"
        uses = re.findall(r"(?m)^\s+uses:\s+(\S+)", self.workflow)

        self.assertEqual(uses, [checkout, setup_python])
        self.assertEqual(self.workflow.count(checkout), 1)
        self.assertEqual(self.workflow.count(setup_python), 1)
        self.assertEqual(self.workflow.count(proof), 1)
        self.assertLess(self.workflow.index(checkout), self.workflow.index(setup_python))
        self.assertLess(self.workflow.index(setup_python), self.workflow.index(proof))
        self.assertRegex(self.workflow, r"(?m)^permissions:\n  contents: read$")
        self.assertIn('python-version: "3.12"', self.workflow)
        self.assertNotRegex(self.workflow, r"(?m)^\s+[a-z-]+: write$")
        self.assertNotIn("id-token: write", self.workflow)




if __name__ == "__main__":
    unittest.main()
