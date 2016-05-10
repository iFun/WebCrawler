from six.moves.urllib.parse import urlparse
#from urllib.parse import urlparse

# Get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split()
        return '{0}.{1}'.format(results[-2],results[-1])
    except:
        return ''



# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

