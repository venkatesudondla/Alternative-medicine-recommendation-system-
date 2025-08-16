from flask import Flask, render_template, request, jsonify
import json
from chatbot import get_response

app = Flask(__name__)

def load_remedies():
    with open('remedies.json') as f:
        return json.load(f)

def load_ehr():
    with open('ehr_data.json') as f:
        return json.load(f)

def load_feedback():
    with open('feedback.json') as f:
        return json.load(f)

def save_feedback(new_entry):
    data = load_feedback()
    data.append(new_entry)
    with open('feedback.json', 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_remedies', methods=['POST'])
def get_remedies():
    user_id = request.json['user_id']
    ehr = load_ehr()
    remedies = load_remedies()

    user_conditions = ehr.get(user_id, {}).get('conditions', [])
    matched = [r for r in remedies if r['condition'] in user_conditions]
    return jsonify(matched)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = get_response(message)
    return jsonify({'response': response})

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    save_feedback(data)
    return jsonify({'message': 'Feedback saved'})

@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    return jsonify(load_feedback())

if __name__ == '__main__':
    app.run(debug=True)
