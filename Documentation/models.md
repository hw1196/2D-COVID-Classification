# Models
## cnn_intermediate

Extracts an intermediate layer of a CNN model based on the layer's name.

### Parameters

- `cnn_model` (Keras): A CNN model
- `layer_name` (str): The name of the target intermediate layer

### Returns

- `intermediate_layer_model` (Keras): A CNN model ending at the layer of `layer_name`.
## xgboost_model

Creats an XGBoost classifier for multi-class classification using features extracted from the intermediate layer of a CNN_model.

### Parameters

- `x_train` (array-like): Training data 
- `y_train` (array-like): Training data labels
- `num_class` (int): Number of classes
- `cnn_model` (Keras, optional): CNN model for extracting intermediate_layer
- `layer_name` (str, optional): Name of the target layer in the CNN model for feature extraction. 
- `intermediate_layer_model` (Keras, optional): A pre-existing layer of a CNN model

### Returns

- `xgbmodel` (XGBoostClassifier): An XGBoost extension of the CNN model

## xgboost_result

### Description

This function evaluates the performance of the CNN+XGBoost classifier.

### Parameters

- `x_test` (array-like): The test data features
- `y_test` (array-like): The true labels for the test data
- `xgboost` (XGBoostClassifier): The trained XGBoost model being tested
- `intermediate_layer_model` (Keras Model): The intermediate Keras model used to extract features from the CNN

### Returns

- `conf_mat` (array): A confusion matrix of the XGBoost performance
