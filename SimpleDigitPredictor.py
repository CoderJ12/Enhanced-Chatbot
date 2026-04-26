import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


# Load dataset
data = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = data.load_data()

# Normalize data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Build model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=4)

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)
print("Accuracy:", accuracy)
print("Loss:", loss)

# Predict custom images
for x in range(1, 5):
    img = cv.imread(f'{x}.png', cv.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Image {x}.png not found")
        continue

    img = cv.resize(img, (28, 28))
    img = img / 255.0
    img = np.reshape(img, (1, 28, 28))
    img=1-img

    prediction = model.predict(img)

    print("------")
    print("The predicted output is:", np.argmax(prediction))
    print("------")
    plt.imshow(img[0])
    plt.show()  