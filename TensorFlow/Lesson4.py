#Data from: 
#https://storage.googleapis.com/learning-datasets/rps.zip \ 
#https://storage.googleapis.com/learning-datasets/rps-test-set.zip \
import os
import zipfile

path = '../../temp/'

local_zip = path+'rps.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall(path)
zip_ref.close()

local_zip = path+'rps-test-set.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall(path)
zip_ref.close()

rock_dir = os.path.join(path+'rps/rock')
paper_dir = os.path.join(path+'rps/paper')
scissors_dir = os.path.join(path+'rps/scissors')

#Check how many images
if(False):
    print('total training rock images:', len(os.listdir(rock_dir)))
    print('total training paper images:', len(os.listdir(paper_dir)))
    print('total training scissors images:', len(os.listdir(scissors_dir)))

#Print a few radom ones to check naming
if(False):
    rock_files = os.listdir(rock_dir)
    print(rock_files[:10])

    paper_files = os.listdir(paper_dir)
    print(paper_files[:10])

    scissors_files = os.listdir(scissors_dir)
    print(scissors_files[:10])

#%matplotlib inline
#look at the figures
if(False):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    pic_index = 2

    next_rock = [os.path.join(rock_dir, fname) 
                    for fname in rock_files[pic_index-2:pic_index]]
    next_paper = [os.path.join(paper_dir, fname) 
                    for fname in paper_files[pic_index-2:pic_index]]
    next_scissors = [os.path.join(scissors_dir, fname) 
                    for fname in scissors_files[pic_index-2:pic_index]]

    for i, img_path in enumerate(next_rock+next_paper+next_scissors):
      #print(img_path)
      img = mpimg.imread(img_path)
      plt.imshow(img)
      plt.axis('Off')
      plt.show()

#Train the neural network
if(False):
    import tensorflow as tf
    import tensorflow.keras.preprocessing
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.preprocessing.image import ImageDataGenerator

    TRAINING_DIR = path+"rps/"
    training_datagen = ImageDataGenerator(
        rescale = 1./255,
	    rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    VALIDATION_DIR = path+"rps-test-set/"
    validation_datagen = ImageDataGenerator(rescale = 1./255)

    train_generator = training_datagen.flow_from_directory(
    	TRAINING_DIR,
    	target_size=(150,150),
    	class_mode='categorical',
      batch_size=126
    )

    validation_generator = validation_datagen.flow_from_directory(
    	VALIDATION_DIR,
    	target_size=(150,150),
    	class_mode='categorical',
      batch_size=126
    )

    model = tf.keras.models.Sequential([
        # Note the input shape is the desired size of the image 150x150 with 3 bytes color
        # This is the first convolution
        tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The second convolution
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # The third convolution
        tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # The fourth convolution
        tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # Flatten the results to feed into a DNN
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
        # 512 neuron hidden layer
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])


    model.summary()

    model.compile(loss = 'categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    history = model.fit(train_generator, epochs=25, steps_per_epoch=20, validation_data = validation_generator, verbose = 1, validation_steps=3)

    model.save("rps.h5")

    #Check the result of the training

    import matplotlib.pyplot as plt
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.plot(epochs, acc, 'r', label='Training accuracy')
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend(loc=0)
    plt.figure()


    plt.show()

if(True):
    import tensorflow as tf
    from keras.models import load_model
    import numpy as np
    #from google.colab import files
    from keras.preprocessing import image
    model = load_model('rps.h5')
    #uploaded = files.upload()

    def luokka(prediction):
        pap = prediction[0]
        kiv = prediction[1]
        sak = prediction[2]
        mika = max(pap,kiv,sak)
        if(prediction[0] != 0):
            return "Paper"
        if(prediction[1] != 0):
            return "Rock"
        else:
            return "Scissors"

    for fn in range(10):
        paper = 'paper/testpaper01-0'+str(fn)+'.png'
        image = tf.keras.utils.load_img(path+'rps-test-set/'+paper,target_size=(150,150))
        input_arr = tf.keras.utils.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch.
        predictions = model.predict(input_arr)
        print("=======================================================")
        print(paper+" was found to be "+luokka(predictions[0]))
        print(predictions[0])

    for fn in range(10):
        rock = 'rock/testrock01-0'+str(fn)+'.png'
        image = tf.keras.utils.load_img(path+'rps-test-set/'+rock,target_size=(150,150))
        input_arr = tf.keras.utils.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch.
        predictions = model.predict(input_arr)
        print("=======================================================")
        print(rock+" was found to be "+luokka(predictions[0]))
        print(predictions[0])

    for fn in range(10):
        scissors = 'scissors/testscissors01-0'+str(fn)+'.png'
        image = tf.keras.utils.load_img(path+'rps-test-set/'+scissors,target_size=(150,150))
        input_arr = tf.keras.utils.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch.
        predictions = model.predict(input_arr)
        print("=======================================================")
        print(scissors+" was found to be "+luokka(predictions[0]))
        print(predictions[0])

    #
    #  # predicting images
    #  path = fn
    #  img = image.load_img(path, target_size=(150, 150))
    #  x = image.img_to_array(img)
    #  x = np.expand_dims(x, axis=0)
    #
    #  images = np.vstack([x])
    #  classes = model.predict(images, batch_size=10)
    #  print(fn)
    #  print(classes)