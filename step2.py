#step 2
#extract all the pixel values from the image
#store in a list


def main ():
	#step 1	
	#importing the Image module of PIL
	from PIL import Image

	#creating Image object
	#opening the image for reading mode
	image = Image.open('grace-hopper.png', 'r')
	
	#step 2
	#used website: www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
	#create a list that is filled with the values stored in the pixels in the image
	pixel_values =  list(image.getdata())
	
if __name__ == '__main__':
	main ()
