#!/usr/bin/env python

from urllib import urlretrieve
from urllib2 import urlopen, urlparse
from BeautifulSoup import BeautifulSoup
import re, sys, os.path

def main(url):
    dir = 'tmp'
    # Example URL: http://picturesofshit.com/v/2009/10-15_-_Dudescademy/
    img_size_qry_string = '?g2_imageViewsIndex=1'

    # Go to gallery and grab links to high resolution photos
    gallery = urlopen(url)
    soup = BeautifulSoup(gallery.read())
    links = [tag.attrMap['href'] + img_size_qry_string for tag in soup.findAll(href=re.compile('JPG.html'))]

    # Go to each link, grab the image source, and download
    links = [urlparse.urljoin(url, link) for link in links]

    for link in links:
        gallery_image = urlopen(link)
        soup = BeautifulSoup(gallery_image.read())
        image_url = urlparse.urljoin(url, soup.find('img', 'ImageFrame_none').attrMap['src'])
        file_name = re.search('([^/]+)$', image_url).groups()[0]
        file = os.path.join(dir, file_name)
        print 'Downloading %s' % file_name
        urlretrieve(image_url, file)
    print '--- Downloads Complete ---'

if __name__ == "__main__":
    main(sys.argv[1])
