Leafsnap Dataset Readme
-----------------------

Leafsnap (http://leafsnap.com) is an electronic field guide for identifying tree
species from photos of their leaves. It was jointly created by computer
scientists from Columbia University and the University of Maryland, and
botanists from the Smithsonian Institution in Washington, DC.

To promote further research in leaf recognition, we are releasing the leafsnap
dataset, which consists of the following pieces:

- Images of leaves taken from two different sources:
  * "Lab" images, consisting of high-quality images taken of pressed leaves,
    from the Smithsonian collection. These images appear in controlled backlit
    and front-lit versions, with several samples per species.
  * "Field" images, consisting of "typical" images taken by mobile devices
    (iPhones mostly) in outdoor environments. These images contain varying
    amounts of blur, noise, illumination patterns, shadows, etc.

- Segmented versions of all images, using the Leafsnap segmentation algorithm

The dataset covers all 185 tree species from the Northeastern United States.

If you use this dataset, please cite the following paper:

Neeraj Kumar, Peter N. Belhumeur, Arijit Biswas, David W. Jacobs, W. John Kress, Ida Lopez, João V. B. Soares,
"Leafsnap: A Computer Vision System for Automatic Plant Species Identification,"
Proceedings of the 12th European Conference on Computer Vision (ECCV),
October 2012.


The included leafsnap-dataset-images.txt file contains a listing of all the images, in tab-separated format.
The first line is the header row, which describes each column.

file_id    image_path   segmented_path    species    source

Each line lists information about a single image. There are 5 fields, which are separated by tabs:

- A unique numerical id for each image. These are not guaranteed to be
  consecutive or in order. They will not change over future versions of the
  dataset.
- The path of the original image.
- The path of the segmented version of the image.
- The scientific name of the species of the image. Note that these can have spaces and hyphens, and are in mixed case.
- The source of the image. This is either 'lab' or 'field'
