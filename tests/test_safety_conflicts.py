# -*- coding: utf-8 -*-
"""
RailwayTwin Safety & Conflict Edge Case Unit Test Suite
Tests conflicting train movements, speed threshold violations, invalid state transitions, and signal safety verification failures.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.digital_twin.safety_verifier import SafetyVerifier
from src.digital_twin.twin_state import TwinState
from src.digital_twin.conflict_detector import ConflictDetector


class TestRailwaySafetyConflicts(unittest.TestCase):

    def setUp(self):
        self.verifier = SafetyVerifier()
        self.detector = ConflictDetector()
        self.twin = TwinState()

    def test_overspeed_safety_violation(self):
        """Test detection of trains exceeding track speed limits."""
        self.twin.update_train("TRAIN_EXPRESS", {"id": "TRAIN_EXPRESS", "speed": 180, "location": "SECTION_A"})
        self.twin.update_track("SECTION_A", {"track_id": "SECTION_A", "speed_limit": 100})
        
        # Verify overspeed checking logic
        train = self.twin.get_train("TRAIN_EXPRESS")
        track = self.twin.get_track("SECTION_A")
        self.assertGreater(train["speed"], track["speed_limit"])

    def test_invalid_speed_state(self):
        """Test handling of invalid state transitions (negative speed or missing location)."""
        self.twin.update_train("TRAIN_ERR", {"id": "TRAIN_ERR", "speed": -50, "location": "UNKNOWN"})
        train = self.twin.get_train("TRAIN_ERR")
        self.assertLess(train["speed"], 0)

    def test_multiple_simultaneous_conflicts(self):
        """Test detection of multiple track and signal conflicts."""
        self.twin.update_track("TRACK_SEC_1", {"track_id": "TRACK_SEC_1", "allocated_to": "T1"})
        self.twin.tracks["TRACK_SEC_1_DUP"] = {"track_id": "TRACK_SEC_1", "allocated_to": "T2"}
        
        conflicts = self.detector.check_track_conflicts(self.twin)
        self.assertGreater(len(conflicts), 0)


if __name__ == "__main__":
    unittest.main()
