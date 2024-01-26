# import the required modules
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# read image
img = cv2.imread('haha.jpeg')

# call imshow() using plt object
plt.imshow(img[:, :, : : -1])

# display that image
plt.show()

# storing the result
result = DeepFace.analyze(img, actions=['emotion'])

# extract emotion values and percentages
emotions = result['emotion']
max_emotion = max(emotions, key=emotions.get)
max_percentage = emotions[max_emotion]

# print result
print(f"Detected emotion: {max_emotion} with {max_percentage}% confidence")
