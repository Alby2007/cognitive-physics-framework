"""
Core Interface for Cognitive Physics Framework

This module provides the fundamental building blocks:
- CognitiveNetwork: Graph structure with nodes and edges
- MemoryModule: Memory persistence and decay
- CausalityEngine: Causal density tracking
- EmergenceDetector: Detects cognitive emergence

Author: Cognitive Physics Project
License: MIT
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import random
import math


@dataclass
class CognitiveNetwork:
    """
    A network of proto-agents with weighted connections.
    
    Attributes:
        nodes: Dict mapping node_id to node properties (activation, etc.)
        edges: Dict mapping (src, dst) to edge properties (weight, causal_strength)
    """
    nodes: Dict[str, Dict[str, float]] = field(default_factory=dict)
    edges: Dict[Tuple[str, str], Dict[str, float]] = field(default_factory=dict)
    
    def add_node(self, node_id: str, activation: float = 0.0):
        """Add a node to the network"""
        self.nodes[node_id] = {"activation": activation}
    
    def add_edge(self, src: str, dst: str, weight: float = 0.5, causal_strength: float = 0.5):
        """Add an edge between two nodes"""
        self.edges[(src, dst)] = {
            "weight": weight,
            "causal_strength": causal_strength
        }
    
    def propagate(self, steps: int = 1):
        """Propagate activations through the network"""
        for _ in range(steps):
            new_activations = {}
            for node_id in self.nodes:
                incoming = 0.0
                for (src, dst), edge in self.edges.items():
                    if dst == node_id and src in self.nodes:
                        incoming += self.nodes[src]["activation"] * edge["weight"]
                
                current = self.nodes[node_id]["activation"]
                new_activations[node_id] = 0.9 * current + 0.1 * math.tanh(incoming)
            
            for node_id, activation in new_activations.items():
                self.nodes[node_id]["activation"] = activation
    
    def get_degree_distribution(self) -> List[int]:
        """Get the degree distribution of the network"""
        degrees = defaultdict(int)
        for node_id in self.nodes:
            for (src, dst) in self.edges:
                if src == node_id or dst == node_id:
                    degrees[node_id] += 1
        return list(degrees.values())


@dataclass
class MemoryModule:
    """
    Memory system with persistence and decay.
    
    Attributes:
        persistence: How long memories last (0-1)
        memories: Stored memory traces
        proto_language: Emergent symbolic patterns
    """
    persistence: float = 0.05
    memories: Dict[str, float] = field(default_factory=dict)
    proto_language: List[str] = field(default_factory=list)
    
    def store(self, key: str, strength: float = 1.0):
        """Store a memory trace"""
        self.memories[key] = strength
    
    def recall(self, key: str) -> float:
        """Recall a memory (returns strength or 0)"""
        return self.memories.get(key, 0.0)
    
    def decay(self):
        """Apply decay to all memories"""
        decay_rate = 1.0 - self.persistence
        to_remove = []
        
        for key in self.memories:
            self.memories[key] *= (1.0 - decay_rate * 0.1)
            if self.memories[key] < 0.01:
                to_remove.append(key)
        
        for key in to_remove:
            del self.memories[key]
    
    def form_proto_language(self, pattern: str):
        """Form a proto-language symbol from repeated patterns"""
        if pattern not in self.proto_language:
            self.proto_language.append(pattern)


@dataclass
class CausalityEngine:
    """
    Tracks causal relationships and computes causal density.
    
    Attributes:
        events: List of causal events (src, dst, strength)
        current_density: Current causal density measure
    """
    events: List[Tuple[str, str, float]] = field(default_factory=list)
    current_density: float = 0.0
    
    def register_event(self, src: str, dst: str, strength: float):
        """Register a causal event"""
        self.events.append((src, dst, strength))
        self._update_density()
    
    def _update_density(self):
        """Update the current causal density"""
        if len(self.events) == 0:
            self.current_density = 0.0
            return
        
        recent = self.events[-100:]  # Last 100 events
        total_strength = sum(e[2] for e in recent)
        self.current_density = min(1.0, total_strength / max(len(recent), 1))
    
    def get_causal_chain(self, start: str, max_depth: int = 5) -> List[str]:
        """Trace a causal chain from a starting node"""
        chain = [start]
        current = start
        
        for _ in range(max_depth):
            next_nodes = [dst for src, dst, _ in self.events if src == current]
            if not next_nodes:
                break
            current = next_nodes[-1]
            chain.append(current)
        
        return chain


class EmergenceDetector:
    """
    Detects cognitive emergence based on network state.
    
    Checks for:
    - Structural patterns (hubs, bridges, clusters)
    - Causal coherence
    - Memory persistence
    - Proto-language formation
    """
    
    def __init__(self):
        self.detection_history: List[Dict[str, Any]] = []
    
    def detect(self, network: CognitiveNetwork, memory: MemoryModule, 
               causality: CausalityEngine) -> List[Dict[str, Any]]:
        """Detect emergent phenomena"""
        emergences = []
        
        # Check for structural emergence
        degrees = network.get_degree_distribution()
        if degrees:
            max_degree = max(degrees)
            avg_degree = sum(degrees) / len(degrees)
            
            if max_degree > avg_degree * 2:
                emergences.append({
                    "type": "structural_hub",
                    "strength": max_degree / len(degrees)
                })
        
        # Check for causal emergence
        if causality.current_density > 0.2:
            emergences.append({
                "type": "causal_coherence",
                "strength": causality.current_density
            })
        
        # Check for memory-based emergence
        if len(memory.memories) > 5:
            emergences.append({
                "type": "memory_persistence",
                "strength": len(memory.memories) / 10
            })
        
        # Check for proto-language
        if len(memory.proto_language) > 0:
            emergences.append({
                "type": "proto_language",
                "strength": len(memory.proto_language) / 5
            })
        
        self.detection_history.append({
            "emergences": emergences,
            "count": len(emergences)
        })
        
        return emergences


def create_minimal_cognitive_system(
    num_nodes: int = 20,
    connectivity: float = 0.1,
    memory_persistence: float = 0.05
) -> Tuple[CognitiveNetwork, MemoryModule, CausalityEngine, EmergenceDetector]:
    """
    Create a minimal cognitive system with all components.
    
    Args:
        num_nodes: Number of nodes in the network
        connectivity: Edge probability (0-1)
        memory_persistence: Memory decay rate (0-1)
    
    Returns:
        Tuple of (network, memory, causality, detector)
    """
    network = CognitiveNetwork()
    
    # Create nodes
    for i in range(num_nodes):
        network.add_node(f"node_{i}", activation=random.uniform(-0.1, 0.1))
    
    # Create edges
    nodes = list(network.nodes.keys())
    for src in nodes:
        for dst in nodes:
            if src != dst and random.random() < connectivity:
                network.add_edge(
                    src, dst,
                    weight=random.uniform(0.3, 0.7),
                    causal_strength=random.uniform(0.3, 0.7)
                )
    
    memory = MemoryModule(persistence=memory_persistence)
    causality = CausalityEngine()
    detector = EmergenceDetector()
    
    return network, memory, causality, detector


def compute_structural_differentiation(network: CognitiveNetwork) -> float:
    """
    Compute structural differentiation S of a network.
    
    High S = heterogeneous topology (hubs, bridges, clusters)
    Low S = uniform topology
    
    Returns:
        S value between 0 and 1
    """
    degrees = network.get_degree_distribution()
    
    if not degrees:
        return 0.0
    
    avg_degree = sum(degrees) / len(degrees)
    if avg_degree == 0:
        return 0.0
    
    # Coefficient of variation
    variance = sum((d - avg_degree) ** 2 for d in degrees) / len(degrees)
    cv = math.sqrt(variance) / avg_degree
    
    # Hub score
    max_degree = max(degrees)
    hub_score = min(1.0, max_degree / (len(degrees) * 0.3))
    
    # Combined differentiation
    differentiation = min(1.0, cv * 0.5 + hub_score * 0.5)
    
    return differentiation
