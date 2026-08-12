# -*- coding: utf-8 -*-
"""
RailwayTwin Unit Test Suite
Tests Digital Twin state synchronization, safety verification, conflict detection, and network graph creation.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.digital_twin.safety_verifier import SafetyVerifier, VerificationResult
from src.digital_twin.twin_state import TwinState
from src.digital_twin.conflict_detector import ConflictDetector
from src.network.network_builder import NetworkBuilder


class TestRailwayTwin(unittest.TestCase):

    def test_twin_state_initialization(self):
        """Test digital twin state creation and train update."""
        twin = TwinState()
        twin.update_train("TRAIN_01", {"id": "TRAIN_01", "speed": 80, "location": "TRACK_A"})
        state = twin.get_train("TRAIN_01")
        self.assertIsNotNone(state)
        self.assertEqual(state["speed"], 80)

    def test_conflict_detector_clean(self):
        """Test conflict detector with non-overlapping train states."""
        detector = ConflictDetector()
        twin = TwinState()
        twin.update_track("TRACK_1", {"track_id": "TRACK_1", "allocated_to": "T1"})
        twin.update_track("TRACK_2", {"track_id": "TRACK_2", "allocated_to": "T2"})
        
        conflicts = detector.check_track_conflicts(twin)
        self.assertEqual(len(conflicts), 0)

    def test_conflict_detector_overlap(self):
        """Test conflict detector detecting multiple allocations on same track."""
        detector = ConflictDetector()
        twin = TwinState()
        twin.update_track("TRACK_1", {"track_id": "TRACK_1", "allocated_to": "T1"})
        # Update track 1 again to simulate duplicate allocation
        twin.tracks["TRACK_1_DUP"] = {"track_id": "TRACK_1", "allocated_to": "T2"}
        
        conflicts = detector.check_track_conflicts(twin)
        self.assertEqual(len(conflicts), 1)
        self.assertEqual(conflicts[0]['type'], 'TRACK_CONFLICT')

    def test_safety_verifier_sync(self):
        """Test safety verifier state synchronization."""
        verifier = SafetyVerifier()
        verifier.sync_state(
            trains=[{"id": "T100", "speed": 75}],
            tracks=[{"track_id": "TK1", "occupied": False}]
        )
        train_info = verifier.twin_state.get_train("T100")
        self.assertEqual(train_info["speed"], 75)

    def test_network_builder(self):
        """Test network graph builder creation."""
        builder = NetworkBuilder()
        graph = builder.build_topology()
        self.assertIsNotNone(graph)


if __name__ == "__main__":
    unittest.main()
