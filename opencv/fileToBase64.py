import base64

def fileToBase64(path):
    with open(path,'rb') as f:
        return base64.b64encode(f.read())

if '__main__'==__name__:
    import sys
    base64_str=fileToBase64(sys.argv[1]).decode("utf8")
    print(base64_str)
    with open('./demo.base64','w') as f:
        f.write(base64_str)