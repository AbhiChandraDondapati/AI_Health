# AI_Health: Enterprise AI Agent Operating System Prototype

This project demonstrates a prototype for an agent operating system that supports vertical AI agents in an enterprise environment. It includes:

1. **System Architecture:**  
   - A modular design with multiple agents.
   - A communication framework (RabbitMQ) for inter-agent collaboration.

2. **Agent Development:**  
   - **Treatment Recommendation Agent:** Provides treatment recommendations using a dummy ML model.  
   - **Data Analysis Agent:** Subscribes to insights in real-time and performs basic analytics.
   - Both agents share data and insights via RabbitMQ.

3. **Machine Learning Integration:**  
   - The Treatment Recommendation Agent integrates a dummy ML model.
   - The model can be updated dynamically through an endpoint.

4. **Performance Monitoring:**  
   - A dashboard endpoint in the Treatment Recommendation Agent shows performance metrics (e.g., task completion time, request count).

5. **Bonus - Reinforcement Learning Module:**  
   - A feedback endpoint allows simulated reinforcement learning updates to improve recommendations over time.

## Prerequisites

- **Python 3.x:** [Download from python.org](https://www.python.org/downloads/)
- **Visual Studio Code:** [Download VS Code](https://code.visualstudio.com/)
- **RabbitMQ:**  
  - Install **Erlang**: [Download Erlang](https://www.erlang.org/downloads)  
  - Install **RabbitMQ**: [RabbitMQ on Windows](https://www.rabbitmq.com/install-windows.html)  
  - Start the RabbitMQ service after installation.

## Setup Instructions

1. Clone or download this repository into your **AI_Health** folder.
2. Open the folder in Visual Studio Code.
3. Create and activate a virtual environment:

   ```bash
   cd AI_Health
   python -m venv venv
   venv\Scripts\activate
