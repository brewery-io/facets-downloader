import urllib2
from BeautifulSoup import BeautifulSoup

for i in range(316):
    if i % 63 == 0:
        page_url = "http://www.facets.la/offset/%s/" % i
        page_src = urllib2.urlopen(page_url).read()
        page_soup = BeautifulSoup(page_src)

        for div in page_soup.findAll("div", attrs = {"class": "thumb-image"}):
            preview_url = div.find("a")["href"]
            preview_src = urllib2.urlopen(preview_url).read()
            preview_soup = BeautifulSoup(preview_src)
            name = str(preview_soup.find("h1"))[4:-5]
            for preview_div in preview_soup.findAll("div", attrs = {"class": "size13"}):
                if "Download Wallpaper" in str(preview_div):
                    image_url = preview_div.find("a")["href"]
                    image_src = urllib2.urlopen(image_url).read()
                    image = open(name + ".jpg", "w")
                    image.write(image_src)
                    image.close()
                    print "Downloaded %s" % name
