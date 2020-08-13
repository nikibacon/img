from PIL import Image
import os #政府跟檔案相關


# for file in os.listdir('.'):  # '.' 現在位置的意思,listdir資料夾清單列出來的功能
#     if file.endswith('.jpg'): # string的功能,檢查字串的結尾

#         image_file = Image.open(file) # open image
#         image_file = image_file.convert('L') # covert image to black and white
#         image_file.save(file[:-4] + '_grey.png')


for file in os.listdir('orig'):  
    if file.endswith('.jpg'): # string的功能,檢查字串的結尾
        image_file = Image.open(os.path.join('orig', file)) # open image
        image_file = image_file.convert('L') # covert image to black and white
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))