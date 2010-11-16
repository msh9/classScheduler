"""main module, does the file io reading in the quarterly class information
and prerequisite information"""

from optparse import OptionParser
import os.path
import Class

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

def parse_normal_form(reqs):
    """Parse normal form takes a string in pseudo propositional logic that is
    in disjunctive normal form and converts it into a list of sets.
    
    Arguments:
        regs: A string of the form specified in the README file for class
            prerequisites
    Returns: 
        A list of sets
    Example:
        A | (B & C) will become [ (A), (B, C) ]
    """
    final = []
    # first split into list of disjunctions
    conjunctions = reqs.split("|")
    # for each conjunctive term...
    for conjunction in conjunctions:
        curr_set = None
        # are we dealing with a bunch of terms together?
        if conjunction.strip().startswith('('):
            # if so we...get ready...strip off space at either end of the term, then strip off
            # then ( ), then we split on &, then we use a map to take the split list to one where
            # all elements have had the trailing and leading white space stripped, then finally
            # we put the final list into a frozen(constant)set
            curr_set = frozenset(map(lambda x: x.strip(),conjunction.strip()[1:-1].split('&')))
        else:
            # or if we have a single term we just put it into a singleton frozenset...
            curr_set = frozenset([conjunction.strip()])
        final.append(curr_set)   
    return final

def main():
    """Main application entry point, args should be parsed by 
    optparser
    
    Returns an int indicating exit status
    """
    # get options
    files = get_options()
    # check if we had an error
    if files == 1:
        return 1
    # if no error continue executing
    # create a set of all classes we will ever consider (i.e. the union of all
    # sets of classes offered every quarter)
    quarters = ['fall','winter','spring']
    if 'summer' in files.keys():
        quarters.append('summer')
    all_classes = {}
    i = 0 
    for qtr in quarters:
        for line in files[qtr]:
            (cls, credits) = line.split(':')
            try:
                # subscript madness: cls indexes into the dictionary by the class name key,
                # then we index into the first item in the list, and then finally index into
                # the offered tuple by quarter i
                all_classes[cls][0][i] = True
            except KeyError:
                offered = [False,False,False,False]
                offered[i] = True
                all_classes[cls] = [offered, int(credits)]
            else:
                 
                all_classes[cls][0][i] = True
        i += 1
    
    
if __name__ == "__main__":
    exit(main())