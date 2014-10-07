import urllib.request

def retrieve_page(url):

    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta



the_text = retrieve_page("http://realblog.zkiz.com/greatsoup38/75180")
print(the_text)

