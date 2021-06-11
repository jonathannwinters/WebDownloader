#!//usr/bin/python



__author__ = "Jonathan N. Winters"
__copyright__ = "Copyright June, 9 2021"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonathan N. Winters"
__email__ = "jnw25@cornell.edu"
__status__ = ""


# Usage:
# create a single column text file with all of the desired full URLs, ie:
#  http://www.domain.com/file1.pdf
#  http://www.domain.com/file2.jpg
#  http://www.domain.com/file3.csv
# and so on...

# save the file as input.txt

# execute the following:
#  $ WebDownloader.py input.txt /destination/path

import sys, os, wget

input_file = sys.argv[1]
destination_path = sys.argv[2]


with open(input_file) as file:
    for count,line in enumerate(file):
        url = line.strip()

        print(count, url)

        file_name =  url.split("/")[-1]
        
        try:
            os.mkdir(destination_path)
        except Exception as e:
            print(e)

        try:
            wget.download(url, destination_path + "/" + file_name)
        except Exception as e:
            print(e)

