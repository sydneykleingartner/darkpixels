#imports
from PIL import Image
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib import pyplot as mp


def main ():

	#import image & print pixel values
	pixel_values = misc.imread('grace-hopper.png')
    	print(pixel_values)

        #print dimensions of the image
	print(pixel_values.shape)

	#comparison variable against sum
	#assign to the first pixel's sum
        #use long in case that the sum is greater than 256 (max for an integer)
	smallest_and_darkest = long(pixel_values[0][0][0]) + long(pixel_values[0][0][1])+ long(pixel_values[0][0][2])

	#store placement (rows & columns) within image of the darkest pixel
	min_i = 0
	min_j = 0

        #for each row in the image
	for i in range(pixel_values.shape[0]):
                #for each column in the image
		for j in range(pixel_values.shape[1]):
			#sum is equal to the three values for that pixel added together
                        #long in case the sum is greater than 256
			sumup = long(pixel_values[i][j][0]) + long(pixel_values[i][j][1]) + long(pixel_values[i][j][2])

			#if this sum is smaller than the current smallest (meaning darkest pixel)
			if sumup < smallest_and_darkest:
				#reassign smallest_and_darkest to the sum at that position
				smallest_and_darkest = sumup
				min_i = i
				min_j = j

        #print contents of darkest pixel
	print(pixel_values[min_i][min_j])

        #color a red X around the darkest pixel
	colorX(pixel_values, min_i, min_j)

        #print the new pixel values
	print(pixel_values)

	#reassign the pixels to the image
	#show and save the altered image
	plt.imshow(pixel_values)
	plt.imsave('altered3.png', pixel_values)
	plt.show()

#color a red X around the darkest pixel
def colorX (pixel_values, min_i, min_j):
        #store the dimensions of the image
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
