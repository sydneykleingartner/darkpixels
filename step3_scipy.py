from PIL import Image
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib import pyplot as mp
#step 3

#for loop through the list
#goal: to find the two darkest pixels

#how i might go about this
	#for loop through the three dimensions inside the pre-existing list
	#store the darkest pixels in an three-dimensional array
	#it would be easier to just do one
		#how might i go about choosing the two darkest??
		#think more about this
	#remember: the pixels cannot be right next to each other
		#must be distinct "eyes"
	#for each of the darkest pixels (for loop)
		#replace the color of that specific pixel with red
		#place the X's around each
			#in the three dimensional array that the pixels are stored in, place red at the pixels around the "darkest" ones to form an X

def main ():

	
	pixel_values = misc.imread('grace-hopper.png')
	# pixel_values = misc.imread('color_teeny.png', 'r')
	print(pixel_values)

	#STEP TWO
	#create a list that is filled with the values stored in the pixels in the image
	#print out list (error/format checking)
	#can comment the for loop out in order to de-clutter
	print(pixel_values.shape)
	# for x in range(len(pixel_values)):
	# 	print str(pixel_values[x][0]) + " "	+  str(pixel_values[x][1]) + " " + str(pixel_values[x][2])

	# sumup = 0	

	#comparison variable against sum
	#assign to the first pixel's sum
	smallest_and_darkest = long(pixel_values[0][0][0]) + long(pixel_values[0][0][1])+ long(pixel_values[0][0][2])

	#list of the two darkest pixels
	darkest_pixels = []
	#assign darkest pixel (the first position in this list) to the first pixel in the image
	# darkest_pixels[0] = pixel_values[0][0]	
	min_i = 0
	min_j = 0

	for i in range(pixel_values.shape[0]):
		for j in range(pixel_values.shape[1]):
			#sum is equal to the three values for that pixel added together
			sumup = long(pixel_values[i][j][0]) + long(pixel_values[i][j][1]) + long(pixel_values[i][j][2])
			#if this sum is smaller than the current smallest (meaning darkest pixel)

			if sumup < smallest_and_darkest:
				#reassign smallest_and_darkest to the sum at that position
				smallest_and_darkest = sumup
				min_i = i
				min_j = j

	print(pixel_values[min_i][min_j])

	colorX(pixel_values, min_i, min_j)

	print(pixel_values)

	#reassign the pixels to the image
	
	#show new image
	plt.imshow(pixel_values)
	plt.imsave('altered3.png', pixel_values)
	plt.show()

	#pylab.savefig('face.png')
	#show()

	#save new image
	#mp.savefig('face.png')
	#mp.savefig('face.png', bbox_inches='tight')
	#mp.show('face.png')

	# image = Image.open('face.png').show()

def colorX (pixel_values, min_i, min_j):
	shape = pixel_values.shape;
	#color darkest pixel itself
	pixel_values[min_i][min_j][0] = 255;
	pixel_values[min_i][min_j][1] = 0;
	pixel_values[min_i][min_j][2] = 0;

	#edge cases
	#if top row
	if (min_i == 0):
		#if top left corner
		if (min_j == 0):
			#only color bottom right
			pixel_values[min_i+1][min_j+1][0] = 255;
			pixel_values[min_i+1][min_j+1][1] = 0;
			pixel_values[min_i+1][min_j+1][2] = 0;
		#if top right corner
		elif (min_j == shape[1] -1):
			#only color bottom left
			pixel_values[min_i+1][min_j-1][0] = 255;
			pixel_values[min_i+1][min_j-1][1] = 0;
			pixel_values[min_i+1][min_j-1][2] = 0;
		#in the top row, but not a corner
		else:
			#color bottom right and bottom left
			#bottom left
			pixel_values[min_i+1][min_j-1][0] = 255;
			pixel_values[min_i+1][min_j-1][1] = 0;
			pixel_values[min_i+1][min_j-1][2] = 0;
			#bottom right
			pixel_values[min_i+1][min_j+1][0] = 255;
			pixel_values[min_i+1][min_j+1][1] = 0;
			pixel_values[min_i+1][min_j+1][2] = 0;

	#if bottom row
	elif (min_i == shape[0] -1):
		#if bottom left corner
		if (min_j == 0):
			#only color top right
			pixel_values[min_i-1][min_j+1][0] = 255;
			pixel_values[min_i-1][min_j+1][1] = 0;
			pixel_values[min_i-1][min_j+1][2] = 0;
		#if bottom right corner
		elif (min_j == shape[1] -1):
			#only color top left
			pixel_values[min_i-1][min_j-1][0] = 255;
			pixel_values[min_i-1][min_j-1][1] = 0;
			pixel_values[min_i-1][min_j-1][2] = 0;
		#in bottom row, but not a corner
		else:
			#color top right and top left
			#top left
			pixel_values[min_i-1][min_j-1][0] = 255;
			pixel_values[min_i-1][min_j-1][1] = 0;
			pixel_values[min_i-1][min_j-1][2] = 0;
			#top right
			pixel_values[min_i-1][min_j+1][0] = 255;
			pixel_values[min_i-1][min_j+1][1] = 0;
			pixel_values[min_i-1][min_j+1][2] = 0;

	#if furthest left column
	elif (min_j == 0):
		#only color right top & bottom
		#right top
		pixel_values[min_i-1][min_j+1][0] = 255;
		pixel_values[min_i-1][min_j+1][1] = 0;
		pixel_values[min_i-1][min_j+1][2] = 0;
		#right bottom
		pixel_values[min_i+1][min_j+1][0] = 255;
		pixel_values[min_i+1][min_j+1][1] = 0;
		pixel_values[min_i+1][min_j+1][2] = 0;

	#if furthest right column
	elif (min_j == shape[1] - 1):
		#only color left top & bottom
		#left top
		pixel_values[min_i-1][min_j-1][0] = 255;
		pixel_values[min_i-1][min_j-1][1] = 0;
		pixel_values[min_i-1][min_j-1][2] = 0;
		#left bottom
		pixel_values[min_i+1][min_j-1][0] = 255;
		pixel_values[min_i+1][min_j-1][1] = 0;
		pixel_values[min_i+1][min_j-1][2] = 0;

	#darkest pixel is somewhere in the middle of the image
	else:
		#color all 4

		#top left
		pixel_values[min_i-1][min_j-1][0] = 255;
		pixel_values[min_i-1][min_j-1][1] = 0;
		pixel_values[min_i-1][min_j-1][2] = 0;

		#top right
		pixel_values[min_i-1][min_j+1][0] = 255;
		pixel_values[min_i-1][min_j+1][1] = 0;
		pixel_values[min_i-1][min_j+1][2] = 0;

		#bottom left
		pixel_values[min_i+1][min_j-1][0] = 255;
		pixel_values[min_i+1][min_j-1][1] = 0;
		pixel_values[min_i+1][min_j-1][2] = 0;

		#bottom right
		pixel_values[min_i+1][min_j+1][0] = 255;
		pixel_values[min_i+1][min_j+1][1] = 0;
		pixel_values[min_i+1][min_j+1][2] = 0;

		# return pixel_values
				
		
if __name__ == '__main__':
	main ()
