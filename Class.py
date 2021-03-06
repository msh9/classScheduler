"""python module that defines class objects
"""

class Course:
    """A course satisfies prerequisites but does not occur during a specific
    time period. The Class object is a course that occurs during a specific
    quarter
    """

    def __init__(self, name, credits, offered):
        """We define a course, this consists of the number of
        credis, the name, and when it is offered

        Returns: A Course object
        """
        self.credits = credits
        self.name = name
        self.offered = offered

    def __str__(self):
        return self.name

    def __repr__(self):
        return " ".join([self.name,repr(self.credits),repr(self.offered)])

    def __eq__(self, other):
        return self.name == other.name 
    
    def __ne__(self,other):
        return not self.__eq__(self,other)

    def __hash_(self):
        val = hash(self.name)
        val += self.credits
        for of in self.offered:
            if of == 1:
                val += 7
        return val

class Class(Course):
    """Defines a class object that is used in the rest
    of the scheduler. The class at the least has time, credits, qtr offered,
    and name attributes. Other possible attributes are prereq for and prereq
    satisfied values. Note that for our purposes the name & time, offered 
    attributes should be enough to uniquely id a class
    """
    
    def __init__(self, time, offered, section, sln, course):
        """Initializer for the class object
        Arguments:
            Time: A three tuple (t_begin,t_end)
            Offered: An integer 0-3: 0 = fall,1=winter,2=spring,3=summer
            Name: A string, the name of the class
            Section: A string letter code for the section of the class, this doesn't
            need to be specified
            Sln: schedule identifier number
            course: A Course ojbect indicate what this class is
        Returns: A Class object
        """
        self.time = time
        self.offered = offered
        self.section = section
        self.sln = sln    
    	self.children = 0
    
    # below we define string operations
    def __str__(self):
        """Definition of informal to string function"""
        return name
    
    def __repr__(self):
        """Returns a more formal string representation"""
        return " ".join([str(self.time),str(self.credits),str(self.offered),
            name])
    
    # with to string operations defined we define what it means for equality 
    # to exist
    
    def __ne__(self, other):
        """Defines concept of not equal
        Essentially return true if the name or times don't match (or if other
        is not a class object
        """
        
        if isinstance(other,Class):
            return (self.name != other.name or self.time != other.time or 
                self.offered != other.offered or self.section != other.section)
        else:
            return True
    
    def __eq__(self,other):
        """we make equality simply the opposite of not equal..."""
        return not self.__ne__(other)
        
    # for other comparisions we use cmp
    
    def __cmp__(self, other):
        """defines comparison value for <, >"""
        if isinstace(other,Class) and self.__ne__(other):
            return self.credits - other.credits
        elif isinstanceof(other,Class):
            return 0
        return False
    
    def __hash__(self):
        """Defines that hash function for this object, we simply
        combine the hash values for the stored attributes"""
        
        # define a lamba to do c-style int multiplication (with overflow)
        c_mult = lambda a,b: eval(hex((a * b) & 0xFFFFFFFF)[:-1])
        
        hash_val = hash(self.name)
        for d in self.time.values():
            hash_val += hash(d)
        for qtr in self.offered:
            if qtr:
                hash_val = c_mult(hash_val, 19)
        hash_val += hash(self.name) + hash(self.section)
        return hash_val

    def set_children(self,children):
        self.children = children
        
class PrerequisiteNode(Class):
    """Defines a node in the prerequsite tree
    Inherits from class for basic properties and then adds some more to handle
    representing class prerequisites
    """
    
    def __init__(self, time, credits, offered, name, prereqs, points_to):
        """Same arguments as Class initializer, plus two more arguments
        
        Prereq: A list of sets of prerequsites. Logically the list should be in
        disjunction of conjunctions form. For the class to be available at least
        one entire set of prereq from the set must be satisfied.
        
        Points_to: A tuple that contains a list of PrerequisiteNodes that this
        current class is a prereq _for_. It's worth noting that each node in this
        graph has information about its parents and children, not necessarily
        space efficient, but it may allows us to run in a reasonable
        amount of time
        """
        
        super().__init__(time, credits, offered, name)
        self.prereqs = prereqs
        self.points_to = points_to
    
    # interesting I think we can safely leave everything else alone...
