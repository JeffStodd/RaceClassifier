import tensorflow as tf

def generateModel():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(200,200,3)))
    
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=64, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(tf.keras.layers.Conv2D(kernel_size=(3,3), filters=128, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=4, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(3,3), filters=16, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=4, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=8, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(3,3), filters=32, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=8, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=16, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(3,3), filters=64, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=16, activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=2))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=32, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(3,3), filters=128, activation='relu'))
    model.add(tf.keras.layers.Conv2D(kernel_size=(1,1), filters=32, activation='relu'))
    
    #model.add(tf.keras.layers.GlobalMaxPooling2D())
    
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units = 5, activation='softmax'))

    #training settings
    adam = tf.keras.optimizers.Adam(
        learning_rate=0.0001,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-07,
        amsgrad=False,
        name='Adam'
    )
    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer=adam, metrics=[tf.keras.metrics.Precision(), tf.keras.metrics.FalsePositives(), tf.keras.metrics.FalseNegatives()])
    return model

def main():
    print("Generating")
    model = generateModel()
    model.save("Classifier.h5")
    print("Saved")
    print(model.summary())

if __name__ == "__main__":
    main()
