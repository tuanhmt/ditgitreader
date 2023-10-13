import mnist
from PIL import Image
img = mnist.test_images()[1]

Image.fromarray(img).save('test1.png')