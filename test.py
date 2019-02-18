from PIL import Image
from scipy import ndimage
from scipy import misc
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
	image = Image.open('color_teeny_2.png', 'r')
	
	
	#STEP TWO
	#create a list that is filled with the values stored in the pixels in the image
	pixel_values =  list(image.getdata())
	
	#print out list (error/format checking)
	#can comment the for loop out in order to de-clutter
	print(pixel_values)
	# for x in range(len(pixel_values)):
	# 	print str(pixel_values[x][0]) + " "	+  str(pixel_values[x][1]) + " " + str(pixel_values[x][2])

	# sumup = 0	

	#comparison variable against sum
	#assign to the first pixel's sum
	smallest_and_darkest = pixel_values[0][0] + pixel_values[0][1]+ pixel_values[0][2]

	#list of the two darkest pixels
	darkest_pixels = []
	#assign darkest pixel (the first position in this list) to the first pixel in the image
	# darkest_pixels[0] = pixel_values[0][0]	
	min_i = 0

	for i in range(len(pixel_values)):
			#sum is equal to the three values for that pixel added together
			sumup = pixel_values[i][0] + pixel_values[i][1] + pixel_values[i][2]
			#if this sum is smaller than the current smallest (meaning darkest pixel)

			if sumup < smallest_and_darkest:
				#reassign smallest_and_darkest to the sum at that position
				smallest_and_darkest = sumup
				min_i = i

	print(pixel_values[min_i])
	#once we have found the darkest pixel and stored it in the darkest_pixels
	#we want to go find the second darkest
	#for m in range(len(pixel_values)):
		#for n in range(len(pixel_values)): 
				
		
if __name__ == '__main__':
	main ()
