__author__ = 'Lukas Salkauskas'

import os
import requests

# Constants

# Identity related
_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7'
_headers = { 'User-Agent' : _user_agent }

def extractTagFromString(stringValue, startTag, endTag):
    """
     Helper method will extract information between two tags.
     f.ex a string = "<a> hello lady <a>"
            startTag = "hello"
            endTag = "<a>"
            Result = "lady"
    """
    startIndex = stringValue.find(startTag)
    if startIndex != -1:
        # move starting index to the end of the tag.
        startIndex += len(startTag)

        # endIndex will be calculated in the string, starting from startIndex
        endIndex = stringValue.find(endTag, startIndex)
        if endIndex != -1:
            # slice string and return a result.
            return stringValue[startIndex:endIndex]
        return ''

def dir_list2(dir_name, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)

        # folder name can be movie name as well
        #if os.path.isfile(dirfile):
        if len(args) == 0:
            fileList.append(os.path.splitext(os.path.basename(dirfile))[0])
        else:
            if os.path.splitext(dirfile)[1][1:] in args:
                fileList.append(os.path.splitext(os.path.basename(dirfile))[0])
        '''
        elif os.path.isdir(dirfile):
            print "Accessing directory:", dirfile
            fileList += dir_list2(dirfile, *args)
        '''
    return fileList

def main():
    print 'Reading files on current folder...'
    input_data = dir_list2('.')
    input_data_list = list()

    for data in input_data:
        input_data_list.append(data.replace('./', '').replace('-', ' ').replace('.', ' ').replace('_', ' '))

    # remove object.
    del input_data

    for data in input_data_list:
        requestObj = requests.get('http://www.google.lt/search?aq=f&sourceid=chrome&ie=UTF-8&q='+data.replace(' ', '+'), headers = _headers)
        html = requestObj.content
        if html:
            print data.upper() + ' - ' + str(extractTagFromString(html, 'Reitingas: ', '/'))
        else: print data + ' - no data'

if __name__ == '__main__':
    main()