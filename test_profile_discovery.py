import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "profile-proof.yml"
PROOF = "https://github.com/DiadkoShmek/evidence-gated-agent-workflows"
SIGNAL_DESK = "https://diadkoshmek.github.io/talent-research-workflow-prototype/?lang=uk&showcase=1"
CONTACT = "https://www.linkedin.com/in/%D0%B0%D1%80%D1%82%D1%83%D1%80-%D0%BE%D0%BD%D0%B8%D1%81%D1%8C%D0%BA%D0%BE-842296411/"


class ProfileDiscoveryContractTest(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")
        self.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_profile_leads_to_real_work_and_human_contact(self):
        for route in (PROOF, SIGNAL_DESK, CONTACT):
            self.assertIn(route, self.readme)
        self.assertIn("python3 run_proof.py", self.readme)
        self.assertIn("прототипи", self.readme)
        self.assertIn("не історії про впровадження в клієнтів", self.readme)

    def test_profile_has_no_fixed_offer_or_private_paths(self):
        for sales_fragment in ("$1,500", "Proof Sprint", "fixed-scope", "3–5 working days"):
            self.assertNotIn(sales_fragment, self.readme)
        self.assertNotIn("/home/pustota", self.readme)
        self.assertNotIn("file://", self.readme)

    def test_profile_links_are_public_https_targets(self):
        targets = re.findall(r"\[[^]]+\]\(([^)]+)\)", self.readme)
        self.assertTrue(targets)
        self.assertTrue(
            all(target.startswith("https://") or target.startswith("#") for target in targets),
            targets,
        )

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
