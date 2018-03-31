########################################################################
# Digits Recognition
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/digits.png')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Split th image to 5000 cells, each 20x20 size
# cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# # Make it into array
# x = np.array(cells)

# # Prepare train data and test data
# train = x[:, :50].reshape(-1, 400).astype(np.float32)
# test = x[:, 50:100].reshape(-1, 400).astype(np.float32)

# # Create labels for train and test data
# k = np.arange(10)
# train_labels = np.repeat(k, 250)[:, np.newaxis]
# test_labels = train_labels.copy()

# # Initiate kNN, train the data and test data
# knn = cv.ml.KNearest_create()
# knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
# ret, result, neighbours, dist = knn.findNearest(test, k=5)

# # Compare te result with test_labels
# matches = result == test_labels
# correct = np.count_nonzero(matches)
# accuracy = correct * 100.0 / result.size
# print("classify precision:")
# print(accuracy)

########################################################################
# English Alphabets Recognition
########################################################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Load data
data = np.loadtxt('../../img/letter-recognition.data', dtype='float32',
                  delimiter=',', converters={0: lambda ch: ord(ch) - ord('A')})

# Split data to train and test parts
train, test = np.vsplit(data, 2)

# Split data to feature and responses
responses, trainData = np.hsplit(train, [1])
labels, testData = np.hsplit(test, [1])

# Initiate kNN and classify
knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

# Measure accuracy
correct = np.count_nonzero(result == labels)
accuracy = correct * 100.0 / 10000
print("classify precision:")
print(accuracy)
