from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import math
import threading
import time

app = Flask(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

letter = ''
sentence = []

handNo = 0

def detect_hands():
    global letter
    global sentence
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        while True:
            success, image = cap.read()
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)
            image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                myHand = results.multi_hand_landmarks[handNo]
                lmList = []

                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    for id, lm, in enumerate(myHand.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])

                if len(lmList) != 0:
                    x1, y1 = lmList[8][1], lmList[8][2]
                    x2, y2 = lmList[12][1], lmList[12][2]
                    x3, y3 = lmList[16][1], lmList[16][2]
                    x4, y4 = lmList[20][1], lmList[20][2]
                    x5, y5 = lmList[4][1], lmList[4][2]

                    lengthIndexMiddle = math.hypot(x2 - x1, y2 - y1)
                    lengthMiddleRing = math.hypot(x3 - x2, y3 - y2)
                    lengthRingPinky = math.hypot(x4 - x3, y4 - y3)
                    lengthThumbMiddle = math.hypot(x5 - x2, y5 - y2)
                    lengthIndexThumb = math.hypot(x5 - x1, y5 - y1)
                    lengthPinkyThumb = math.hypot(x5 - x4, y5 - y4)

                    if len(lmList) == 0:
                        letter = ''
                    elif lmList[4][1] > lmList[3][1] and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2] and lmList[20][2] < lmList[18][2]:
                        letter = 'B'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[4][1] < lmList[3][1] and lengthPinkyThumb > 40 and lmList[8][1] > lmList[4][1]:
                        letter = 'A'
                    elif lmList[4][1] < lmList[3][1] and lengthIndexMiddle < 20 and lengthMiddleRing < 20 and lengthRingPinky < 20 and lengthIndexThumb > 40:
                        letter = 'C'
                    elif lengthThumbMiddle < 30 and lengthMiddleRing < 30 and lengthRingPinky < 30 and lmList[8][2] < lmList[6][2] and lmList[8][1] > lmList[12][1]:
                        letter = 'D'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[4][1] > lmList[3][1] and lmList[4][2] > lmList[7][2] and lmList[4][2] > lmList[11][2] and lmList[4][2] > lmList[15][2] and lengthPinkyThumb > 40:
                        letter = 'E'
                    elif lengthIndexThumb < 20 and lmList[8][2] > lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] < lmList[14][2] and lmList[20][2] < lmList[18][2]:
                        letter = 'F'
                    elif lmList[8][1] < lmList[6][1] and lmList[12][1] > lmList[10][1] and lmList[16][1] > lmList[14][1] and lmList[20][1] > lmList[18][1] and lmList[4][1] > lmList[8][1] and lmList[8][2] < lmList[14][2] and lmList[4][2] > lmList[8][2]:
                        letter = 'G'
                    elif lmList[8][1] < lmList[6][1] and lmList[12][1] < lmList[10][1] and lmList[16][1] > lmList[14][1] and lmList[20][1] > lmList[18][1] and lmList[4][1] > lmList[8][1] and lmList[12][2] < lmList[14][2]:
                        letter = 'H'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] < lmList[18][2] and lmList[4][1] > lmList[3][1] and lengthPinkyThumb > 50:
                        letter = 'I'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] < lmList[18][2] and lmList[20][1] < lmList[16][1]:
                        letter = 'J'
                    elif lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[4][2] < lmList[18][2] and lmList[8][1] < lmList[12][1] and lmList[4][1] > lmList[8][1] and lmList[4][1] < lmList[10][1]:
                        letter = 'K'
                    elif lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[8][2] < lmList[6][2] and lmList[4][1] < lmList[8][1] and lengthThumbMiddle > 50 and lmList[8][1] < lmList[12][1]:
                        letter = 'L'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[4][2] < lmList[18][2] and lmList[4][1] > lmList[14][1]:
                        letter = 'M'
                    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[4][2] < lmList[14][2] and lmList[4][1] > lmList[10][1]:
                        letter = 'N'
                    elif lengthIndexMiddle < 30 and lengthMiddleRing < 30 and lengthRingPinky < 30 and lengthThumbMiddle < 30:
                        letter = 'O'
                    elif lmList[8][2] > lmList[4][2] and lmList[12][2] > lmList[4][2] and lmList[12][2] > lmList[8][2] and lengthPinkyThumb < 70:
                        letter = 'P'
                    elif lmList[8][2] > lmList[10][2] and lmList[4][2] > lmList[10][2] and lmList[8][2] > lmList[12][2] and lmList[8][2] > lmList[16][2] and lmList[4][2] > lmList[12][2] and lmList[4][2] > lmList[16][2]:
                        letter = 'Q'
                    elif lmList[8][2] < lmList[16][2] and lmList[12][2] < lmList[16][2] and lmList[8][1] > lmList[12][1] and lmList[8][1] < lmList[4][1]:
                        letter = 'R'
                    elif lmList[4][2] < lmList[12][2] and lmList[4][2] < lmList[16][2] and lmList[4][1] > lmList[10][1]:
                        letter = 'S'
                    elif lmList[4][2] < lmList[12][2] and lmList[6][2] < lmList[10][2] and lmList[6][1] > lmList[8][1] and lmList[8][1] < lmList[4][1]:
                        letter = 'T'
                    elif lmList[8][2] < lmList[14][2] and lmList[12][2] < lmList[14][2] and lmList[4][1] > lmList[8][1] and lengthIndexMiddle < 40:
                        letter = 'U'
                    elif lmList[8][2] < lmList[14][2] and lmList[12][2] < lmList[14][2] and lmList[4][1] > lmList[8][1] and lengthIndexMiddle > 45 and lmList[16][2] > lmList[14][2]:
                        letter = 'V'
                    elif lmList[8][2] < lmList[18][2] and lmList[12][2] < lmList[18][2] and lmList[16][2] < lmList[18][2] and lengthMiddleRing > 45 and lmList[20][2] > lmList[18][2]:
                        letter = 'W'
                    elif lmList[8][2] < lmList[5][2] and lmList[6][2] < lmList[8][2]:
                        letter = 'X'
                    elif lmList[4][2] < lmList[8][2] and lmList[20][2] < lmList[14][2] and lmList[16][2] > lmList[14][2] and lmList[12][2] > lmList[10][2] and lmList[8][2] > lmList[6][2] and lengthPinkyThumb > 70:
                        letter = 'Y'
                    elif lmList[8][2] < lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[8][1] < lmList[12][1]:
                        letter = 'Z'
                    elif lmList[8][1] > lmList[12][1] and lmList[4][2] < lmList[10][2] and lmList[4][2] < lmList[18][2]:
                        letter = ' '

            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', image)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def update_letter():
    global letter
    global sentence
    threading.Timer(3.0, update_letter).start()
    if letter:
        sentence.append(letter)

@app.route('/get_letter')
def get_letter():
    return jsonify(letter)

@app.route('/get_sentence')
def get_sentence():
    global sentence
    return jsonify(sentence)

@app.route('/')
def index():
    return render_template('index.html', letter=letter)

@app.route('/video_feed')
def video_feed():
    return Response(detect_hands(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    update_letter()
    app.run(debug=True)