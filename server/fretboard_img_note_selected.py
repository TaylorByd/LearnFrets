import cv2 as cv
import threading
import time

dot_coordinates = [[1]*25 for i in range(6)]
x_coordinates = [26, 78, 175, 269, 361, 450, 537, 622, 704, 786, 864, 942, 1016, 1090, 1160, 1228,
                 1294, 1358, 1420, 1481, 1541, 1598, 1654, 1707, 1760]
y_coordinates = [188, 154, 119, 84, 51, 16]

for i in range(6):
    y_dot = y_coordinates[i]
    for j in range(25):
        dot_coordinates[i][j] = [x_coordinates[j], y_dot]

stop_incorrect_flag = threading.Event()

def create_dot(red, green, blue, dot_coordinates):
    img = cv.imread("..\\client\\src\\images\\GuitarFretboard.png")
    img = cv.circle(img, dot_coordinates, 10, (blue, green, red), -1, lineType=cv.LINE_AA)
    cv.imwrite("..\\client\\src\\images\\modified_guitar_fretboard.png", img)

def incorrect_note(dot_coordinates):
    for _ in range(3):
        if stop_incorrect_flag.is_set():  # Check if correct_note was activated
            print("Stopping incorrect note because correct note was activated.")
            return
        create_dot(255, 0, 0, dot_coordinates)
        time.sleep(0.5)
        create_dot(255, 0, 255, dot_coordinates)
        time.sleep(0.5)

def correct_note(dot_coordinates):
    # Set the stop flag to stop the incorrect_note thread
    stop_incorrect_flag.set()
    create_dot(0, 180, 0, dot_coordinates)
    time.sleep(1)
    create_dot(255, 0, 255, dot_coordinates)
    # Reset the flag for future use
    stop_incorrect_flag.clear()