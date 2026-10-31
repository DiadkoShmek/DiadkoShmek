import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "profile-proof.yml"
PROOF = "https://github.com/DiadkoShmek/evidence-gated-agent-workflows"
SIGNAL_DESK = "https://diadkoshmek.github.io/talent-research-workflow-prototype/?lang=uk&showcase=1"


class ProfileDiscoveryContractTest(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")
        self.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_profile_leads_to_real_work_without_personal_contact(self):
        for route in (PROOF, SIGNAL_DESK):
            self.assertIn(route, self.readme)
        self.assertNotIn("linkedin.com/in/", self.readme)
        self.assertNotIn("mailto:", self.readme)
        self.assertIn("python3 run_proof.py", self.readme)
        self.assertIn("прототипи", self.readme)
        self.assertIn("не історії про впровадження в клієнтів", self.readme)
        self.assertIn("https://diadkoshmek.github.io/mae7-viewer/", self.readme)
        self.assertIn("https://github.com/DiadkoShmek/mae7-viewer", self.readme)

    def test_profile_has_no_fixed_offer_or_private_paths(self):
        for sales_fragment in ("$1,500", "Proof Sprint", "fixed-scope", "3–5 working days"):
            self.assertNotIn(sales_fragment, self.readme)
        self.assertNotRegex(self.readme, r"/home/[^/]+")
        self.assertNotIn("file://", self.readme)

    def test_open_source_work_links_upstream_and_states_current_disposition(self):
        self.assertIn("https://github.com/PrimeIntellect-ai/verifiers/pull/2925", self.readme)
        self.assertIn("https://github.com/AndreyBegma/FilesDrop/pull/32", self.readme)
        self.assertIn("FilesDrop #32", self.readme)
        self.assertIn("· merged", self.readme)
        self.assertIn("https://github.com/PrimeIntellect-ai/verifiers/pull/2973", self.readme)
        self.assertIn("superseded, не злитий", self.readme)
        self.assertNotIn("21.10.2026 обидва PR відкриті, ще не злиті", self.readme)

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



class ResultsJournalContractTest(unittest.TestCase):
    def setUp(self):
        import json
        self.records = json.loads((ROOT / "results.json").read_text(encoding="utf-8"))["records"]
        self.journal = (ROOT / "RESULTS.md").read_text(encoding="utf-8")
        self.readme = README.read_text(encoding="utf-8")

    def test_profile_exposes_the_results_journal_without_manual_coding_claim(self):
        self.assertIn("https://github.com/DiadkoShmek/DiadkoShmek/blob/main/RESULTS.md", self.readme)
        self.assertIn("AI-інструментами", self.readme)
        self.assertNotIn("Пишу код для", self.readme)

    def test_each_result_is_bounded_dated_and_publicly_sourced(self):
        from datetime import date, datetime
        self.assertEqual(len({row["id"] for row in self.records}), len(self.records))
        self.assertGreaterEqual(len(self.records), 2)
        for row in self.records:
            with self.subTest(record=row["id"]):
                date.fromisoformat(row["as_of"])
                if "rank" in row:
                    self.assertGreaterEqual(row["rank"], 1)
                    self.assertLessEqual(row["rank"], row["participants"])
                elif row.get("category", "competition") == "competition":
                    self.assertEqual(row["result"], "prize_winner")
                    self.assertNotIn("participants", row)
                statuses = {
                    "competition": ("snapshot", "preliminary", "final"),
                    "upstream_contribution": ("merged", "incorporated_in_maintainer_fix"),
                    "external_audit": ("credited_in_release",),
                }
                self.assertIn(row["status"], statuses[row.get("category", "competition")])
                self.assertTrue(row["boundary"])
                self.assertTrue(row["source_url"].startswith("https://"))
                self.assertIn(row["source_url"], self.journal)
                for key in ("observed_at", "checked_at", "expected_final_at"):
                    if key in row:
                        self.assertIsNotNone(datetime.fromisoformat(row[key].replace("Z", "+00:00")).tzinfo)

    def test_arena_snapshot_has_the_declared_evidence_bytes(self):
        import hashlib
        row = next(row for row in self.records if row["format"] == "continuous_arena")
        self.assertEqual(row["status"], "snapshot")
        evidence = row["evidence"]
        path = (ROOT / evidence["path"]).resolve()
        self.assertTrue(path.is_relative_to(ROOT.resolve()))
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), evidence["sha256"])
        self.assertIn(evidence["path"], self.journal)
        self.assertIn(f'{row["rank"]}/{row["participants"]}', self.journal)
        self.assertIn(row["rank_scope"], self.journal)

    def test_preliminary_rank_and_final_announcement_remain_distinct(self):
        row = next(row for row in self.records if row["competition"] == "Zoria 2026")
        self.assertEqual(row["status"], "preliminary")
        self.assertNotIn("prize_amount", row)
        self.assertNotIn("payment_received", row)
        final = next(row for row in self.records if row.get("result") == "prize_winner")
        self.assertEqual(final["status"], "final")
        self.assertEqual(final["account"], row["account"])
        self.assertNotIn("rank", final)
        self.assertNotIn("prize_amount", final)
        self.assertNotIn("payment_received", final)
        self.assertNotIn("ще очікується", self.readme)
        self.assertNotIn("5/9", self.readme)
        self.assertIn("не є їх публікацією", self.journal)


class EngineeringReportContractTest(unittest.TestCase):
    def setUp(self):
        import json
        self.index = (ROOT / "ENGINEERING.md").read_text(encoding="utf-8")
        self.report = (ROOT / "reports/codingame-2026-10.md").read_text(encoding="utf-8")
        self.extract = json.loads((ROOT / "evidence/codingame-local-evaluation-2026-10.json").read_text(encoding="utf-8"))

    def test_process_is_primary_and_autonomy_is_not_invented(self):
        self.assertIn("https://github.com/DiadkoShmek/DiadkoShmek/blob/main/ENGINEERING.md", README.read_text(encoding="utf-8"))
        for boundary in ("Ігровий бот", "AI-агент розробки", "Людина визначає напрям", "не виміряні"):
            self.assertIn(boundary, self.index)
        self.assertIn("не контрольований порівняльний бенчмарк", self.index)
        self.assertTrue(self.extract["unmeasured"])

    def test_report_retains_negative_and_conditional_outcomes(self):
        rejected, conditional = self.extract["experiments"]
        self.assertEqual((rejected["wins"], rejected["completed_games"]), (2, 8))
        self.assertLess(rejected["wins"] + rejected["planned_games"] - rejected["completed_games"], rejected["required_wins"])
        self.assertFalse(rejected["reserve_opened"])
        self.assertEqual(conditional["wins"] / conditional["completed_games"], conditional["win_rate"])
        self.assertEqual(conditional["unique_seeds"] * 2, conditional["completed_games"])
        self.assertTrue(conditional["criteria_changed_after_prior_failures"])
        for row in self.extract["experiments"]:
            self.assertFalse(row["official_submission"])
            self.assertIn(f'{row["wins"]}/{row["completed_games"]}', self.report)
            for field in ("candidate_source_sha256", "baseline_source_sha256", "source_receipt_sha256"):
                self.assertRegex(row[field], r"^[a-f0-9]{64}$")
        self.assertIn("Не приписую це місце V89b", self.report)
        self.assertIn("відтворити матчі", self.report)

    def test_public_entry_is_short_and_method_remains_available(self):
        self.assertLess(len(README.read_text(encoding="utf-8").split()), 260)
        self.assertLess(len(self.index.split()), 260)
        self.assertIn("<details>", self.report)
        self.assertIn("Методика, дані та обмеження", self.report)
        self.assertIn("після цієї невдачі", self.report)
        self.assertIn("English summary", self.report)
        folder_index = (ROOT / "reports/README.md").read_text(encoding="utf-8")
        self.assertIn("codingame-2026-10.md", folder_index)

    def test_public_markdown_relative_links_resolve_inside_repository(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            for target in re.findall(r"!?\[[^]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("https://", "#")):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), (path.name, target))
                self.assertTrue(resolved.is_file(), (path.name, target))


class ExternalContributionContractTest(unittest.TestCase):
    def setUp(self):
        import json
        self.data = json.loads((ROOT / "results.json").read_text(encoding="utf-8"))
        self.records = {row["id"]: row for row in self.data["records"]}

    def test_prime_keeps_our_proposal_separate_from_merged_implementation(self):
        row = self.records["prime-intellect-verifiers-2026-10-24"]
        self.assertEqual(row["category"], "upstream_contribution")
        self.assertEqual(row["status"], "incorporated_in_maintainer_fix")
        self.assertFalse(row["contribution_merged"])
        self.assertEqual(row["implementation_by"], "maintainers")
        self.assertEqual(row["original_issue_author"], "rasdani")
        self.assertEqual(len(row["upstream_fixes"]), 2)
        for fix in row["upstream_fixes"]:
            self.assertTrue(fix["merged"])
            self.assertRegex(fix["merge_commit_sha"], r"^[a-f0-9]{40}$")

    def test_m7_audit_credit_is_not_an_implementation_or_current_health_claim(self):
        row = self.records["m7-audit-release-2026-10-29"]
        self.assertEqual(row["category"], "external_audit")
        self.assertEqual(row["status"], "credited_in_release")
        self.assertEqual(row["implementation_by"], "maintainers")
        self.assertEqual(row["release"], "v3.18.1")
        self.assertRegex(row["release_commit"], r"^[a-f0-9]{40}$")
        self.assertNotIn("contribution_merged", row)
        self.assertFalse(row["follow_up"]["full_reaudit"])
        self.assertFalse(row["follow_up"]["all_issues_closed"])
        self.assertEqual(row["follow_up"]["focused_tests_passed"], 168)
        import hashlib
        evidence = row["evidence"]
        self.assertEqual(hashlib.sha256((ROOT / evidence["path"]).read_bytes()).hexdigest(), evidence["sha256"])

    def test_filesdrop_is_the_merged_code_contribution(self):
        row = self.records["filesdrop-api-fixes-2026-10-21"]
        self.assertTrue(row["contribution_merged"])
        self.assertEqual(row["status"], "merged")
        self.assertEqual(row["implementation_by"], "DiadkoShmek with Codex assistance")
        self.assertRegex(row["merge_commit_sha"], r"^[a-f0-9]{40}$")

    def test_results_have_bilingual_entry_and_source_bound_case_reports(self):
        self.assertEqual(self.data["schema_version"], 2)
        english = (ROOT / "RESULTS.en.md").read_text(encoding="utf-8")
        for row in self.data["records"]:
            self.assertIn(row["source_url"], english)
            if row.get("category") != "competition":
                report = (ROOT / row["report_path"]).read_text(encoding="utf-8")
                self.assertIn(row["source_url"], report)
                self.assertIn("## English summary", report)
                self.assertNotRegex(report, r"/home/|/tmp/|mailto:|linkedin\.com/in/")
        self.assertIn("RESULTS.en.md", (ROOT / "README.en.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

