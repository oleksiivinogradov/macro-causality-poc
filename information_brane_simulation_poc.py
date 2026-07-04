import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

class InformationBraneSimulation:
    """
    Simulation of topological probability collapse on an Information Brane 
    using the Least Action Principle to minimize informational debt.
    """
    def __init__(self, num_agents=60, num_connections=60, learning_rate=0.05):
        self.num_agents = num_agents
        self.lr = learning_rate
        
        # Initialize phase space (Brane) with maximum entropy (random coordinates)
        self.positions = np.random.rand(num_agents, 2) * 100
        
        # Generate informational debt (Quantum entanglement / Strings / Transactions)
        self.graph = nx.gnm_random_graph(num_agents, num_connections)
        self.adjacency = nx.to_numpy_array(self.graph)

    def step(self):
        """
        One epoch of gradient calculation and agent shift (Least Action).
        The system routes events to minimize overall network tension.
        """
        gradients = np.zeros_like(self.positions)
        
        for i in range(self.num_agents):
            for j in range(self.num_agents):
                if self.adjacency[i, j] == 1:
                    # Attraction vector (minimizing informational debt)
                    diff = self.positions[i] - self.positions[j]
                    gradients[i] -= diff * 0.1 
                    
            # Add Brownian noise (kinetic energy of the environment)
            gradients[i] += (np.random.rand(2) - 0.5) * 2.0
            
        # Update positions based on gradients
        self.positions += gradients * self.lr

if __name__ == "__main__":
    print("Initiating quantum graph on the Information Brane...")
    sim = InformationBraneSimulation()

    # Set up the animation window
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)

    def update(frame):
        ax.clear()
        # Fix phase space boundaries
        ax.set_xlim(-20, 120)
        ax.set_ylim(-20, 120)
        ax.set_title(
            f"Epoch {frame}: Minimizing Informational Debt (Least Action Principle)\nEmergent Macro-Causality Clustering", 
            fontsize=14
        )
        
        # Execute one simulation step
        sim.step()
        
        # Render the current state of the graph
        nx.draw(
            sim.graph, 
            pos=sim.positions, 
            ax=ax, 
            node_size=60, 
            node_color='darkred', 
            edge_color='gray', 
            alpha=0.7
        )

    # Run animation (200 frames, 50ms per frame)
    ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)

    print("Rendering macro-events. Close the window to exit.")
    plt.show()