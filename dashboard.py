from flask import Flask, jsonify, render_template
import redis
import json
from datetime import datetime

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def index():
    """Serve the main dashboard page."""
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    """Fetch execution metrics from Redis and return JSON."""
    task_metrics = redis_client.get('task_metrics')
    if task_metrics:
        data = json.loads(task_metrics)
        data['timestamps'] = [datetime.strptime(ts, "%H:%M:%S").strftime("%H:%M:%S") for ts in data['timestamps']]
        return jsonify(data)
    return jsonify({"timestamps": [], "durations": []})

if __name__ == '__main__':
    app.run(debug=True, port=5002)




# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.graph_objs as go
# import redis
# import json

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Connect to Redis
# redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# # Layout of the Dashboard
# app.layout = html.Div([
#     html.H1("AI_Health Performance Dashboard"),
    
#     # Task Duration Graph
#     dcc.Graph(id='task-duration-graph'),
    
#     # Auto-refresh Interval (updates every 5 seconds)
#     dcc.Interval(
#         id='interval-component',
#         interval=5000,  # 5000ms = 5 seconds
#         n_intervals=0
#     )
# ])

# # Callback to update the graph
# @app.callback(
#     Output('task-duration-graph', 'figure'),
#     Input('interval-component', 'n_intervals')
# )
# def update_graph(n_intervals):
#     """Fetches latest task metrics from Redis and updates the graph."""
#     data = redis_client.get("task_metrics")
    
#     if data:
#         metrics = json.loads(data)
#         timestamps = metrics.get("timestamps", [])
#         durations = metrics.get("durations", [])

#         figure = {
#             'data': [
#                 go.Scatter(
#                     x=timestamps,
#                     y=durations,
#                     mode='lines+markers',
#                     name='Task Duration'
#                 )
#             ],
#             'layout': go.Layout(
#                 title="Task Durations Over Time",
#                 xaxis={'title': 'Timestamp'},
#                 yaxis={'title': 'Duration (seconds)'},
#                 plot_bgcolor='rgba(255,255,255,1)'
#             )
#         }
#         return figure
#     else:
#         return {
#             'data': [],
#             'layout': go.Layout(title="No Data Available")
#         }

# # Run the Dashboard
# if __name__ == '__main__':
#     app.run_server(debug=True)




# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import redis
# import json
# import pandas as pd
# import plotly.express as px

# # Connect to Redis
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Layout of the dashboard
# app.layout = html.Div(children=[
#     html.H1(children="AI Health Performance Dashboard"),
#     dcc.Graph(id='task-duration-graph'),
#     dcc.Interval(
#         id='interval-component',
#         interval=5000,  # Update every 5 seconds
#         n_intervals=0
#     )
# ])

# # Callback to update the graph
# @app.callback(
#     Output('task-duration-graph', 'figure'),
#     Input('interval-component', 'n_intervals')
# )
# def update_graph(n_intervals):
#     """Fetches data from Redis and updates the graph."""
#     existing_data = redis_client.get("task_metrics")
    
#     if not existing_data:
#         return px.line(title="No Data Available")

#     metrics = json.loads(existing_data)

#     # Convert to DataFrame
#     df = pd.DataFrame({
#         "Timestamp": metrics["timestamps"],
#         "Duration (seconds)": metrics["durations"]
#     })

#     # Create the graph
#     fig = px.line(df, x="Timestamp", y="Duration (seconds)", title="Task Processing Time")

#     return fig

# # Run the dashboard
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)
