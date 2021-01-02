import cv2

img_file = "Car Image2.jpg"

classifier_file = "car_detector.xml"

img = cv2.imread(img_file)

car_tracker = cv2.CascadeClassifier(classifier_file)

cars = car_tracker.detectMultiScale(img)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Car Tracking', img)

cv2.waitKey()

print("Code Completed")
