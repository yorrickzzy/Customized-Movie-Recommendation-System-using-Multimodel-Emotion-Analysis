from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

emotion_labels = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sadness', 'surprise']


def analyze_emotion(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=-1)
    emotion_scores = predictions[0].tolist()
    return emotion_scores

@app.route('/')
def home():
    return render_template('chatbox.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_text = data['text']
    question_index = data['question_index']

    emotion_scores = analyze_emotion(user_text)
    
    return jsonify({
        'emotion_scores': emotion_scores,
        'question_index': question_index
    })

@app.route('/finalize', methods=['POST'])
def finalize():
    data = request.json
    emotion_scores = data['scores']  
    
    total_scores = [sum(x) for x in zip(*emotion_scores)]
    
    max_index = total_scores.index(max(total_scores))
    emotion = emotion_labels[max_index]
    confidence = max(total_scores) * 100 / len(emotion_scores)  

    return jsonify({
        'emotion': emotion,
        'confidence': f"{confidence:.2f}%"
    })

if __name__ == '__main__':
    app.run(debug=True)

