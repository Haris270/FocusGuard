
from fiftyone.utils.openimages import download_open_images_split



download_open_images_split(
    dataset_dir = "/Users/harisz/Documents/ten-oid", #directory to download the dataset to
    split = "train",                # the category of downloaded class
    version = "v7",                 # Open Images version
    label_types = ["detections"],   # the label category to download
    classes = ["Mobile phone"],     # the list of classes to download
    max_samples = 10000,             # number of images to download
    shuffle = True
)



