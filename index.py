from PIL import Image

def resize_image(sizel, size2) :
    image = Image.open('/Users/creativelabs/Image_resizer/resize_image_test.jpeg')

    print(f"Current size : {image.size}" )

    resized_image = image.resize(( sizel, size2))
    
    resized_image.save('image_test-resized' + str(size1) + '.jpeg')

size1 = int(input( ' Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2)