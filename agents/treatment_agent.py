
#ML MOdle
from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
from communication.message_queue import send_message

app = Flask(__name__)

# Get absolute path of the model file
MODEL_PATH = os.path.abspath("ml_model/model.pkl")

@app.route('/recommend', methods=['POST'])
def recommend_treatment():
    """Receives patient data and recommends a treatment plan."""
    try:
        with open("ml_model/model.pkl", "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        return jsonify({"error": "Model not found. Run train_model.py first."}), 500

    data = request.json.get('features', [])
    if not data:
        return jsonify({"error": "No patient data provided"}), 400

    prediction = int(model.predict([np.array(data)])[0])

    send_message.delay('dashboard', {"recommendation": prediction})

    return jsonify({"treatment_recommendation": prediction})

    prediction = model.predict([np.array(data)])[0]

    # ✅ Convert NumPy int64 to standard Python int
    prediction = int(prediction.item())  # ✅ Use `.item()` to ensure JSON serialization works

    # Send recommendation to the performance dashboard
    send_message.delay('dashboard', {"recommendation": prediction})

    return jsonify({"treatment_recommendation": prediction})

if __name__ == "__main__":
    app.run(port=5001, debug=True)

    # #rl model
# from flask import Flask, request, jsonify
# from agents.rl_treatment_agent import recommend_treatment, update_treatment_feedback

# app = Flask(__name__)

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     """Receives patient data and recommends a treatment using RL."""
#     data = request.json.get('features', [])
#     if not data:
#         return jsonify({"error": "No patient data provided"}), 400

#     recommendation = recommend_treatment(data)
#     return jsonify({"treatment_recommendation": recommendation})

# @app.route('/feedback', methods=['POST'])
# def feedback():
#     """Receives feedback on a treatment's success/failure and updates RL agent."""
#     data = request.json
#     patient_data = data.get('features', [])
#     action_taken = data.get('action')
#     success = data.get('success')

#     if not patient_data or action_taken is None or success is None:
#         return jsonify({"error": "Incomplete feedback data"}), 400

#     update_treatment_feedback(patient_data, action_taken, success)
#     return jsonify({"message": "Feedback received, RL agent updated!"})

# if __name__ == "__main__":
#     app.run(port=5001, debug=True)



