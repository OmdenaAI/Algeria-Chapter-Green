
🌾Wheat Detection🌾

Problem Statement:

Detection of wheat heads is an important task allowing to estimate pertinent traits including head population density and head characteristics such as sanitary state, size, maturity stage and the presence of awns. Several studies developed methods for wheat head detection from high-resolution RGB imagery. They are based on computer vision and machine learning and are generally calibrated and validated on limited datasets. However, variability in observational conditions, genotypic differences, development stages, head orientation represents a challenge in computer vision. Further, possible blurring due to motion or wind and overlap between heads for dense populations make this task even more complex.

Dataset Description:

More details on the data acquisition and processes are available at https://arxiv.org/abs/2005.02162

What should we expect the data format to be?

The data is images of wheat fields, with bounding boxes for each identified wheat head. Not all images include wheat heads / bounding boxes. The images were recorded in many locations around the world.

The CSV data is simple - the image ID matches up with the filename of a given image, and the width and height of the image are included, along with a bounding box (see below). There is a row in train.csv for each bounding box. Not all images have bounding boxes.

What am I predicting?

We are attempting to predict bounding boxes around each wheat head in images that have them. If there are no wheat heads, we must predict no bounding boxes.

In this Notebook we have performed EDA on our dataset and done visualization of wheat heads in images through bounding boxes with the help of Computer Vision.





Contributors: 

Searching for Dataset - Arokamal Sethy & Guindo Sadio

Research on related works - Moumni samir & Hazem

Searching for methods and algorithms - Nirmit Shah & Abhijeet Pundkar

Implementation of EDA - Arokamal Sethy, Nirmit Shah & Abhijeet Pundkar

Presentation & Documentation - Arokamal Sethy, Moumni Samir , Nirmit
Shah & Abhijeet Pundkar
