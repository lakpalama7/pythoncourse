from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import time
import os

def download_image(url):
    image_data = None
    with urlopen(url) as f:
        image_data = f.read()
     

    if not image_data:
        raise Exception(f"Error: could not download the image from {url}")

    filename = os.path.basename(url)
    with open("./dist/sales/" +filename, 'wb') as image_file:
        image_file.write(image_data)
        print(f'{filename} was downloaded...')

start = time.perf_counter()

urls = [
    'https://www.python.org/static/community_logos/python-logo.png',
    'https://www.python.org/static/community_logos/python-powered-h-140x182.png',
    'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
    'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
]

with ThreadPoolExecutor() as executor:
     executor.map(download_image, urls)
finish = time.perf_counter()    

print(f'It took {finish-start} second(s) to finish.')