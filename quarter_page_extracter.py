"""Short script to extract math classes from a particular quarter page"""

import os.path
import sys
import re

class offering:
    def __init__(this,sln, code, cr, days, btime, etime):
        this.sln = int(sln)
        this.code = code
        this.cr = int(cr)
        this.days = days
        this.start_time = btime
        this.end_time = etime
        
    def __str__(this):
        return ",".join([str(this.sln),this.code,str(this.cr),this.days,this.start_time,this.end_time])

def main(args):
    """Controls main program execution
    Arguments:
        args: A string list of command line arguments, essentially sys.argv
        
    Returns Int for success or failure
    """
    if len(args) != 2:
        # Too many args or was the argument was not a path to a file
        print("Too many args")
    elif not (os.path.isfile(args[1])):
        print("Cannot find "+args[1])
    # gets lines from file
    lines = open(args[1], 'r').readlines()
    classes = {}
    # prepare regular expressions
    math_class = re.compile(r"^\*?MATH\s+(\d\d\d).*<.*>\*")
    main_section = re.compile(r"(\d{5})\s<.*>\s(\w)\s+(\d)\s+(\w{1,6})\s+(\d{3,4})-(\d{3,4})")
    qz_section = re.compile(r"(\d{5})\s<.*>\s(\w\w)\s+QZ\s+(\w{1,6})\s+(\d{3,4})-(\d{3,4})")
    curr_class = 0
    curr_sec = None
    for line in lines:
        math_class_match = math_class.match(line)
        main_section_match = main_section.search(line)
        qz_section_match = qz_section.search(line)
        # priority one is switching the current class
        if math_class_match is not None:
            print("Matched "+math_class_match.group(1))
            curr_class = int(math_class_match.group(1))
        # next pri is switching the offered sections of a course
        elif main_section_match is not None:
            curr_sec = offering(main_section_match.group(1),
                main_section_match.group(2),main_section_match.group(3),
                main_section_match.group(4),main_section_match.group(5),
                main_section_match.group(6))
            try:
                classes[curr_class].update({curr_sec:[]})
            except KeyError:
                classes[curr_class] = {curr_sec:[]}
        # finally we consider the qz sections offered
        elif qz_section_match is not None:
            curr_qz = offering(qz_section_match.group(1),
                qz_section_match.group(2),0,
                qz_section_match.group(3),qz_section_match.group(4),
                qz_section_match.group(5))
            classes[curr_class][curr_sec].append(curr_qz)
    for k in classes.keys():
        print("Class Math"+str(k))
        for (j,v) in classes[k].items():
            print("\t"+str(j))
            for q in v:
                print("\t\t"+str(q))
    return 0
    
if __name__ == '__main__':
    exit(main(sys.argv))
