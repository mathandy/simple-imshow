**python-imshow**
#################


**What it does:**

Reads and displays an image from a url, local filename, PIL image object, `numpy.ndimage object`, or any object type scipy.misc.imread supports directly.
Also contains an `imread` function that will return the image as a `numpy.ndarray`.

I've had to look up how to display an image in this context or that too many
times.  This is an attempt to remedy that.


**Request for Community Support:**

I'd love for others to help me make this a more
robust, more convenient tool -- so, as the FAA likes to say, "If you see something, say something." Or at least feel free to.


**TODO:**

* Add simple tool to take a list of images and display a random sample (or all) as a grid of thumbnails.

* Add support for plots.


**Some thoughts on guidelines for this project:**

* `imread` should be fast.

* I'd like to keep required dependencies limited to common ones available through pip (e.g. no requirement for opencv)

* It'd be nice if `imshow` could refresh quickly enough support video feeds.  In my experience matplotlib figures will not though (I do not know matplotlib well though).