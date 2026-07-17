import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.agent = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")

    def test_trigger_description_covers_postmatch_review_and_evolution(self):
        frontmatter = self.skill.split("---", 2)[1]

        self.assertIn("post-match review", frontmatter)
        self.assertIn("self-evolution", frontmatter)
        self.assertIn("赛后复盘", frontmatter)

    def test_skill_requires_bilingual_review_for_correct_and_incorrect_forecasts(self):
        self.assertIn("## Post-Match Review And Evolution", self.skill)
        self.assertIn("correct and incorrect forecasts", self.skill)
        self.assertIn("same language as the user", self.skill)

    def test_skill_keeps_result_periods_separate(self):
        self.assertIn("score_90m", self.skill)
        self.assertIn("score_after_extra_time", self.skill)
        self.assertIn("penalties", self.skill)
        self.assertIn("Never settle a 90-minute market", self.skill)

    def test_skill_documents_distinct_match_floors_and_no_single_match_update(self):
        self.assertIn("100 distinct matches", self.skill)
        self.assertIn("30 distinct matches in every affected bucket", self.skill)
        self.assertIn("One completed match never changes the active profile", self.skill)

    def test_skill_documents_walk_forward_gates_and_rollback(self):
        for phrase in (
            "grouped chronological walk-forward",
            "1% relative Brier improvement",
            "no log-loss regression",
            "no totals or BTTS regression",
            "2% bucket regression cap",
            "0.005 calibration-error tolerance",
            "30 new distinct matches",
        ):
            self.assertIn(phrase, self.skill)

    def test_skill_documents_all_evolution_states(self):
        for state in (
            "model_unchanged",
            "challenger_pending",
            "champion_promoted",
            "champion_rolled_back",
        ):
            self.assertIn(state, self.skill)

    def test_skill_documents_every_self_evolution_command(self):
        for script in (
            "scripts/forecast.py",
            "scripts/postmatch_review.py",
            "scripts/calibrate.py",
            "scripts/evolve.py",
            "scripts/postmatch_alerts.py",
        ):
            self.assertIn(script, self.skill)
        self.assertIn("--mode rollback", self.skill)
        self.assertIn("references/postmatch-evolution.md", self.skill)

    def test_skill_retains_no_certainty_or_profit_guarantee(self):
        self.assertIn("no guarantees", self.skill)
        self.assertIn("no profit claims", self.skill)
        self.assertIn("Never guarantee a result", self.skill)

    def test_agent_metadata_mentions_forecast_review_and_user_language(self):
        self.assertIn("post-match", self.agent)
        self.assertIn("Match the user's language", self.agent)

    def test_skill_defines_sofascore_and_hkjc_live_source_roles(self):
        self.assertIn("## Live Match Data Workflow", self.skill)
        self.assertIn("Sofascore", self.skill)
        self.assertIn("HKJC", self.skill)
        self.assertIn("match-state source", self.skill)
        self.assertIn("Hong Kong in-play market source", self.skill)

    def test_skill_fails_closed_on_unsynchronized_or_suspended_live_data(self):
        for phrase in (
            "90 seconds",
            "scores disagree",
            "market is suspended",
            "event identity",
            "unsupported_live_state",
        ):
            self.assertIn(phrase, self.skill)

    def test_skill_never_relabels_pre_match_prices_as_live(self):
        self.assertIn("freeze pre-match prices at kickoff", self.skill)
        self.assertIn("Never relabel a pre-match quote as an in-play quote", self.skill)

    def test_source_policy_documents_live_source_validation(self):
        source_policy = (ROOT / "references" / "source-policy.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Live Match Sources",
            "Sofascore",
            "HKJC",
            "90 seconds",
            "one bookmaker",
            "suspended",
        ):
            self.assertIn(phrase, source_policy)


if __name__ == "__main__":
    unittest.main()
