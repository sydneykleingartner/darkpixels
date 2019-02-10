# darkpixels

a python program that finds the two darkest pixels in an image and puts an "X" on top of each

what i have done:
- download homebrew
- download python conda
- check that PIL (python image library) is downloaded in the correct version
- choose an image
    - in darkpixels directory
- step1.py
    - loaded in image to do more cool stuff with!
- step2.py
    - extract all pixel values from the image and store in a list
    - print out the for loop for formatting checking 
- step3.py
    - initialize variables and for loops
    - overall strategy for step 3

what i still need to do:  
- step3.py
    - for loop through the list to find the two darkest pixels
    - store these two pixels (that are not next to each other) in an array
            -i'm having SO much trouble with this -> would it be more efficient to go through looking for the darkest first and then the second darkest?
            -how do i know that the two pixels aren't next to each other?
            -need to work more on python list syntax & function
    - for each, replace the color of that specific pixel with red
    - as well, place the X's around each
      - in the two dimensional array that the pixels are stored in, place red at the pixels around it to form an X
- celebrate!

some websites i have gotten help from:

    - https://code.tutsplus.com/tutorials/image-processing-using-python--cms-25772?fbclid=IwAR37XgqfY6xdMTNvbANny-JpNbKkhTR-okyZfaOyr9ZLN2dzjPRfgu4PSC8
    
    - https://snakify.org/en/lessons/two_dimensional_lists_arrays/?fbclid=IwAR067q-IIZ48JLFvBWerOU9rF3fUC55nlem5ZNO5ofRqM1b8gD-kCIB-290
    
    - https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
    
    - https://developers.google.com/edu/python/lists
    
    - https://www.programiz.com/python-programming/list
    
    
   current questions:
        - how do i reference one specific value in a pixel?
                ex. we print out the three numbers in (124, 127, 135) BUT what i specifically wanted to reference 124?
        - storing the second best pixel
                - what is the best way to do this? most efficient versus least complicated (both are pretty complicated in my brain right now though)
                        - using two for loops feels quite inefficient
                            - you would need to scan through the sums to find the minimum and then scan through again looking for the second smallest sum, meanwhile storing these in an effective way
                
    brainstorming:
        - if the darker the pixel, the smaller the sum of the numbers
                THEN: 
                    - add together the #'s in the pixel
                    - find the two smallest sums
                            - would this always work? or is it close enough for now?
   
   
