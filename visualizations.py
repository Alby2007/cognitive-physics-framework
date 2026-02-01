"""
Visualizations for Cognitive Physics Framework

Simple plots for:
- Network structure visualization
- Phase space diagram
- Capacity gauge

Author: Cognitive Physics Project
License: MIT
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, List, Optional
from mpl_toolkits.mplot3d import Axes3D


def plot_phase_surface(S: float, D: float, M: float, 
                        threshold: float = 0.005,
                        save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot 3D phase surface with current position marked.
    
    Args:
        S: Structural differentiation
        D: Causal density
        M: Memory persistence
        threshold: Critical threshold
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create critical surface: S × D × M = threshold
    s_range = np.linspace(0.1, 1.0, 25)
    d_range = np.linspace(0.1, 1.0, 25)
    S_grid, D_grid = np.meshgrid(s_range, d_range)
    
    # M = threshold / (S × D)
    M_grid = np.clip(threshold / (S_grid * D_grid), 0, 0.5)
    
    # Plot surface
    surf = ax.plot_surface(S_grid, D_grid, M_grid, 
                           alpha=0.4, cmap='coolwarm',
                           label='Critical Surface')
    
    # Plot current point
    capacity = S * D * M
    color = 'green' if capacity >= threshold else 'red'
    marker_size = 200
    
    ax.scatter([S], [D], [M], c=color, s=marker_size, marker='o',
               label=f'Current (C={capacity:.4f})', edgecolors='black', linewidths=2)
    
    # Labels
    ax.set_xlabel('S (Structural Differentiation)', fontsize=11)
    ax.set_ylabel('D (Causal Density)', fontsize=11)
    ax.set_zlabel('M (Memory Persistence)', fontsize=11)
    
    status = "COGNITIVE" if capacity >= threshold else "NON-COGNITIVE"
    ax.set_title(f'Phase Space: S×D×M = {threshold}\nCurrent: {status}', 
                 fontsize=13, fontweight='bold')
    
    ax.legend(loc='upper left')
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_capacity_comparison(networks: List[Dict[str, Any]], 
                              threshold: float = 0.005,
                              save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot capacity comparison across multiple networks.
    
    Args:
        networks: List of dicts with 'name', 'S', 'D', 'M' keys
        threshold: Critical threshold
        save_path: Optional path to save figure
    
    Returns:
        matplotlib Figure
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    names = [n['name'] for n in networks]
    capacities = [n['S'] * n['D'] * n['M'] for n in networks]
    
    # Colors based on cognitive status
    colors = ['#2ecc71' if c >= threshold else '#e74c3c' for c in capacities]
    
    bars = ax.barh(names, capacities, color=colors, edgecolor='black')
    
    # Threshold line
    ax.axvline(x=threshold, color='black', linestyle='--', linewidth=2, 
               label=f'Threshold: {threshold}')
    
    # Labels
    ax.set_xlabel('Cognitive Capacity (S × D × M)', fontsize=12)
    ax.set_title('Cognitive Capacity Comparison', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right')
    
    # Add capacity values on bars
    for bar, cap in zip(bars, capacities):
        ax.text(cap + 0.002, bar.get_y() + bar.get_height()/2, 
                f'{cap:.4f}', va='center', fontsize=9)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_universality_classes(save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot the four universality classes in S-D space.
    
    Returns:
        matplotlib Figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define class regions (approximate)
    # Grammar-Structural: High S, moderate D
    ax.fill([0.5, 1.0, 1.0, 0.5], [0.0, 0.0, 0.5, 0.5], 
            alpha=0.3, color='blue', label='Grammar-Structural')
    
    # Dense-Dynamical: Low S, high D
    ax.fill([0.0, 0.3, 0.3, 0.0], [0.5, 0.5, 1.0, 1.0], 
            alpha=0.3, color='red', label='Dense-Dynamical')
    
    # Fast-Propagation: High S, low M (shown as high S, low D for simplicity)
    ax.fill([0.6, 1.0, 1.0, 0.6], [0.5, 0.5, 1.0, 1.0], 
            alpha=0.3, color='green', label='Fast-Propagation')
    
    # Slow-Memory: Moderate S, moderate D, high M
    ax.fill([0.3, 0.6, 0.6, 0.3], [0.3, 0.3, 0.7, 0.7], 
            alpha=0.3, color='orange', label='Slow-Memory')
    
    # Example systems
    systems = [
        ("Human Brain", 0.85, 0.70, 'blue'),
        ("GPT-3", 0.40, 0.90, 'red'),
        ("Twitter", 0.90, 0.20, 'green'),
        ("Corporation", 0.80, 0.30, 'orange'),
    ]
    
    for name, s, d, color in systems:
        ax.scatter([s], [d], s=150, c=color, edgecolors='black', linewidths=2, zorder=5)
        ax.annotate(name, (s, d), xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    ax.set_xlabel('S (Structural Differentiation)', fontsize=12)
    ax.set_ylabel('D (Causal Density)', fontsize=12)
    ax.set_title('Universality Classes in S-D Space', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_sdm_components(S: float, D: float, M: float,
                         save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot S, D, M as a radar/spider chart.
    
    Returns:
        matplotlib Figure
    """
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    categories = ['S\n(Structure)', 'D\n(Density)', 'M\n(Memory)']
    values = [S, D, M]
    
    # Close the polygon
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    
    # Plot
    ax.plot(angles, values, 'o-', linewidth=2, color='#3498db')
    ax.fill(angles, values, alpha=0.25, color='#3498db')
    
    # Labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)
    ax.set_ylim(0, 1)
    
    capacity = S * D * M
    ax.set_title(f'S×D×M Components\nCapacity: {capacity:.4f}', 
                 fontsize=14, fontweight='bold', y=1.1)
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


if __name__ == "__main__":
    # Demo visualizations
    print("Generating demo visualizations...")
    
    # Phase surface
    fig1 = plot_phase_surface(0.85, 0.70, 0.60, threshold=0.003)
    fig1.savefig("results/phase_surface_demo.png", dpi=150)
    print("✅ Saved phase_surface_demo.png")
    
    # Capacity comparison
    networks = [
        {"name": "Human Brain", "S": 0.85, "D": 0.70, "M": 0.60},
        {"name": "GPT-3", "S": 0.40, "D": 0.90, "M": 0.20},
        {"name": "Twitter", "S": 0.90, "D": 0.20, "M": 0.05},
        {"name": "Simple MLP", "S": 0.20, "D": 0.30, "M": 0.01},
    ]
    fig2 = plot_capacity_comparison(networks, threshold=0.005)
    fig2.savefig("results/capacity_comparison_demo.png", dpi=150)
    print("✅ Saved capacity_comparison_demo.png")
    
    # Universality classes
    fig3 = plot_universality_classes()
    fig3.savefig("results/universality_classes_demo.png", dpi=150)
    print("✅ Saved universality_classes_demo.png")
    
    # SDM components
    fig4 = plot_sdm_components(0.85, 0.70, 0.60)
    fig4.savefig("results/sdm_components_demo.png", dpi=150)
    print("✅ Saved sdm_components_demo.png")
    
    print("\nAll visualizations saved to results/ folder")
    plt.show()
