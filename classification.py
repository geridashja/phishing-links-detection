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
    if (test.is_long(url) or test.has_at(url) or test.has_ngrok(url)) ==1:
        print("Phishing url content") 
        sys.exit()
    else:
        print("No phishing url content")
else:
    print("Invalid url")
    sys.exit()


