import os.path
def download_file(url, filename):
    if os.path.isfile(filename):
        print("Already present %s." % filename)
    else:
        print("Downloading %s" % filename)
        #request.urlretrieve(url, filename)
