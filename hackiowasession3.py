import requests
import os
import bs4

baseUrl = 'https://xkcd.com'
url = baseUrl
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):

    # TODO: Download the page
    print(f'Downloading {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image
    comic = soup.select('#comic img')
    if not comic:
        print('Coulnt find comic')
    else:
        try:
            comicUrl = 'http:' + comic[0].get('src')

            # TODO: Download the image
            res = requests.get(comicUrl)
            res.raise_for_status()

            # TODO: Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        except requests.exceptions.MissingSchema:
            pass

        # TODO: Get the prev button
        link = soup.select('a[rel="prev"]')[0]
        url = baseUrl + link.get('href')

print('Done')