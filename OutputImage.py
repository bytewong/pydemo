from PIL import Image


def get_char(r, g, b, alpha=256):
    grey_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ")
    #   灰度越小，颜色越深；灰度越大，颜色越浅。
    #   字符越靠前，灰度越小，颜色越深；字符越靠后，灰度越大，颜色越浅
    grey = (2126 * r + 7152 * g + 722 * b) / 10000
    length = len(grey_char)
    #   grey/alpha=x/length 灰度占256的比例对应字符在字符串中的相对位置
    return grey_char[int((grey * length) / 256)]


def main(width, height):
    image = Image.open("e:/yangjun1.jpg")
    image.resize((width, height),Image.NEAREST)
    text = ""
    for i in range(width):
        for j in range(height):
            text = text + get_char(*image.getpixel((j, i)))
        text = text + "\n"
    with open('e:/test.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main(600,600)
