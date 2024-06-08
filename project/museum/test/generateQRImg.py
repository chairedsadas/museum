import qrcode
from PIL import Image

def create_qrcode(url, filename):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4, 
    )

    qr.add_data(url)
    qr.make(fit=True)
    img=qr.make_image()

    img=img.convert("RGBA")
    icon=Image.open(filename)
    w,h=img.size
    factor=4
    size_W=int(w/factor)
    size_H=int(h/factor)
    icon_w,icon_h=icon.size
    if icon_w>size_W:
        icon_w=size_W
    if icon_h>size_H:
        icon_h=size_H
    icon=icon.resize((icon_w,icon_h),Image.LANCZOS)
    w=int((w-icon_w)/2)
    h=int((h-icon_h)/2)
    icon=icon.convert("RGBA")
    newimg=Image.new('RGBA',(icon_w + 8, icon_h + 8),(255,255,255,0))
    img.paste(newimg,(w-4, h-4), newimg)
    img.paste(icon,(w,h),icon)
    img.save("qr.png", quality=100)

if __name__ == "__main__":
    create_qrcode("https://www.baidu.com", "../../../about/logo.png")
    print("Done")