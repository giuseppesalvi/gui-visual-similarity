import cv2


def resize_image(target_image_path, reference_image_path):
    """
    Resizes the target image to match the size of a reference image and saves the resized target image in its original path with _resized suffix.

    Parameters:
    target_image_path (str): The path to the target image that needs to be resized

    reference_image_path (str): The path to the reference image whose size will be used to resize the target image
    """

    # Load the images
    target_image = cv2.imread(target_image_path)
    reference_image = cv2.imread(reference_image_path)

    # Check if the images are loaded properly
    if target_image is None:
        print("Could not load image: ", target_image_path)
        return
    if reference_image is None:
        print("Could not load image: ", reference_image_path)
        return

    # Resize target_image to match reference_image size
    target_image_resized = cv2.resize(
        target_image, (reference_image.shape[1], reference_image.shape[0]))

    # Save the resized image
    target_image_path_splitted = target_image_path.split(".")
    resize_image_path = target_image_path_splitted[0] + \
        "_resized." + target_image_path_splitted[1]
    cv2.imwrite(resize_image_path, target_image_resized)


if __name__ == "__main__":
    reference_image_path = "data/img1_original.png"
    target_image_path = "data/img1_modified.png"
    resize_image(target_image_path, reference_image_path)
