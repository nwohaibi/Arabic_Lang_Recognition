import cv2
import util
import numpy


THRESHOLD = 0.075


def simpleCompareImages(image1, image2):
    val = numpy.mean(abs(image1 - image2))
    if val <= THRESHOLD:
        return True
    return False


def templateRecognition(line, templ, resultPath, colour):
    height = templ.shape[0]
    width = templ.shape[1]
    newImage = cv2.imread(resultPath, cv2.CV_LOAD_IMAGE_COLOR)

    beginCol = line.shape[1] - 1
    endCol = beginCol - width + 1
    while endCol >= 0:
        image = line[:, range(endCol, beginCol + 1)]
        if simpleCompareImages(image, templ):
            cv2.rectangle(newImage, (endCol, 0), (beginCol, height - 1), colour, thickness=2)
        beginCol -= 1
        endCol -= 1
    cv2.imwrite(resultPath, newImage)


def getRectangleColours():
    colours = [(255, 255, 0, 0), (48, 213, 200, 0), (48, 213, 200, 0), (123, 63, 0, 0),
               (0, 0, 255, 0), (255, 0, 0, 0), (0, 255, 0, 0), (58, 117, 196, 0),
               (215, 125, 49, 0), (255, 71, 202, 0), (139, 0, 255, 0), (139, 0, 255, 0)]
    return colours


def getTemplates():
    templates = []
    for i in range(1, 13):
        path = "../images/train_data/" + str(i) + ".bmp"
        templates.append(util.readGrayIm(path))
    return templates


def getLines():
    lines = []
    for i in range(0, 7):
        lines.append(util.readGrayIm("../images/lines/line_" + str(i) + ".bmp"))
    return lines


def makeOCR():
    lines = getLines()
    templates = getTemplates()
    colours = getRectangleColours()

    for index in range(0, len(lines)):
        for i in range(1, len(templates)):
            resultPath = "../images/results/line_" + str(index) + ".bmp"
            templateRecognition(lines[index], templates[i], resultPath, colours[i])


# makeOCR()