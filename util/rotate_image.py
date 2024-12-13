from PIL import Image, ExifTags

image = Image.open("ANN_3747.JPG")

for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
exif = image._getexif()

if exif[orientation] == 3:
    image = image.rotate(180, expand=True)
elif exif[orientation] == 6:
    image = image.rotate(270, expand=True)
elif exif[orientation] == 8:
    image = image.rotate(90, expand=True)


# image = image.rotate(90)
image.save("ROTATED_ANN_3747.JPG")