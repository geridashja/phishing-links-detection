import validators 
import sys 
import time

class Classification:
    def __init__(self,url):
        self.url = url
    
    def is_long(self,x):
        if len(str(x)) > 53:
            return 1
        return 0

    def has_at(self,x):
        if '@' in str(x):
            return 1
        return 0
    
    def double_slash(self,x):
        if '//' in str(x):
            return 1
        return 0

    def has_minus(self,x):
        if '-' in str(x):
            return 1
        return 0
    
    def many_subd(self,x):
        if str(x).count('.') > 3:
            return 1
        return 0
    
    def has_ngrok(self,x):
        if 'ngrok' in str(x):
            return 1
        return 0

#validating url
url = input('Enter an valid url to test for phishing content: ')
isValid = validators.url(url)
if isValid == True:
    print("Valid url")
    time.sleep(1)
    print("Checking for phishing content...")
    time.sleep(5)
    test = Classification(url)
    test.url = url
    if 'www' in url:
        domain = url.split('//www.')[1].split('.')[0]
    else:
        domain = url.split('//')[1].split('.')[0]
    #print(domain)
    if (test.is_long(url) or test.has_at(url) or test.has_ngrok(url)) ==1:
        print("Phishing content in FULL URL") 
        sys.exit()
    if (test.double_slash(domain) or test.has_minus(domain) or test.many_subd(domain)) ==1:
        print("Phishing content in DOMAIN") 
        sys.exit()
    else:
        print("No phishing content")
        sys.exit()
else:
    print("Invalid url")
    sys.exit()


