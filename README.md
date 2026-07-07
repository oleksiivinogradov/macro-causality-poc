# Emergent Macro-Causality: Proof of Concept

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20828211.svg)](https://doi.org/10.5281/zenodo.20828211)

This repository contains the computational Proof of Concept (PoC) for the theoretical framework introduced in the preprint:
[**Emergent Macro-Causality: A Holographic Approach to Predictive Modeling on Information Branes**](https://doi.org/10.5281/zenodo.20828211).

## Overview
Current predictive models in complex multi-agent systems often fail to predict emergent, non-linear macro-events. This simulation demonstrates a novel topological routing approach using the **Least Action Principle**. 

By treating complex systems as "Information Branes" and modeling system entropy as "informational debt," this script visualizes how a network spontaneously routes events to minimize global tension, leading to the emergence of macroscopic attractors (clusters).

## Features
* **Maximum Entropy Initialization:** Agents are spawned in a 2D phase space with random coordinates.
* **Informational Debt Generation:** A dynamic adjacency matrix represents unresolved transactions or "quantum entanglement" between agents.
* **Topological Probability Collapse:** A custom gradient descent algorithm forces connected nodes to cluster, overcoming simulated Brownian noise (kinetic energy).
* **Multi-Topology Support:** The simulation now supports stress-testing the framework across different network topologies to observe the robustness of macro-causality:
  * Erdős-Rényi (`random`)
  * Watts-Strogatz (`small_world`)
  * Barabási-Albert (`scale_free`)

## Requirements
To run the simulation, you will need Python 3 installed along with the following libraries:

```bash
pip install numpy matplotlib networkx
