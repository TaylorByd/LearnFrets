import cv2 as cv

dot_coordinates = [[1]*25 for i in range(6)]
x_coordinates = [26, 78, 175, 269, 361, 450, 537, 622, 704, 786, 864, 942, 1016, 1090, 1160, 1228,
                 1294, 1358, 1420, 1481, 1541, 1598, 1654, 1707, 1760]
y_coordinates = [188, 154, 119, 84, 51, 16]

for i in range(6):
    y_dot = y_coordinates[i]
    for j in range(25):
        dot_coordinates[i][j] = [x_coordinates[j], y_dot]

def place_dot_img(dot_coordinates):
    img = cv.imread("..\\client\\src\\images\GuitarFretboard.png")
    img = cv.circle(img, dot_coordinates, 10, (0, 0, 255), -1, lineType=cv.LINE_AA)
    cv.imwrite("..\\client\\src\\images\\modified_guitar_fretboard.png", img)