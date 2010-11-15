"""main module, does the file io reading in the quarterly class information
and prerequisite information"""

from optparse import OptionParser
import os.path

def get_options():
    """Uses an OptionParser to parse command line options
    Returns a python dict of str -> file if successful. Prints an error and returns 1
    otherwise
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
    # the next piece is messy, essentially we check that each file ame was
    # specified and is a valid file name. If so then we open the files and
    # store the file handles in the files dictionary
    if (options.summer is not None and os.path.isfile(options.summer)):
        files['summer'] = open(options.summer) #default open mode is read only
    else:
        print("Summer classes were not specified")
        return 1
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
    return files

def main():
    """Main application entry point, args should be parsed by 
    optparser
    
    Returns an int indicating exit status
    """
    # get options
    files = get_options()
    # check if we had an error
    if (files == 1) {
        return 1
    }
    # if no error continue executing
    
    
if __name__ == "__main__":
    exit(main())