from requests import get
from io import BytesIO
from scipy.misc import imread as scipy_imread
from numpy import ndarray


def simread(image):
    """Reads an image from a url, local filename, PIL image
    object, `numpy.ndimage object`, or any object type scipy.misc.simread
    supports directly.  Return the image as a `numpy.ndarray`.

    Args:
        image: A `str` filename or web address, PIL `Image` object,
        `numpy.ndarray` (will simply return input), or any object type
        scipy.misc.simread directly supports.

    Returns:
        A `numpy.ndarray`.
    """
    if isinstance(image, str) and len(image) > 4 and image[:5] == 'http:':
        return scipy_imread(BytesIO(get(image).content))
    elif isinstance(image, ndarray):
        return image
    else:
        try:  # maybe scipy.misc.fromimage would handle this already
            from PIL.Image import isImageType
            from scipy.misc import fromimage
            if isImageType(image):
                return fromimage(image)
        except ImportError:
            pass

        return scipy_imread(image)


def simshow(image):
    """Reads and displays an image from a url, local filename, PIL image
    object, `numpy.ndimage object`, or any object type scipy.misc.simread
    supports directly.

    Args:
        image: A `str` filename or web address, ndarray (will simply return
        input), or any object type scipy.misc.simread supports.

    Returns:
        A `numpy.ndarray`.
    """
    import matplotlib.pyplot as plt
    plt.ion()
    plt.imshow(simread(image))
    plt.show()
