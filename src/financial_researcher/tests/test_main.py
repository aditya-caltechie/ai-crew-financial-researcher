"""Unit tests for main module."""
import pytest
from unittest.mock import MagicMock, patch

from financial_researcher.main import run


class TestRun:
    """Tests for the run() function."""

    @patch("financial_researcher.main.ResearchCrew")
    @patch("financial_researcher.main.os.makedirs")
    def test_run_creates_crew_and_kicks_off(self, mock_makedirs, mock_research_crew_cls):
        """run() instantiates ResearchCrew and calls kickoff with expected inputs."""
        mock_crew_instance = MagicMock()
        mock_result = MagicMock()
        mock_result.raw = "Sample report content"
        mock_crew_instance.kickoff.return_value = mock_result

        mock_research_crew_instance = MagicMock()
        mock_research_crew_instance.crew.return_value = mock_crew_instance
        mock_research_crew_cls.return_value = mock_research_crew_instance

        run()

        mock_research_crew_cls.assert_called_once()
        mock_research_crew_instance.crew.assert_called_once()
        mock_crew_instance.kickoff.assert_called_once_with(inputs={"company": "Tesla"})
        mock_makedirs.assert_called_once_with("output", exist_ok=True)

    @patch("financial_researcher.main.ResearchCrew")
    @patch("financial_researcher.main.os.makedirs")
    @patch("financial_researcher.main.print")
    def test_run_prints_result(self, mock_print, mock_makedirs, mock_research_crew_cls):
        """run() prints the result raw content."""
        mock_result = MagicMock()
        mock_result.raw = "Test report output"

        mock_crew_instance = MagicMock()
        mock_crew_instance.kickoff.return_value = mock_result

        mock_research_crew_instance = MagicMock()
        mock_research_crew_instance.crew.return_value = mock_crew_instance
        mock_research_crew_cls.return_value = mock_research_crew_instance

        run()

        assert any(
            "Test report output" in str(call) for call in mock_print.call_args_list
        )
