import tensorflow as tf
from tf.keras.layers import  Conv2D, MaxPooling2D, Dense, Flatten, Dropout,  BatchNormalization
from tf.keras.models import Model, Sequential
from xgboost import XGBClassifier
from sklearn import metrics

def cnn(input_shape, num_class):
  model = Sequential([
        Conv2D(16, kernel_size = 3, activation = 'relu', padding = 'same', name = 'conv_1', input_shape = input_shape),
        MaxPooling2D(pool_size = 2, padding = 'same', name = 'pool_1'),
        Dropout(0.5, name = 'dropout_1'),
        Conv2D(32, kernel_size = 3, activation = 'relu', padding = 'same', name = 'conv_2'),
        MaxPooling2D(pool_size = 2, padding = 'same', name = 'pool_2'),
        BatchNormalization(input_shape = input_shape, name = 'norm_1'),
        Dropout(0.5, name = 'dropout_2'),
        Flatten(name = 'flatten'),
        Dense(64, activation = 'relu',name='dense_1'),
        Dense(128, activation = 'relu',name='dense_2')
    ])
  model.add(Dense(num_class, activation = 'softmax', name = 'dense_classification'))
  model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  return model

def cnn_intermediate(cnn_model, layer_name):
  intermediate_layer_model = Model(inputs=cnn_model.input,
                                 outputs=cnn_model.get_layer(layer_name).output)
  return intermediate_layer_model

def xgboost_model(x_train, y_train, num_class, cnn_model = None, layer_name = None, intermediate_layer_model=None):
  if intermediate_layer_model is None:
    intermediate_layer_model = cnn_intermediate(cnn_model, layer_name)
  xgbmodel = XGBClassifier(n_estimators = 2, max_depth = 200, objective='multi:softprob',
                      num_class=num_class, tree_method='hist')
  xgb_train = intermediate_layer_model.predict(x_train)
  xgbmodel.train(xgb_train, y_train)
  return xgbmodel


def xgboost_result(x_test, y_test, xgboost, intermediate_layer_model):
  xgb_test = intermediate_layer_model.predict(x_test)
  xgb_result = xgboost.predict(xgb_test)
  conf_mat = metrics.confusion_matrix(xgb_result,y_test)
  return conf_mat
