import urllib.request as urllib
import progressbar
import time
import test


def main(url='www.google.com'):
    
    response = urllib.urlopen('https://' + url)
    
    print('Checking Connectivity, Please Wait!')
    for _ in progressbar.progressbar(range(100)):
        time.sleep(0.02)
    print('Status' , response.getcode())
    
    return response.getcode()
    
    ...
    
#print('Greetings and welcome to the URL Checker!')

#url = input('Enter a website url --> ') 
#main(url)

def test_urlChecker(func):
    if func() in range(200,500):
        test.print_pass(func.__name__)
    else:
        test.print_fail(func.__name__)
        
test_urlChecker(main)