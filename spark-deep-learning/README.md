This is a demo to run Spark deep learning pipeline to train a multi-class classification problem, and then build a toy recommendation system based on image data only.

# Dataset

We use [Stanford Cars Dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html). The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

# System and Library

Apache Spark 2.3
Apache Zeppelin 0.8.0
[Spark deep learning pipeline 1.0.0](https://github.com/databricks/spark-deep-learning/tree/v1.0.0)

# Preprocessing

* Spark deep learning pipeline 1.0.0 can't accept the original format of image data, so you need to convert the image data to png format.

* Use this [script](preprocessing.py) to extract image id to label map.

# Model training, evaluation and prediction

Load this [script](deep-learning-demo.json) into Zeppelin and run step by step.
