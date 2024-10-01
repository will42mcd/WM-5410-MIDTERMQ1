from PIL import Image

def composite_image(IMG_NAME, BACKGROUND_IMAGE):
    threshold = 75
    with Image.open(IMG_NAME + '.jpg').convert('RGB') as im:
        pixels = list(im.getdata())
        color = pixels[0]
        no_back_pixels = []
        index = color.index(max(color))
        for p in pixels:
            if p[index] >= color[index] - threshold and p[index] - p[index-1] > threshold:
                no_back_pixels.append((0,0,0))
            else:
                no_back_pixels.append(p)        
        outimg = Image.new("RGB", im.size)
        with Image.open(BACKGROUND_IMAGE + '.jpg').convert('RGB') as im2:
            im2 = im2.resize(im.size)
            back_pixels = list(im2.getdata())
        final_pixels = []
        count = 0
        for p in no_back_pixels:
            if p == (0,0,0):
                final_pixels.append(back_pixels[count])
            else:
                final_pixels.append(p)
            count = count + 1
            
        outimg.putdata(final_pixels)
        outimg.save(IMG_NAME + '_composite.jpg')

def main():
    composite_image('jack','jack_back')
    composite_image('guard', 'guard_back')
        

if __name__ == '__main__':
    main()