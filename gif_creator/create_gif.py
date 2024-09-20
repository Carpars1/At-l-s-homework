import imageio.v3 as iio

filenames = ['teampic1.png', 'teampic2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)