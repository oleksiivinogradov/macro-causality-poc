import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

class InformationBraneSimulation:
    def __init__(self, num_agents=60, num_connections=60, topology='random', learning_rate=0.05):
        self.num_agents = num_agents
        self.lr = learning_rate
        self.topology = topology
        
        # 1. Initialize Phase Space (Brane) with maximum entropy (random coordinates)
        self.positions = np.random.rand(num_agents, 2) * 100
        
        # 2. Generate Topology (Informational debt / Entanglement)
        # Added topologies based on Dr. Levada's recommendation
        if topology == 'random':
            # Erdős-Rényi random graph
            self.graph = nx.gnm_random_graph(num_agents, num_connections)
        elif topology == 'small_world':
            # Watts-Strogatz small-world graph
            self.graph = nx.watts_strogatz_graph(num_agents, k=4, p=0.1)
        elif topology == 'scale_free':
            # Barabási-Albert scale-free graph
            self.graph = nx.barabasi_albert_graph(num_agents, m=2)
        else:
            raise ValueError("Unknown topology. Choose 'random', 'small_world', or 'scale_free'.")

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
    # You can change the topology here to 'random', 'small_world', or 'scale_free'
    selected_topology = 'scale_free' 
    
    print(f"Initiating quantum graph on the Information Brane using '{selected_topology}' topology...")
    sim = InformationBraneSimulation(topology=selected_topology)

    # Set up the animation window
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)

    def update(frame):
        ax.clear()
        # Fix phase space boundaries
        ax.set_xlim(-20, 120)
        ax.set_ylim(-20, 120)
        ax.set_title(
            f"Epoch {frame}: Minimizing Informational Debt (Least Action Principle)\nTopology: {selected_topology.replace('_', ' ').title()}", 
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

    # Run animation
    ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)

    print("Rendering macro-events. Close the window to exit.")
    plt.show()
