from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load image from the path passed, check for the file format,
print the arrray shape and return the image array."""
    try:
        image = Image.open(path)
        assert path.endswith(".jpg") \
            or path.endswith(".jpeg"), "file is not in .jpg or .jpeg format"
        arr = np.array(image)
        print(arr.shape)
        return arr
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except FileNotFoundError:
        print("FileNotFoundError: No such file or directory:", path)
