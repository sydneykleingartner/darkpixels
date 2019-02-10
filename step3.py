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

	#STEP THREE
	#sum variable adds up the RGB values of each pixel
	sum = 0	

	#comparison variable against sum
	#assign to the first pixel's sum
	smallest_and_darkest = pixel_values[0][0][0] + pixel_values[0][0][1] + pixel_values[0][0][2]

	#list of the two darkest pixels
	darkest_pixels = []
	#assign darkest pixel (the first position in this list) to the first pixel in the image
	darkest_pixels[0] = pixel_values[0][0]	
	
	#!!!!!
	#new strategy
	#create a list of the sums of the three values of each pixel in the pixel_values list
	sums = []
	#for loop to add in the elements
	for k in range(len(pixel_values)):
		sums[k] = pixel_values[k][0] + pixel_values[k][1] + pixel_values[k][2]

	#find the minimum value in the sums list
	#store minimum value in darkest_pixels
		#we also need to store which pixel that was -> currently storing the sum
		#i don't know what to do here
	darkest_pixels.extend(min(sums))

	#remove min
	#find the min again
	#store second min in darkest_pixels
	
	#how to make sure that the two pixels aren't next to each other??

	#OLD STRATEGY
	#actually how are these arrays stored is it by line or the whole thing is one long one dimensional array (the 2D elements are the 3 values)
	#for loop through the three dimensions already stored for each pixel
	#compare values using the sum variable
	for i in range(len(pixel_values)):
		for j in range(len(pixel_values)):
			#sum is equal to the three values for that pixel added together
			sum = pixel_values[i][j][0] + pixel_values[i][j][1] + pixel_values[i][j][2]
			#if this sum is smaller than the current smallest (meaning darkest pixel)
			if sum < smallest_and_darkest:
				#reassign smallest_and_darkest to the sum at that position
				smallest_and_darkest = sum

	#once we have found the darkest pixel and stored it in the darkest_pixels
	#we want to go find the second darkest
	#for m in range(len(pixel_values)):
		#for n in range(len(pixel_values)): 
				
		
if __name__ == '__main__':
	main ()
