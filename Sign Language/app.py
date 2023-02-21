from flask import Flask, render_template, Response, request, redirect
import cv2
from tensorflow.keras.models import load_model
from play_video import predict_model

app = Flask(__name__)
cap = cv2.VideoCapture(0)
model = load_model('data_model/action7.h5', compile=False)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/PlayVideo")
def play_video():
    return render_template("PlayVideo.html")

@app.route("/video_feed")
def video_feed():
    actions = ['Fine', 'He', 'Hello', 'Me', 'Sorry', 'We', 'You']
    return Response(predict_model(cap, actions, model), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__=="__main__":
    app.run(debug=True)
