from requests import get
from io import BytesIO
from scipy.misc import imread as scipy_imread
from numpy import ndarray

# For Python 3 compatibility
try:
    input = raw_input
except:
    pass


def imread(image):
    """Reads an image from a url, local filename, PIL image 
    object, `numpy.ndimage object`, or any object type scipy.misc.imread 
    supports directly.  Return the image as a `numpy.ndarray`.

    Args:
        image: A `str` filename or web address, PIL `Image` object, 
        `numpy.ndarray` (will simply return input), or any object type 
        scipy.misc.imread directly supports.

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


def imshow(image):
    """Reads and displays an image from a url, local filename, PIL image 
    object, `numpy.ndimage object`, or any object type scipy.misc.imread 
    supports directly. 
    
    Args:
        image: A `str` filename or web address, ndarray (will simply return 
        input), or any object type scipy.misc.imread supports.

    Returns: 
        A `numpy.ndarray`.
    """
    import matplotlib.pyplot as plt
    plt.ion()
    plt.imshow(imread(image))
    plt.show()


if __name__ == '__main__':
    # web address test
    imshow('http://mathandy.com/escher_sphere.png')
    input('web address test: you should see an image of a human. '
          'Press enter to continue.')

    # local filename test
    imshow('test-pup.jpg')
    input('filename test: you should see an image of a puppy. '
          'Press enter to continue.')

    # numpy array test
    imshow(scipy_imread('test-cats.jpg'))
    input('`numpy.ndarray` test: you should see an of two cats. '
          'Press enter to continue.')

    # PIL test
    try:
        from PIL import Image
        imshow(Image.open("test-pw.jpg"))
        input('PIL object test: you should see an image of a paperweight. '
              'Press enter to continue.')
    except ImportError:
        pass


