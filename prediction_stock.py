import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# Define a function to create the dataset (You can replace this with your actual helper function)
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

# Load the CSV data
df = pd.read_csv('TSLA.csv')
df = df['Open'].values
df = df.reshape(-1, 1)

# Setup datasets
dataset_train = np.array(df[:int(df.shape[0] * 0.8)])
dataset_test = np.array(df[int(df.shape[0] * 0.8):])

# Scale the values
scaler = MinMaxScaler(feature_range=(0, 1))
dataset_train = scaler.fit_transform(dataset_train)
dataset_test = scaler.transform(dataset_test)

# Use the 'create_dataset' function here on the datasets to create train/test datasets
x_train, y_train = create_dataset(dataset_train)
x_test, y_test = create_dataset(dataset_test)

# Reshape the 'x_train' and 'x_test' datasets
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Implement the 'Sequential' model
model = Sequential()
model.add(LSTM(units=4, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=4))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model
model.fit(x_train, y_train, epochs=5, batch_size=16, verbose=0)

# Predict the values for 'x_test'
predictions = model.predict(x_test)

# Print the last column of the 'predictions' array and the model summary
print(predictions[:, -1])
model.summary()
