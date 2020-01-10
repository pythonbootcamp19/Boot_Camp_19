sample_url = 'http://coreyms.com'
print(sample_url)
#reverse the url
print(sample_url[::-1])
#print only .com
print(sample_url[-4:])
#print without http://
print(sample_url[7:])
#print the url without the http:// or the top level domain
print(sample_url[7:-4])
"""following 2 lines will print the same output. 
You can print the same output with different start 
and end numbers"""
print(sample_url[7:-4])
print(sample_url[7:14])

print(sample_url[7:-4:2])