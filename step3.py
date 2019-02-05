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
	#STEP ONE
	#importing the Image module of PIL
	from PIL import Image

	#creating Image object
	#opening the image for reading mode
	image = Image.open('grace-hopper.png', 'r')
	
	#STEP TWO
	#create a list that is filled with the values stored in the pixels in the image
	pixel_values =  list(image.getdata())
	
	#print out list (error/format checking)
	#can comment the for loop out in order to de-clutter
	for x in range(len(pixel_values)):
		print pixel_values[x],	

	#STEP 3

	#sum variable adds up the RGB values of each pixel
	sum = 0	

	#comparison variable against sum
	smallest_and_darkest = 0;

	#list of the two darkest pixels
	darkest_pixels = []

	#for loop through the three dimensions already stored for each pixel
	#compare values using the sum variable
	for i in range(len(pixel_values)):
		for j in range(len(pixel_values)):
			for k in range(len(pixel_values)):
				#sum is equal to the three values for that pixel added together
				sum = pixel_values[i][j][k]

if __name__ == '__main__':
	main ()
