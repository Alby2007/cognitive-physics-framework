"""
Example Networks for Cognitive Physics Framework

Pre-defined networks representing real-world systems:
- Biological: C. elegans, human brain
- Artificial: GPT-3, simple neural net
- Social: Twitter, corporate organization

Each network includes estimated S, D, M values based on
known properties of these systems.

Author: Cognitive Physics Project
License: MIT
"""

from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class ExampleNetwork:
    """An example network with known properties"""
    name: str
    description: str
    category: str
    S: float  # Structural differentiation
    D: float  # Causal density
    M: float  # Memory persistence
    nodes: int
    expected_cognitive: bool
    notes: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "S": self.S,
            "D": self.D,
            "M": self.M,
            "nodes": self.nodes,
            "expected_cognitive": self.expected_cognitive,
            "notes": self.notes
        }


# =============================================================================
# BIOLOGICAL NETWORKS
# =============================================================================

C_ELEGANS = ExampleNetwork(
    name="C. elegans Connectome",
    description="Complete neural wiring of the nematode C. elegans",
    category="biological",
    S=0.70,  # High hub structure (command neurons)
    D=0.40,  # Moderate synaptic activity
    M=0.30,  # Good memory for simple organism
    nodes=302,
    expected_cognitive=True,
    notes="First complete connectome mapped. Shows clear hub-and-spoke topology."
)

FRUIT_FLY = ExampleNetwork(
    name="Drosophila Brain",
    description="Fruit fly brain connectome",
    category="biological",
    S=0.75,
    D=0.50,
    M=0.40,
    nodes=100000,
    expected_cognitive=True,
    notes="Complex sensory processing and learning capabilities."
)

MOUSE_BRAIN = ExampleNetwork(
    name="Mouse Brain",
    description="Mammalian brain with cortical organization",
    category="biological",
    S=0.80,
    D=0.60,
    M=0.50,
    nodes=70000000,
    expected_cognitive=True,
    notes="Clear hierarchical structure with specialized regions."
)

HUMAN_BRAIN = ExampleNetwork(
    name="Human Brain",
    description="Human cerebral cortex",
    category="biological",
    S=0.85,  # Highly differentiated (hubs, modules, hierarchy)
    D=0.70,  # High neural activity
    M=0.60,  # Strong memory systems
    nodes=86000000000,
    expected_cognitive=True,
    notes="Most complex known cognitive system. Grammar-structural class."
)


# =============================================================================
# ARTIFICIAL NETWORKS
# =============================================================================

BERT_BASE = ExampleNetwork(
    name="BERT-base",
    description="Bidirectional transformer (110M parameters)",
    category="artificial",
    S=0.30,  # Relatively uniform attention
    D=0.80,  # High activation density
    M=0.10,  # Context window only
    nodes=110000000,
    expected_cognitive=True,
    notes="Dense-dynamical class. Compensates low S with high D."
)

GPT2 = ExampleNetwork(
    name="GPT-2",
    description="Autoregressive transformer (1.5B parameters)",
    category="artificial",
    S=0.35,
    D=0.85,
    M=0.15,
    nodes=1500000000,
    expected_cognitive=True,
    notes="Larger context enables more memory-like behavior."
)

GPT3 = ExampleNetwork(
    name="GPT-3",
    description="Large language model (175B parameters)",
    category="artificial",
    S=0.40,
    D=0.90,
    M=0.20,
    nodes=175000000000,
    expected_cognitive=True,
    notes="Dense-dynamical class. Emergent capabilities at scale."
)

GPT4 = ExampleNetwork(
    name="GPT-4 (estimated)",
    description="Multimodal large language model",
    category="artificial",
    S=0.45,
    D=0.92,
    M=0.25,
    nodes=1000000000000,  # Estimated
    expected_cognitive=True,
    notes="Estimated values. Shows increasing S with scale."
)

SIMPLE_MLP = ExampleNetwork(
    name="Simple MLP",
    description="3-layer multilayer perceptron",
    category="artificial",
    S=0.20,  # Very uniform
    D=0.30,  # Low activation
    M=0.01,  # No memory
    nodes=1000,
    expected_cognitive=False,
    notes="Too simple for cognitive emergence."
)


# =============================================================================
# SOCIAL NETWORKS
# =============================================================================

TWITTER = ExampleNetwork(
    name="Twitter/X Network",
    description="Social media follower graph",
    category="social",
    S=0.90,  # Extreme power-law (influencers)
    D=0.20,  # Sparse interactions
    M=0.05,  # Short attention span
    nodes=300000000,
    expected_cognitive=True,
    notes="Fast-propagation class. Viral dynamics, low memory."
)

FACEBOOK = ExampleNetwork(
    name="Facebook Network",
    description="Social connections graph",
    category="social",
    S=0.85,
    D=0.25,
    M=0.08,
    nodes=3000000000,
    expected_cognitive=True,
    notes="More persistent connections than Twitter."
)

CORPORATE_ORG = ExampleNetwork(
    name="Corporate Organization",
    description="Fortune 500 company structure",
    category="social",
    S=0.80,  # Clear hierarchy
    D=0.30,  # Regular meetings/communications
    M=0.15,  # Institutional memory
    nodes=10000,
    expected_cognitive=True,
    notes="Slow-memory class. Institutional knowledge persists."
)

SMALL_TEAM = ExampleNetwork(
    name="Small Team",
    description="10-person startup team",
    category="social",
    S=0.50,  # Relatively flat
    D=0.60,  # High interaction
    M=0.40,  # Strong shared memory
    nodes=10,
    expected_cognitive=True,
    notes="High density compensates for small size."
)

GOVERNMENT = ExampleNetwork(
    name="Government Bureaucracy",
    description="Large government organization",
    category="social",
    S=0.75,
    D=0.25,
    M=0.20,
    nodes=100000,
    expected_cognitive=True,
    notes="Slow-memory class. Very persistent institutional memory."
)


# =============================================================================
# INFRASTRUCTURE NETWORKS
# =============================================================================

INTERNET_AS = ExampleNetwork(
    name="Internet AS Topology",
    description="Autonomous systems routing graph",
    category="infrastructure",
    S=0.90,  # Extreme hub structure (Tier 1 providers)
    D=0.30,  # Packet routing
    M=0.02,  # Stateless routing
    nodes=70000,
    expected_cognitive=True,
    notes="Fast-propagation class. Highly resilient."
)

POWER_GRID = ExampleNetwork(
    name="US Power Grid",
    description="Electrical transmission network",
    category="infrastructure",
    S=0.60,
    D=0.20,
    M=0.01,  # No memory
    nodes=5000,
    expected_cognitive=False,
    notes="Below threshold. No cognitive properties expected."
)

SUPPLY_CHAIN = ExampleNetwork(
    name="Global Supply Chain",
    description="International trade network",
    category="infrastructure",
    S=0.80,
    D=0.15,
    M=0.03,
    nodes=50000,
    expected_cognitive=True,
    notes="Borderline. Emergent coordination behaviors."
)


# =============================================================================
# ECOSYSTEM NETWORKS
# =============================================================================

RAINFOREST = ExampleNetwork(
    name="Rainforest Ecosystem",
    description="Species interaction network",
    category="ecosystem",
    S=0.85,  # Keystone species as hubs
    D=0.30,  # Ecological interactions
    M=0.40,  # Long-term adaptation
    nodes=10000000,
    expected_cognitive=True,
    notes="Slow-memory class. Collective intelligence of ecosystem."
)

CORAL_REEF = ExampleNetwork(
    name="Coral Reef Ecosystem",
    description="Marine ecosystem network",
    category="ecosystem",
    S=0.80,
    D=0.35,
    M=0.35,
    nodes=1000000,
    expected_cognitive=True,
    notes="Complex symbiotic relationships."
)


# =============================================================================
# COLLECTIONS
# =============================================================================

BIOLOGICAL_NETWORKS = [C_ELEGANS, FRUIT_FLY, MOUSE_BRAIN, HUMAN_BRAIN]
ARTIFICIAL_NETWORKS = [BERT_BASE, GPT2, GPT3, GPT4, SIMPLE_MLP]
SOCIAL_NETWORKS = [TWITTER, FACEBOOK, CORPORATE_ORG, SMALL_TEAM, GOVERNMENT]
INFRASTRUCTURE_NETWORKS = [INTERNET_AS, POWER_GRID, SUPPLY_CHAIN]
ECOSYSTEM_NETWORKS = [RAINFOREST, CORAL_REEF]

ALL_NETWORKS = (
    BIOLOGICAL_NETWORKS + 
    ARTIFICIAL_NETWORKS + 
    SOCIAL_NETWORKS + 
    INFRASTRUCTURE_NETWORKS + 
    ECOSYSTEM_NETWORKS
)


def get_networks_by_category(category: str) -> List[ExampleNetwork]:
    """Get all networks in a category"""
    return [n for n in ALL_NETWORKS if n.category == category]


def get_cognitive_networks() -> List[ExampleNetwork]:
    """Get all networks expected to be cognitive"""
    return [n for n in ALL_NETWORKS if n.expected_cognitive]


def get_non_cognitive_networks() -> List[ExampleNetwork]:
    """Get all networks expected to be non-cognitive"""
    return [n for n in ALL_NETWORKS if not n.expected_cognitive]


if __name__ == "__main__":
    print("\n📊 EXAMPLE NETWORKS FOR COGNITIVE PHYSICS")
    print("="*60)
    
    categories = ["biological", "artificial", "social", "infrastructure", "ecosystem"]
    
    for cat in categories:
        networks = get_networks_by_category(cat)
        print(f"\n{cat.upper()} ({len(networks)} networks):")
        print("-"*40)
        
        for net in networks:
            status = "✅" if net.expected_cognitive else "❌"
            capacity = net.S * net.D * net.M
            print(f"  {status} {net.name}")
            print(f"     S={net.S:.2f}, D={net.D:.2f}, M={net.M:.2f}")
            print(f"     Capacity: {capacity:.4f}")
    
    print(f"\n📈 SUMMARY:")
    print(f"  Total networks: {len(ALL_NETWORKS)}")
    print(f"  Expected cognitive: {len(get_cognitive_networks())}")
    print(f"  Expected non-cognitive: {len(get_non_cognitive_networks())}")
