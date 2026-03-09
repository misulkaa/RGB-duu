from PIL import Image

pic = Image.open("lesok.jpeg")
pic2 = Image.new("RGB", (pic.size[1], pic.size[0]), "white")
pixels = pic.load()
pixels2 = pic2.load()


for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        temp = pixels[x, y][0]
        pixels[x, y] = (0, temp, 0)


#menis cisla
pic.show()
pic.save('zelenykanal.jpeg')