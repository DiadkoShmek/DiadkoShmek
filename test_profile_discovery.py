import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
RELEASE = "https://github.com/DiadkoShmek/evidence-gated-agent-workflows/releases/tag/public-proof-v1.7.0"
SPRINT = "https://diadkoshmek.github.io/evidence-gated-agent-workflows/ai-systems-sprint.html"
INQUIRY = "https://github.com/DiadkoShmek/evidence-gated-agent-workflows/issues/new?template=client-inquiry.yml"


class ProfileDiscoveryContractTest(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")

    def test_profile_routes_proof_to_one_exact_offer_and_review_intake(self):
        for route in (RELEASE, SPRINT, INQUIRY):
            self.assertIn(route, self.readme)
        self.assertIn("$1,500 fixed, 3–5 working days", self.readme)
        self.assertIn("Production deployment, SLA, certification", self.readme)
        self.assertIn("Публічний issue не повинен містити credentials", self.readme)

    def test_public_proof_claim_is_current_and_reproducible(self):
        self.assertNotIn("f60c8a8", self.readme)
        self.assertNotIn("17 deterministic tests", self.readme)
        self.assertIn("python3 run_proof.py", self.readme)
        self.assertIn("ALL PUBLIC PROOFS PASSED", self.readme)
        self.assertIn("Immutable release `public-proof-v1.7.0`", self.readme)
        self.assertIn("Public proof v1.7", self.readme)
        self.assertIn("historical held-FD readback без current-path claim", self.readme)
        self.assertNotIn("public-proof-v1.6.0", self.readme)
        self.assertGreaterEqual(self.readme.count(RELEASE), 2)

    def test_public_files_do_not_expose_local_paths_or_authority_claims(self):
        self.assertNotIn("/home/pustota", self.readme)
        self.assertNotIn("file://", self.readme)
        self.assertIn("network_access_performed=false", self.readme)
        self.assertIn("external_action_performed=false", self.readme)
        self.assertIn("review-only inquiry", self.readme)

    def test_public_profile_does_not_link_local_only_materials(self):
        targets = re.findall(r"\[[^]]+\]\(([^)]+)\)", self.readme)
        self.assertTrue(targets)
        self.assertTrue(
            all(target.startswith("https://") or target.startswith("#") for target in targets),
            targets,
        )
        self.assertIn("не є частиною публічного proof", self.readme)


if __name__ == "__main__":
    unittest.main()
