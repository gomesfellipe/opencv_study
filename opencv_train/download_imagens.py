# https://gist.github.com/yunjey/14e3a069ad2aa3adf72dee93a53117d6
# First, you should install flickrapi
# pip install flickrapi

import flickrapi
import urllib
from PIL import Image

# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

# Positive

keyword = 'cockatiel'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    url = photo.get('url_c')
    urls.append(url)    
    # obter 50 urls
    if i > 50:
        break

# Veja as urls:
print (urls)

# Download das imagens e salvar na pasta positive_images
for i in range(len(urls)):
    urllib.request.urlretrieve(urls[i], 'positive_images/'+ str(i) +'.jpg')

# Ajustar tamanho das imagens e subscrever
for i in range(39):
    image = Image.open('positive_images/' + str(i) + '.jpg') 
    image = image.resize((256, 256), Image.ANTIALIAS)
    image.save('positive_images/' + str(i) + '.jpg')
    
    
# Negative ---
    
keyword = 'random'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=1000,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    url = photo.get('url_c')
    urls.append(url)    
    # obter 50 urls
    if i > 500:
        break

# Veja as urls:
print (urls)

# Download das imagens e salvar na pasta positive_images
for i in range(len(urls)):
    try:
        urllib.request.urlretrieve(urls[i], 'negative_images/'+ str(i) +'.jpg')
    except:
        print("Sem link em:"+str(i))

# Ajustar tamanho das imagens e subscrever
for i in range(501):
    try:
        image = Image.open('negative_images/' + str(i) + '.jpg') 
        image = image.resize((256, 256), Image.ANTIALIAS)
        image.save('negative_images/' + str(i) + '.jpg')
    except:
        print("Sem link em:"+str(i))