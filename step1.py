#step one of the project
#goal: python program that loads image and prints it

#>>>from PIL import Image

#>>>im = Image.open('grace-hopper.png', ' r')

def main ():
	
	#importing the Image module of PIl
	from PIL import Image

	#creating an Image object
	#opening the image for reading mode (so then we can do stuff with it!)
	im = Image.open('grace-hopper.png', 'r')

if __name__ == '__main__':
	main()

#extract all pixel values from the image


#store all the pixels in a two dimensional array
#each pixel is a three dimensional array on its own



#for loop through the array
#goal: to find the darkest pixel


