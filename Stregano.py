'''
   Steganorgaphy Progamm v 1.0 
   This programm can help you to hide your message into .png file!
   Just enter your text and the unique picture will be downloaded automatically!
   You will find it in your home directory and choose this picture to paste your text in!
   Follow the instructions!
'''


from bs4 import BeautifulSoup
import urllib.request
import random
import string
import Image, stepic

  # finding the image

url_base = 'https://prnt.sc/'
result = 0
picture_name =""
def get_html():
    global url_last3
    url_last3 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(3)))
    req = str(url_base + url_first3 + url_last3)
    html = urllib.request.urlopen(req).read()
    return html

def main():
    count = 1
    pic_count = int(count)
    global url_first3
    count = 1
    url_first3 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(3)))
    print("\n Loading image...\n")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    for counter in range(pic_count):
        html = get_html()
        soup = BeautifulSoup(html, 'html.parser')
        picture_url = soup.find(id='screenshot-image')['src']
        urllib.request.urlretrieve(picture_url, picture_url[40:])
        count = counter + 1
        print (str(count) + ' - [' + picture_url + '] - DONE!')
        picture_name=picture_url

if __name__ == '__main__':

   # Input the text, then encode it

   message = input("Input the message \n")
   message = str(message)
   b_message = str.encode(message)
   while result == 0:
    try:
     main()
     result+=1
    except:
     print("Wait..")

   # Input the text into picture

   result = 0
while result == 0:
 try:
   name=input("\n Input the name of your picture \n")
   im = Image.open(str(name))
   im2 = stepic.encode(im, b_message)
   im2.save("ImageGetter"+"test.png")
   result+=1
 except:
     print("Failed, try again...")

# Checking the result

answer = input("\n Want to check ? Y/N \n")
if answer == 'Y':
    im3 = stepic.decode(im2)
    print("\n result =   "+im3)
