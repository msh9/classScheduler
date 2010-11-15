"""main module, does the file io reading in the quarterly class information
and prerequisite information"""

from optparse import OptionParser
import os.path

def main():
    """Main application entry point, args should be parsed by 
    optparser
    
    Returns an int indicating exit status
    """
    parser = OptionParser()
    # default action = store and default type check = string
    parser.add_option("-w","--winter", 
        help="Winter Classes")
    parser.add_option("-g","--spring",  
        help="Spring Classes")
    parser.add_option("-f","--fall",
        help="Fall Classes")
    parser.add_option("-p","--prereqs", 
        help="Class Prerequisites")
    parser.add_option("-s","--summer",
        help="Summer Classes")
    (options,args) = parser.parse_args()
    # initialize a dictionary to hold files
    files = {}
    # by default we won't take summer classes
    summer_classes = False
    # the next piece is messy, essentially we check that each file ame was
    # specified and is a valid file name. If so then we open the files and
    # store the file handles in the files dictionary
    if (options.summer is not None and os.path.isfile(options.summer)):
        summer_classes = True
        files['summer'] = open(options.summer) #default open mode is read only
    if (options.fall is not None and os.path.isfile(options.fall)):
        files['fall'] = open(options.fall)
    else:
        print("Fall classes were not specified")
        return 1
    if (options.winter is not None and os.path.isfile(options.winter)):
        files['winter'] = open(options.winter)
    else:
        print("Winter classes were not specified")
        return 1
    if (options.spring is not None and os.path.isfile(options.spring)):
        files['spring'] = open(options.spring)
    else:
        print("Spring classes were not specified")
        return 1
    if (options.prereqs is not None and os.path.isfile(options.prereqs)):
        files['prereqs'] = open(options.prereqs)
    else:
        print("Prereqs were not specified")
        return 1
     
    print(str(files))
    return 0
    
if __name__ == "__main__":
    exit(main())