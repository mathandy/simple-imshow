from simshow import simshow

# For Python 3 compatibility
try:
    input = raw_input
except:
    pass


def test_simshow():
    # web address test
    simshow('http://mathandy.com/escher_sphere.png')
    input('web address test: you should see an image of a human. '
          'Press enter to continue.')

    # local filename test
    simshow('test-pup.jpg')
    input('filename test: you should see an image of a puppy. '
          'Press enter to continue.')

    # numpy array test
    import scipy
    simshow(scipy.misc.imread('test-cats.jpg'))
    input('`numpy.ndarray` test: you should see an of two cats. '
          'Press enter to continue.')

    # PIL test
    try:
        from PIL import Image
        simshow(Image.open("test-pw.jpg"))
        input('PIL object test: you should see an image of a paperweight. '
              'Press enter to continue.')
    except ImportError:
        pass

if __name__ == '__main__':
    test_simshow()