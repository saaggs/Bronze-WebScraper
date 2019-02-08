from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as bsoup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# Opening up connection, accessing web page
uClient = urequest(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = bsoup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "Newegg_products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
	branding = container.findAll("div", {"class":"item-branding"})
	brand = branding[0].a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()


	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()