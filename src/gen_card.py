from PIL import Image,ImageFont,ImageDraw

# generate round avatar
def convert_image_to_circle(pic_path,back_path):
    ima = Image.open(pic_path).convert("RGBA")
    size = ima.size

    # generate  square image
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        imb = Image.new('RGBA', (r2, r2), (255, 255, 255, 0))
        pima = ima.load()
        pimb = imb.load()
        for i in range(r2):
            for j in range(r2):
                pimb[i, j] = pima[(size[0] - r2) / 2 + i, (size[1] - r2) / 2 + j]
    else:
        imb = ima

    # generate round image
    r3 = int(r2 / 2)
    imc = Image.open(back_path)
    pimb = imb.load()
    pimc = imc.load()

    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r3)
            ly = abs(j - r3)
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5

            if l > r3:
                pimb[i, j] = pimc[i, j]
    return imb


# add tetx to card
def add_text_to_card_img(image,text,x_size=2.0,y_size=3.0):
    b_w, b_h = image.size[0], image.size[1]
    p_x,p_y=int(b_w/x_size),int(b_h/y_size) # position of text
    size=(p_x,p_y)
    text_size = 50
    setFont = ImageFont.truetype(font=r"resource\仓耳小丸子.ttf",size=text_size)

    draw = ImageDraw.Draw(image)
    draw.text(size, text, font=setFont,fill='white')
    return image


# generate greeting card
def gen_card(ava_path,back_path,card_path,text,card_name='card',w_size=4.8,h_size=2.3):
    img=convert_image_to_circle(ava_path,back_path)
    img=img.resize((int(img.size[0]*0.8),int(img.size[1]*0.8)),Image.ANTIALIAS)

    back=Image.open(card_path)
    b_w,b_h=back.size[0],back.size[1]
    i_w,i_h=img.size[0],img.size[1]

    w=int((b_w-i_w)/w_size)
    h=int((b_h-i_h)/h_size)
    back.paste(img,(w,h),mask=None)

    back=add_text_to_card_img(back,text,3.0,2.37)
    save_path='cards/'+card_name
    back.save(save_path+'.png')
    print('successfully generate the greeting card!!!')


if __name__=='__main__':
    ava_path=r'resource\ava.jpg'
    back_path=r'resource\lvse.png'
    card_path=r'resource\card.png'
    text='round'
    gen_card(ava_path,back_path,card_path,text)





