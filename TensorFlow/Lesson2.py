#Learning to recognize images
import tensorflow as tf
from tensorflow import keras

#Printing the Tensorflow version
print("Tensorflow version = ",tf.__version__)

#Labels work as
#0	T-shirt/top
#1	Trouser
#2	Pullover
#3	Dress
#4	Coat
#5	Sandal
#6	Shirt
#7	Sneaker
#8	Bag
#9	Ankle boot

#Network with 128 neurons
if(False):
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    #Take a look at the data
    if(False):
        import matplotlib.pyplot as plt
        plt.imshow(train_images[0])
        print(train_labels[0])
        print(train_images[0])

    #Normalize the data
    train_images  = train_images / 255.0
    test_images = test_images / 255.0

    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                        tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer = tf.keras.optimizers.Adam(),
                  loss = 'sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    #The probability that this item is each of the 10 classes
    print(classifications[0])
    #What the actual label ens up being
    print(test_labels[0])

#Same as above but now 1024 neurons
if(False):
    mnist = tf.keras.datasets.fashion_mnist

    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

    training_images = training_images/255.0
    test_images = test_images/255.0

    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(1024, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer = 'adam',
                  loss = 'sparse_categorical_crossentropy')

    model.fit(training_images, training_labels, epochs=5)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    print(classifications[0])
    print(test_labels[0])

#What is the error message if we don't flatten the data
if(False):
    mnist = tf.keras.datasets.fashion_mnist

    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

    training_images = training_images/255.0
    test_images = test_images/255.0

    # This version has the 'flatten' removed. Should rather start with:
    #model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
    model = tf.keras.models.Sequential([tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])


    model.compile(optimizer = 'adam',
                  loss = 'sparse_categorical_crossentropy')

    model.fit(training_images, training_labels, epochs=5)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    print(classifications[0])
    print(test_labels[0])    

#What is the error message if we don't have the same number of neurons as there are classes
if(False):
    mnist = tf.keras.datasets.fashion_mnist

    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

    training_images = training_images/255.0
    test_images = test_images/255.0

    # Replace the above model definiton with this one to see the network with 5 output layers
    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(5, activation=tf.nn.softmax)])

    model.compile(optimizer = 'adam',
                  loss = 'sparse_categorical_crossentropy')

    model.fit(training_images, training_labels, epochs=5)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    print(classifications[0])
    print(test_labels[0])

#Adding an extra layer doesn't do much
if(False):
    mnist = tf.keras.datasets.fashion_mnist

    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

    training_images = training_images/255.0
    test_images = test_images/255.0

    #model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
    #                                    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    #                                    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    #                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])


    model.compile(optimizer = 'adam',
                  loss = 'sparse_categorical_crossentropy')

    model.fit(training_images, training_labels, epochs=5)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    print(classifications[0])
    print(test_labels[0])

#Example of adding epochs (marginal gains)
if(False):
    mnist = tf.keras.datasets.fashion_mnist

    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

    training_images = training_images/255.0
    test_images = test_images/255.0

    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer = 'adam',
                  loss = 'sparse_categorical_crossentropy')

    model.fit(training_images, training_labels, epochs=30)

    model.evaluate(test_images, test_labels)

    classifications = model.predict(test_images)

    print(classifications[34])
    print(test_labels[34])

#If we don't normalize the data (loss is bigger)
if(False):
    mnist = tf.keras.datasets.fashion_mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(512, activation=tf.nn.relu),
      tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
    model.fit(training_images, training_labels, epochs=5)
    model.evaluate(test_images, test_labels)
    classifications = model.predict(test_images)
    print(classifications[0])
    print(test_labels[0])

#Stop at desired accuracy?
if(False):
    class myCallback(tf.keras.callbacks.Callback):
      def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.85):
          print("\nReached 85% accuracy so cancelling training!")
          self.model.stop_training = True

    callbacks = myCallback()
    mnist = tf.keras.datasets.fashion_mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
    training_images=training_images/255.0
    test_images=test_images/255.0
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(512, activation=tf.nn.relu),
      tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])

#What is the class of my own boot?
if(False):
    import numpy as np

    mnist = tf.keras.datasets.fashion_mnist
    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()
    training_images = training_images/255.0
    test_images = test_images/255.0
    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(training_images, training_labels, epochs=5)
    model.evaluate(test_images, test_labels)

    myimage = tf.keras.utils.load_img('./myBoots/Boots/myBoot1.png',color_mode="grayscale",target_size=None,interpolation="nearest",keep_aspect_ratio=False,)
    input_arr = tf.keras.utils.img_to_array(myimage)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    #print(np.shape(input_arr))
    
    predictions = model.predict(input_arr)
    print(predictions[0]) #My boot is a sandal or a t-shirt?

#Run the model once and save it to mnist_model_128nodes_5epochs
if(False):
    mnist = tf.keras.datasets.fashion_mnist
    (training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()
    training_images = training_images/255.0
    test_images = test_images/255.0
    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(training_images, training_labels, epochs=5)
    model.save('./mnist_model_128nodes_5epochs')

#Multiple boots at the same time?
if(True):
    import numpy as np

    myimage = tf.keras.utils.load_img("./myBoots/Boots/myBoot2.png",color_mode="grayscale",target_size=None,interpolation="nearest",keep_aspect_ratio=False,)

    model = keras.models.load_model('./mnist_model_128nodes_5epochs')

    input_arr = tf.keras.utils.img_to_array(myimage)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    print(predictions[0]) #My sandal is a bag

