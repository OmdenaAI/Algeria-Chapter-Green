Dataset Description:🌾

More details on the data acquisition and processes are available at https://arxiv.org/abs/2005.02162

What should we expect the data format to be?🧐

The data is images of wheat fields, with bounding boxes for each identified wheat head. Not all images include wheat heads / bounding boxes. The images were recorded in many locations around the world.🌾

The CSV data is simple - the image ID matches up with the filename of a given image, and the width and height of the image are included, along with a bounding box (see below). There is a row in train.csv for each bounding box. Not all images have bounding boxes.🟥⬜
