# Customized-Movie-Recommendation-System-using-Multimodel-Emotion-Analysis
# Text-based emotional analysis model
I have developed an emotional chatbot that will have a conversation with users by asking them five questions. Then the pre-trained transformer model will do an emotional analysis based on the users' answers and detect the users' final emotion with the confidence rate shown. The final emotion will be either one of the seven emotions listed (happy, anger, disgust, fear, neutral, sadness, and surprise).

To execute this code, place both chatbox.py and the associated templates file into the same directory. Run chatbox.py, then access the website by navigating to the URL http://127.0.0.1:5000 displayed in the terminal.
<img width="341" alt="Text-based model" src="https://github.com/user-attachments/assets/1399067a-5e0b-47a5-9530-c8dc69485f27">

# Audio-based emotional analysis model
I have developed an audio-based emotional detection website. Once users click the start recording button, a random picture will appear and users will have ten seconds to describe what happens in the picture. Users can check whether their voices are being recorded by seeing the voice visualization on the website. After ten seconds finish, the predicted emotion with the confidence rate will be shown. The final emotion will be either one of the seven emotions listed (happy, anger, disgust, fear, neutral, sadness, and surprise).

To execute this code, place both voice.py and the associated templates file into the same directory. Run voice.py, then access the website by navigating to the URL http://127.0.0.1:5000 displayed in the terminal.
<img width="401" alt="video-based model" src="https://github.com/user-attachments/assets/d24afed6-ddff-4be1-ae05-71f3835792bb">

# Video-based emotional analysis model
I successfully developed a video-based emotion detection website. When users click the Capture and Start Analysis button, the system initiates active scanning, highlighted by a red bounding box around the user’s face and a blue scanning line moving vertically to indicate the scanning process. During the scan, the detected emotion and its confidence rate are displayed in real-time on the right side of the video feed. Once the blue timeline visualization completes its pass, the final detected emotion, along with its overall confidence rate, is displayed at the bottom of the video. The final result corresponds to one of seven possible emotions: happy, anger, disgust, fear, neutrality, sadness, or surprise.

To execute this code, place both face.py and the associated static file into the same directory. Run face.py, then access the website by navigating to the URL http://127.0.0.1:5000 displayed in the terminal.
<img width="525" alt="Facial expression-based model" src="https://github.com/user-attachments/assets/bb409c98-19f9-4888-84c6-c80ae30434d5">

