"""
Meta-Law Synthesis Framework for Cognitive Physics

This is the main prediction framework that implements:
- The Structural-Dynamical Equivalence Law
- Four Universality Classes
- Cognitive capacity computation (S × D × M)

Core Equation:
    Φ(N) = 1  iff  S(N) × D(N) × M(N) ≥ C_critical(class)

Author: Cognitive Physics Project
License: MIT
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math

from core_interface import (
    CognitiveNetwork,
    MemoryModule,
    CausalityEngine,
    EmergenceDetector,
    compute_structural_differentiation
)


class UniversalityClass(Enum):
    """The four universality classes of cognitive dynamics"""
    GRAMMAR_STRUCTURAL = "grammar_structural"
    FAST_PROPAGATION = "fast_propagation"
    SLOW_MEMORY = "slow_memory"
    DENSE_DYNAMICAL = "dense_dynamical"


@dataclass
class CognitiveState:
    """Complete state of a cognitive system"""
    S: float  # Structural differentiation
    D: float  # Causal density
    M: float  # Memory persistence
    capacity: float = 0.0
    phi: int = 0  # 1 = cognitive, 0 = not
    universality_class: str = ""
    threshold: float = 0.0
    active_laws: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "S": self.S,
            "D": self.D,
            "M": self.M,
            "capacity": self.capacity,
            "phi": self.phi,
            "universality_class": self.universality_class,
            "threshold": self.threshold,
            "active_laws": self.active_laws
        }


class MetaLawSynthesis:
    """
    Main framework for cognitive physics predictions.
    
    Implements the Structural-Dynamical Equivalence Law:
        Φ(N) = 1  iff  S × D × M ≥ C_critical(class)
    
    Where:
        S = Structural differentiation (topology heterogeneity)
        D = Causal density (interaction intensity)
        M = Memory persistence (pattern retention)
        C_critical = Class-dependent threshold
    """
    
    # Universality class thresholds (empirically derived)
    CLASS_THRESHOLDS = {
        UniversalityClass.GRAMMAR_STRUCTURAL: 0.003,
        UniversalityClass.FAST_PROPAGATION: 0.005,
        UniversalityClass.SLOW_MEMORY: 0.007,
        UniversalityClass.DENSE_DYNAMICAL: 0.010
    }
    
    # Fundamental cognitive laws
    LAWS = {
        "structural_morality": {
            "name": "Structural Morality",
            "description": "Morality emerges from network topology, not external rules",
            "condition": lambda s, d, m: s > 0.3 and d > 0.2
        },
        "observation_independence": {
            "name": "Observation Independence",
            "description": "Emergence is observer-independent",
            "condition": lambda s, d, m: s * d * m > 0.001
        },
        "causal_time": {
            "name": "Causal Time",
            "description": "Time is causal density, not clock ticks",
            "condition": lambda s, d, m: d > 0.15
        },
        "memory_persistence": {
            "name": "Memory Persistence Law",
            "description": "Memory enables pattern formation and cognition",
            "condition": lambda s, d, m: m > 0.02
        },
        "structural_differentiation": {
            "name": "Structural Differentiation",
            "description": "Hubs, bridges, and clusters enable efficient cognition",
            "condition": lambda s, d, m: s > 0.4
        }
    }
    
    def __init__(self):
        self.predictions: List[CognitiveState] = []
    
    def classify_universality_class(self, S: float, D: float, M: float) -> UniversalityClass:
        """
        Determine which universality class a system belongs to.
        
        Classes:
        - Grammar-Structural: High S, moderate D (biological brains)
        - Fast-Propagation: High propagation, low M (social networks)
        - Slow-Memory: High M, slow dynamics (institutions)
        - Dense-Dynamical: Low S, high D (transformers)
        """
        if S > 0.5 and D < 0.5:
            return UniversalityClass.GRAMMAR_STRUCTURAL
        elif S > 0.6 and M < 0.05:
            return UniversalityClass.FAST_PROPAGATION
        elif M > 0.08:
            return UniversalityClass.SLOW_MEMORY
        elif S < 0.3 and D > 0.5:
            return UniversalityClass.DENSE_DYNAMICAL
        else:
            return UniversalityClass.GRAMMAR_STRUCTURAL  # Default
    
    def compute_capacity(self, S: float, D: float, M: float) -> float:
        """Compute cognitive capacity: S × D × M"""
        return S * D * M
    
    def get_active_laws(self, S: float, D: float, M: float) -> List[str]:
        """Determine which cognitive laws are active"""
        active = []
        for law_id, law in self.LAWS.items():
            if law["condition"](S, D, M):
                active.append(law["name"])
        return active
    
    def predict(self, params: Dict[str, Any]) -> CognitiveState:
        """
        Predict cognitive emergence for given parameters.
        
        Args:
            params: Dict with keys:
                - S or structural_differentiation: float (0-1)
                - D or causal_density: float (0-1)
                - M or memory_persistence: float (0-1)
                - network (optional): CognitiveNetwork to compute S from
        
        Returns:
            CognitiveState with prediction results
        """
        # Extract parameters
        S = params.get("S", params.get("structural_differentiation", 0.5))
        D = params.get("D", params.get("causal_density", 0.3))
        M = params.get("M", params.get("memory_persistence", 0.05))
        
        # If network provided, compute S from it
        if "network" in params:
            S = compute_structural_differentiation(params["network"])
        
        # Classify and get threshold
        uni_class = self.classify_universality_class(S, D, M)
        threshold = self.CLASS_THRESHOLDS[uni_class]
        
        # Compute capacity
        capacity = self.compute_capacity(S, D, M)
        
        # Determine emergence (Φ)
        phi = 1 if capacity >= threshold else 0
        
        # Get active laws
        active_laws = self.get_active_laws(S, D, M)
        
        # Create state
        state = CognitiveState(
            S=S,
            D=D,
            M=M,
            capacity=capacity,
            phi=phi,
            universality_class=uni_class.value,
            threshold=threshold,
            active_laws=active_laws
        )
        
        self.predictions.append(state)
        return state
    
    def predict_from_network(self, 
                              network: CognitiveNetwork,
                              memory: MemoryModule,
                              causality: CausalityEngine) -> CognitiveState:
        """
        Predict cognitive emergence from actual network components.
        
        Args:
            network: The cognitive network
            memory: Memory module
            causality: Causality engine
        
        Returns:
            CognitiveState with prediction results
        """
        S = compute_structural_differentiation(network)
        D = causality.current_density
        M = memory.persistence
        
        return self.predict({"S": S, "D": D, "M": M})
    
    def batch_predict(self, param_list: List[Dict[str, Any]]) -> List[CognitiveState]:
        """Run predictions on multiple parameter sets"""
        return [self.predict(params) for params in param_list]
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary of all predictions"""
        if not self.predictions:
            return {"total": 0, "cognitive": 0, "non_cognitive": 0}
        
        cognitive = sum(1 for p in self.predictions if p.phi == 1)
        
        return {
            "total": len(self.predictions),
            "cognitive": cognitive,
            "non_cognitive": len(self.predictions) - cognitive,
            "cognitive_rate": cognitive / len(self.predictions)
        }


def print_prediction(state: CognitiveState):
    """Pretty print a prediction result"""
    status = "🟢 COGNITIVE" if state.phi == 1 else "🔴 NON-COGNITIVE"
    
    print(f"\n{'='*50}")
    print(f"  {status}")
    print(f"{'='*50}")
    print(f"  Parameters:")
    print(f"    S (Structure):  {state.S:.4f}")
    print(f"    D (Density):    {state.D:.4f}")
    print(f"    M (Memory):     {state.M:.4f}")
    print(f"  ")
    print(f"  Capacity (S×D×M): {state.capacity:.6f}")
    print(f"  Threshold:        {state.threshold:.6f}")
    print(f"  Class:            {state.universality_class}")
    print(f"  ")
    print(f"  Active Laws:")
    for law in state.active_laws:
        print(f"    ✅ {law}")
    if not state.active_laws:
        print(f"    ❌ No laws active")
    print(f"{'='*50}")


if __name__ == "__main__":
    # Quick demo
    synthesis = MetaLawSynthesis()
    
    print("\n🧠 COGNITIVE PHYSICS - META-LAW SYNTHESIS")
    print("="*50)
    
    # Test cases
    test_cases = [
        {"name": "Human Brain", "S": 0.85, "D": 0.7, "M": 0.6},
        {"name": "GPT-3", "S": 0.4, "D": 0.9, "M": 0.2},
        {"name": "Twitter Network", "S": 0.9, "D": 0.2, "M": 0.05},
        {"name": "Simple Grid", "S": 0.1, "D": 0.1, "M": 0.01},
    ]
    
    for case in test_cases:
        print(f"\n📊 Testing: {case['name']}")
        state = synthesis.predict(case)
        print_prediction(state)
    
    print("\n📈 Summary:")
    summary = synthesis.get_summary()
    print(f"  Total predictions: {summary['total']}")
    print(f"  Cognitive: {summary['cognitive']}")
    print(f"  Non-cognitive: {summary['non_cognitive']}")
