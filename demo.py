"""
Demo Script for Cognitive Physics Framework

This script demonstrates the core predictions of the framework
on example networks. Run this to see the theory in action.

Usage:
    python demo.py

Author: Cognitive Physics Project
License: MIT
"""

from meta_law_synthesis import MetaLawSynthesis, print_prediction
from example_networks import (
    ALL_NETWORKS,
    BIOLOGICAL_NETWORKS,
    ARTIFICIAL_NETWORKS,
    SOCIAL_NETWORKS,
    get_cognitive_networks,
    get_non_cognitive_networks
)


def print_header():
    """Print demo header"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   🧠 COGNITIVE PHYSICS FRAMEWORK - DEMO                          ║
║                                                                  ║
║   Structural-Dynamical Equivalence Law:                          ║
║   Φ(N) = 1  iff  S × D × M ≥ C_critical(class)                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)


def run_single_prediction(synthesis: MetaLawSynthesis, network):
    """Run prediction on a single network"""
    state = synthesis.predict({
        "S": network.S,
        "D": network.D,
        "M": network.M
    })
    
    # Compact output
    status = "🟢" if state.phi == 1 else "🔴"
    expected = "✓" if (state.phi == 1) == network.expected_cognitive else "✗"
    
    print(f"  {status} {network.name:<30} S={network.S:.2f} D={network.D:.2f} M={network.M:.2f} "
          f"C={state.capacity:.4f} [{expected}]")
    
    return state


def run_category_demo(synthesis: MetaLawSynthesis, networks, category_name: str):
    """Run demo on a category of networks"""
    print(f"\n{'─'*70}")
    print(f"  {category_name.upper()}")
    print(f"{'─'*70}")
    
    correct = 0
    for network in networks:
        state = run_single_prediction(synthesis, network)
        if (state.phi == 1) == network.expected_cognitive:
            correct += 1
    
    accuracy = correct / len(networks) * 100
    print(f"\n  Accuracy: {correct}/{len(networks)} ({accuracy:.0f}%)")
    
    return correct, len(networks)


def run_full_demo():
    """Run the complete demo"""
    print_header()
    
    synthesis = MetaLawSynthesis()
    
    total_correct = 0
    total_networks = 0
    
    # Biological
    c, n = run_category_demo(synthesis, BIOLOGICAL_NETWORKS, "Biological Networks")
    total_correct += c
    total_networks += n
    
    # Artificial
    c, n = run_category_demo(synthesis, ARTIFICIAL_NETWORKS, "Artificial Networks")
    total_correct += c
    total_networks += n
    
    # Social
    c, n = run_category_demo(synthesis, SOCIAL_NETWORKS, "Social Networks")
    total_correct += c
    total_networks += n
    
    # Summary
    print(f"\n{'═'*70}")
    print(f"  SUMMARY")
    print(f"{'═'*70}")
    
    summary = synthesis.get_summary()
    
    print(f"""
  Total Networks Tested:  {summary['total']}
  Predicted Cognitive:    {summary['cognitive']}
  Predicted Non-Cognitive: {summary['non_cognitive']}
  
  Overall Accuracy:       {total_correct}/{total_networks} ({total_correct/total_networks*100:.0f}%)
    """)
    
    # Show universality classes
    print(f"{'─'*70}")
    print(f"  UNIVERSALITY CLASSES")
    print(f"{'─'*70}")
    
    class_counts = {}
    for pred in synthesis.predictions:
        cls = pred.universality_class
        class_counts[cls] = class_counts.get(cls, 0) + 1
    
    for cls, count in sorted(class_counts.items()):
        print(f"  {cls:<25} {count} networks")
    
    # Show the core equation
    print(f"""
{'═'*70}
  THE CORE EQUATION
{'═'*70}

  Φ(N) = 1  iff  S(N) × D(N) × M(N) ≥ C_critical(class)

  Where:
    S = Structural Differentiation (topology heterogeneity)
    D = Causal Density (interaction intensity)  
    M = Memory Persistence (pattern retention)

  Class Thresholds:
    Grammar-Structural:  C = 0.003  (brains, neural nets)
    Fast-Propagation:    C = 0.005  (social media, internet)
    Slow-Memory:         C = 0.007  (institutions, ecosystems)
    Dense-Dynamical:     C = 0.010  (transformers, LLMs)

{'═'*70}
    """)


def run_detailed_example():
    """Run a detailed example with full output"""
    print("\n" + "="*70)
    print("  DETAILED EXAMPLE: Human Brain vs Simple MLP")
    print("="*70)
    
    synthesis = MetaLawSynthesis()
    
    # Human brain
    print("\n📊 Human Brain:")
    state = synthesis.predict({"S": 0.85, "D": 0.70, "M": 0.60})
    print_prediction(state)
    
    # Simple MLP
    print("\n📊 Simple MLP:")
    state = synthesis.predict({"S": 0.20, "D": 0.30, "M": 0.01})
    print_prediction(state)


if __name__ == "__main__":
    run_full_demo()
    run_detailed_example()
