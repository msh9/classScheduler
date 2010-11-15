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
    parser.add_option("-s","--spring",  
        help="Spring Classes")
    parser.add_option("-f","--fall",
        help="Fall Classes")
    parser.add_option("-p","--prereqs", 
        help="Class Prerequisites")
    (options,args) = parser.parse_args()
    print(options.winter)
    
    
    
    
    
if __name__ == "__main__":
    exit(main())