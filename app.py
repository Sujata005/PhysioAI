# # app.py
# from flask import Flask, Response, render_template
# import cv2
# import mediapipe as mp
# import numpy as np
# import os
# os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# app = Flask(__name__)

# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
# mp_drawing = mp.solutions.drawing_utils

# def gen_frames():
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
        
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = pose.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         if results.pose_landmarks:
#             mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#         ret, buffer = cv2.imencode('.jpg', image)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video')
# def video():
#     return Response(gen_frames(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == "__main__":
#     print("Starting Flask app...")
#     app.run(debug=True)








#from flask import Flask, Response, render_template
#import cv2
#import mediapipe as mp
#import numpy as np
#import os

#os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

#app = Flask(__name__, template_folder='templates')

#mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#pose = None
#mp_drawing = mp.solutions.drawing_utils

# def gen_frames():
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break

#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = pose.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         if results.pose_landmarks:
#             mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#         ret, buffer = cv2.imencode('.jpg', image)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




#new code
#from flask import Flask, Response, request
#import cv2
#import mediapipe as mp
#mport math

#app = Flask(__name__)
#cap = cv2.VideoCapture(0)

#pose = mp.solutions.pose.Pose()
#mp_drawing = mp.solutions.drawing_utils
#current_mode = 'shoulder'

#def calculate_angle(a, b, c):
    # Angle calculation from 3 points (a, b, c)
 #   ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) -
  #                     math.atan2(a[1]-b[1], a[0]-b[0]))
   ###   ang = 360 - ang
    #return ang

#def gen_frames():
 #   while True:
  #      success, frame = cap.read()
   #     if not success:
    #        break

     #   image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      #  results = pose.process(image_rgb)

       # if results.pose_landmarks:
        #    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

         #   h, w, _ = frame.shape
          #  lm = results.pose_landmarks.landmark
#
 #           if current_mode == "shoulder":
  #              a = [lm[11].x * w, lm[11].y * h]  # shoulder
   #             b = [lm[13].x * w, lm[13].y * h]  # elbow
    #            c = [lm[15].x * w, lm[15].y * h]  # wrist
     #           angle = calculate_angle(a, b, c)
      #          cv2.putText(frame, f"Shoulder Angle: {int(angle)}", (50, 50),
       #                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#
 #           elif current_mode == "leg":
  #              a = [lm[23].x * w, lm[23].y * h]  # hip
   #             b = [lm[25].x * w, lm[25].y * h]  # knee
    #            c = [lm[27].x * w, lm[27].y * h]  # ankle
     #           angle = calculate_angle(a, b, c)
      #          cv2.putText(frame, f"Knee Angle: {int(angle)}", (50, 50),
       #                     cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        #ret, buffer = cv2.imencode('.jpg', frame)
        #frame = buffer.tobytes()
        #yield (b'--frame\r\n'
         #      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#@app.route('/video_feed')
#def video_feed():
 #   return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

#@app.route('/set_mode', methods=['POST'])
#def set_mode():
 #   global current_mode
  #  data = request.get_json()
   # current_mode = data.get('mode', 'shoulder')
    #return {'status': 'ok', 'mode': current_mode}

#if __name__ == '__main__':
 #   app.run(debug=True)
#


import cv2
import mediapipe as mp
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)




mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle
    return angle

def mediapipe_generator(exercise_mode):
    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                if exercise_mode == "arms":
                    # Coordinates for arms
                    shoulderL = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbowL = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    
                    wristL = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    shoulderR = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    elbowR = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    wristR = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                    angleL = calculate_angle(shoulderL, elbowL, wristL)
                    angleR = calculate_angle(shoulderR, elbowR, wristR)

                    colorL = (0, 255, 0) if angleL > 10 else (0, 0, 255)
                    colorR = (0, 255, 0) if angleR > 10 else (0, 0, 255)

                    cv2.putText(image, str(int(angleL)),
                                tuple(np.multiply(elbowL, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorL, 2, cv2.LINE_AA)

                    cv2.putText(image, str(int(angleR)),
                                tuple(np.multiply(elbowR, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorR, 2, cv2.LINE_AA)

                    if angleL > 160:
                        stage = "down"
                    if angleL < 30 and stage == "down":
                        stage = "up"
                        counter += 1

                    landmark_style = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=3)
                    connection_styleL = mp_drawing.DrawingSpec(color=colorL, thickness=4, circle_radius=3)
                    connection_styleR = mp_drawing.DrawingSpec(color=colorR, thickness=4, circle_radius=3)

                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                              landmark_style, connection_styleL if angleL < 100 else connection_styleR)

                elif exercise_mode == "legs":
                    hipL = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    kneeL = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    ankleL = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                    hipR = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    kneeR = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                    ankleR = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                    angleL = calculate_angle(hipL, kneeL, ankleL)
                    angleR = calculate_angle(hipR, kneeR, ankleR)

                    colorL = (0, 255, 0) if angleL > 90 else (0, 0, 255)
                    colorR = (0, 255, 0) if angleR > 90 else (0, 0, 255)

                    cv2.putText(image, str(int(angleL)),
                                tuple(np.multiply(kneeL, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorL, 2, cv2.LINE_AA)

                    cv2.putText(image, str(int(angleR)),
                                tuple(np.multiply(kneeR, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorR, 2, cv2.LINE_AA)

                    if angleL < 120 :
                        stage = "down"
                    if angleL > 90 and stage == "down":
                        stage = "up"
                        counter += 1

                    landmark_style = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=3)
                    connection_styleL = mp_drawing.DrawingSpec(color=colorL, thickness=4, circle_radius=3)
                    connection_styleR = mp_drawing.DrawingSpec(color=colorR, thickness=4, circle_radius=3)

                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                              landmark_style, connection_styleL if angleL < 100 else connection_styleR)

                elif exercise_mode == "shoulders":
                    hipL = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    shoulderL = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbowL = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                    hipR = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    shoulderR = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    elbowR = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

                    angleL = calculate_angle(hipL, shoulderL, elbowL)
                    angleR = calculate_angle(hipR, shoulderR, elbowR)

                    colorL = (0, 255, 0) if angleL < 100 else (0, 0, 255)
                    colorR = (0, 255, 0) if angleR < 100 else (0, 0, 255)

                    cv2.putText(image, str(int(angleL)),
                                tuple(np.multiply(shoulderL, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorL, 2, cv2.LINE_AA)

                    cv2.putText(image, str(int(angleR)),
                                tuple(np.multiply(shoulderR, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorR, 2, cv2.LINE_AA)

                    if angleL < 30 :
                        stage = "down"
                    if angleL > 80 and stage == "down":
                        stage = "up"
                        counter += 1

                    landmark_style = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=3)
                    connection_styleL = mp_drawing.DrawingSpec(color=colorL, thickness=4, circle_radius=3)
                    connection_styleR = mp_drawing.DrawingSpec(color=colorR, thickness=4, circle_radius=3)

                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                              landmark_style, connection_styleL if angleL < 100 else connection_styleR)

                # Overlay counters
                cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)
                cv2.putText(image, 'REPS', (15, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter), (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, 'STAGE', (65, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, stage if stage else '', (60, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            except Exception as e:
                # You can print e or ignore
                pass

            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    cap.release()


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/leg')
def leg_page():
    return render_template('exercise/leg.html')
@app.route('/arm')
def arm_page():
    return render_template('exercise/arm.html')
@app.route('/shoulder')
def shoulder_page():
    return render_template('exercise/shoulder.html')



@app.route('/video_feed/<exercise_mode>')
def video_feed(exercise_mode):
    if exercise_mode not in ['arms', 'legs', 'shoulders']:
        return "Invalid mode", 400
    return Response(mediapipe_generator(exercise_mode),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
