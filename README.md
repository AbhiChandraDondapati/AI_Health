AI_Health: Enterprise AI Agent Operating System Prototype

This project demonstrates a prototype for an agent operating system that supports vertical AI agents in an enterprise environment. It includes:

1. System Architecture: 
   - A modular design with multiple agents.
   - A communication framework (RabbitMQ) for inter-agent collaboration.

2. Agent Development: 
   - Treatment Recommendation Agent: 
     - Provides treatment recommendations using a dummy ML model.
     - Offers endpoints to update the model dynamically and accept reinforcement by learning feedback.
     - Publishes insights in real time via RabbitMQ.
   - Data Analysis Agent:
     - Subscribes to insights in real time.
     - Aggregates and prints data analytics (e.g., treatment counts).

3. Machine Learning Integration:
   - The Treatment Recommendation Agent includes a dummy ML model.
   - A dynamic model update endpoint simulates model retraining.
   - Saves the model (model.pkl) so that our Flask API can use it later

4. Performance Monitoring Dashboard:
   - A dashboard endpoint displays performance metrics such as:
     - Request count and task completion (response) time.
     - Dummy “accuracy” metric.
     - Resource utilization (CPU and memory usage).
     - Model version and RL score.

5. Bonus – Reinforcement Learning Module:  
   - A feedback endpoint simulates a reinforcement learning update that adjusts an internal RL score and accuracy metric over time.

## Prerequisites

- Python 3.x: [Download from python.org](https://www.python.org/downloads/)
- Visual Studio Code: [Download VS Code](https://code.visualstudio.com/)
- RabbitMQ:  
  - Install Erlang: [Download Erlang](https://www.erlang.org/downloads)  
  - Install RabbitMQ: [RabbitMQ on Windows](https://www.rabbitmq.com/install-windows.html)  
  - After installation, start the RabbitMQ service.

## Setup Instructions

1. Clone or download this repository into your AI_Health folder.
2. Open the folder in Visual Studio Code.
3. Create and activate a virtual environment:

   ```bash
   cd AI_Health
   python -m venv venv
   venv\Scripts\activate


Basic Overview of this project: -
- My project has a Flask-based API, Celery workers, and Redis/RabbitMQ for task processing, forming a distributed system.
- Celery + Redis/RabbitMQ facilitates communication between different components in the project.
- Tasks are sent asynchronously from Flask (API) → Celery workers → Redis dashboard.
- Two Agents are implemented, 
   •	Treatment Recommendation Agent 
   •	Performance Monitoring Agent 
- Real-time data sharing
- Trained ML model recommends treatments based on input patient data.
- The Flask API loads the model each time a request is made.
- Build a dashboard to monitor AI agent performance.

Please have a look at AI_Health/Outputs.docx for key outputs for this project.
