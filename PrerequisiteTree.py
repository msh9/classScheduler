"""module contains class definitions and code for the prerequisite tree
"""

class PrerequisiteTree:
    """Uses prerequisite nodes"""
    def __init__(self, have_taken, final_set):
        """initializes the tree to be empty
        Arguments:
            have_taken: Classes that we start with this is just an initial
            condition set
            final_set: The culminating set of class that need to be taken to
            graduate. We'll start with those for a BS in Math"""
        this.fringe = set()
        # initially we start with a tree for class needed then merge as needed
        this.trees = final_set
        this.have_taken
