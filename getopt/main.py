import sys
import getopt

try:
    options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
except getopt.GetoptError as err:
    print(err)
    sys.exit()

for name,value in options:
    print('key:{0} value:{1}'.format(name,value))