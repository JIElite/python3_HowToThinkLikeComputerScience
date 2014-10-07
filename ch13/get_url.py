import urllib.request


url = "http://realblog.zkiz.com/greatsoup38/75180"
destination_file = "url_output.txt"
urllib.request.urlretrieve(url, destination_file)

