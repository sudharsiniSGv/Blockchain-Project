# Peer-to-Peer Blockchain Network Simulation

This project simulates a simple **Peer-to-Peer (P2P) Blockchain Network** using Python and Flask. It demonstrates the core concepts of blockchain including transactions, block mining using Proof-of-Work, decentralized node communication, and consensus resolution. The application features a user-friendly web interface for managing transactions and viewing blockchain state, with automatic peer connection for seamless synchronization.

# Objectives

- Simulate a decentralized blockchain network with multiple independent nodes.
- Implement block creation, transaction handling, and proof-of-work mining.
- Ensure data consistency across nodes using a basic consensus algorithm.
- Provide a simple web interface to interact with each node.

# Technologies Used

- Python 3.x
- Flask (Web framework)
- Requests (for inter-node communication)
- HTML/CSS (Frontend)

# Features

- Four independent blockchain nodes, each maintaining a local copy.
- Each node can:
  - Add and mine transactions.
  - View its current blockchain state.
  - Automatically connect to and synchronize with other nodes.
- Implements Proof-of-Work (PoW) to mine blocks.
- Uses a consensus algorithm ("longest valid chain") to resolve conflicts.
- Stylish and clean web interface for interaction — no need for Postman or external tools.

# Launching the Nodes
1.Open 4 terminals and run each command in a separate terminal:

python node1.py
python node2.py
python node3.py
python node4.py

2. Access the Web UI in your browser:

http://127.0.0.1:5001
http://127.0.0.1:5002
http://127.0.0.1:5003
http://127.0.0.1:5004


