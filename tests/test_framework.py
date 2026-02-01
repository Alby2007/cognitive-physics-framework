"""
Unit Tests for Cognitive Physics Framework

Simple tests to verify the framework predicts correctly on known cases.

Usage:
    python -m pytest tests/test_framework.py
    or
    python tests/test_framework.py

Author: Cognitive Physics Project
License: MIT
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from meta_law_synthesis import MetaLawSynthesis, UniversalityClass
from core_interface import (
    CognitiveNetwork,
    MemoryModule,
    CausalityEngine,
    create_minimal_cognitive_system,
    compute_structural_differentiation
)
from example_networks import ALL_NETWORKS, HUMAN_BRAIN, SIMPLE_MLP, GPT3


def test_human_brain_is_cognitive():
    """Human brain should be classified as cognitive"""
    synthesis = MetaLawSynthesis()
    state = synthesis.predict({"S": 0.85, "D": 0.70, "M": 0.60})
    
    assert state.phi == 1, "Human brain should be cognitive"
    assert state.capacity > state.threshold, "Capacity should exceed threshold"
    print("✅ test_human_brain_is_cognitive passed")


def test_simple_mlp_is_not_cognitive():
    """Simple MLP should NOT be classified as cognitive"""
    synthesis = MetaLawSynthesis()
    state = synthesis.predict({"S": 0.20, "D": 0.30, "M": 0.01})
    
    assert state.phi == 0, "Simple MLP should not be cognitive"
    assert state.capacity < state.threshold, "Capacity should be below threshold"
    print("✅ test_simple_mlp_is_not_cognitive passed")


def test_capacity_formula():
    """Test that capacity = S × D × M"""
    synthesis = MetaLawSynthesis()
    
    S, D, M = 0.5, 0.4, 0.1
    state = synthesis.predict({"S": S, "D": D, "M": M})
    
    expected = S * D * M
    assert abs(state.capacity - expected) < 0.0001, f"Capacity should be {expected}, got {state.capacity}"
    print("✅ test_capacity_formula passed")


def test_universality_classes():
    """Test that different systems get classified into correct classes"""
    synthesis = MetaLawSynthesis()
    
    # Grammar-structural (high S, moderate D, low M)
    state1 = synthesis.predict({"S": 0.8, "D": 0.4, "M": 0.03})
    assert state1.universality_class == "grammar_structural", f"Expected grammar_structural, got {state1.universality_class}"
    
    # Dense-dynamical (low S, high D, low M)
    state2 = synthesis.predict({"S": 0.2, "D": 0.8, "M": 0.03})
    assert state2.universality_class == "dense_dynamical", f"Expected dense_dynamical, got {state2.universality_class}"
    
    print("✅ test_universality_classes passed")


def test_active_laws():
    """Test that laws activate under correct conditions"""
    synthesis = MetaLawSynthesis()
    
    # High S should activate structural differentiation law
    state = synthesis.predict({"S": 0.6, "D": 0.5, "M": 0.1})
    assert "Structural Differentiation" in state.active_laws, "Structural Differentiation should be active"
    
    # High D should activate causal time law
    assert "Causal Time" in state.active_laws, "Causal Time should be active"
    
    print("✅ test_active_laws passed")


def test_threshold_boundary():
    """Test behavior at the threshold boundary"""
    synthesis = MetaLawSynthesis()
    
    # Just above threshold (grammar_structural threshold = 0.003)
    state_above = synthesis.predict({"S": 0.5, "D": 0.3, "M": 0.025})  # 0.00375
    assert state_above.phi == 1, "Should be cognitive just above threshold"
    
    # Just below threshold
    state_below = synthesis.predict({"S": 0.5, "D": 0.1, "M": 0.01})  # 0.0005
    assert state_below.phi == 0, "Should not be cognitive just below threshold"
    
    print("✅ test_threshold_boundary passed")


def test_example_networks_accuracy():
    """Test prediction accuracy on example networks"""
    synthesis = MetaLawSynthesis()
    
    correct = 0
    total = len(ALL_NETWORKS)
    
    for network in ALL_NETWORKS:
        state = synthesis.predict({"S": network.S, "D": network.D, "M": network.M})
        if (state.phi == 1) == network.expected_cognitive:
            correct += 1
    
    accuracy = correct / total
    assert accuracy >= 0.8, f"Accuracy should be at least 80%, got {accuracy*100:.0f}%"
    print(f"✅ test_example_networks_accuracy passed ({correct}/{total} = {accuracy*100:.0f}%)")


def test_network_creation():
    """Test that we can create cognitive networks"""
    network, memory, causality, detector = create_minimal_cognitive_system(
        num_nodes=20,
        connectivity=0.1,
        memory_persistence=0.05
    )
    
    assert len(network.nodes) == 20, "Should have 20 nodes"
    assert memory.persistence == 0.05, "Memory persistence should be 0.05"
    print("✅ test_network_creation passed")


def test_structural_differentiation():
    """Test structural differentiation computation"""
    network = CognitiveNetwork()
    
    # Create a hub network (one node connected to all others)
    for i in range(10):
        network.add_node(f"node_{i}")
    
    # Node 0 is a hub
    for i in range(1, 10):
        network.add_edge("node_0", f"node_{i}")
    
    S = compute_structural_differentiation(network)
    assert S > 0.3, f"Hub network should have high S, got {S}"
    print("✅ test_structural_differentiation passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("  COGNITIVE PHYSICS FRAMEWORK - UNIT TESTS")
    print("="*60 + "\n")
    
    tests = [
        test_human_brain_is_cognitive,
        test_simple_mlp_is_not_cognitive,
        test_capacity_formula,
        test_universality_classes,
        test_active_laws,
        test_threshold_boundary,
        test_example_networks_accuracy,
        test_network_creation,
        test_structural_differentiation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"  RESULTS: {passed} passed, {failed} failed")
    print("="*60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
