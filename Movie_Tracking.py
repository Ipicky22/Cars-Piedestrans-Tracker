import cv2

video = cv2.VideoCapture('Movie.mp4')

car_tracker_file = "car_detector.xml"
pedestrian_tracker_file = "haarcascade_fullbody.xml"

car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:

    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('Car and Pedestrian Tracking', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()
