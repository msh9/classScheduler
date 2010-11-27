"""The Quarter Solver module contains the code to solve a 
quarterly class problem. This solving the knapsack with conflict
graphes problem
"""

class QtrSolver():
    """Class that contains state and functions for the quarter solver"""

    def __init__(self,prereq_base, available_classes):
        """__init__ sets up the solver object with the initially required
        information to solve the problem

        Arguments:
            prereq_base: The propositional logic dictionary
            available_classes: The classes available in the current quarter

        Returns: A QtrSolver object
        """

        self.prereqs = prereq_base
        self.avail_classes = available_classes
        self.current_classes = None

    def run_solve(self, qtr_index, courses = set()):
        """Runs the solver against the current quarter index and current
        current_classes set.

        Arguments:
            qtr_index: The current quarter index
            courses: Defaults to empty the set of classes we would like to first
            update the solver with

        Returns: An (hopefully) optimal set of classes to take
        """
        # 1st determine the classes we can take
        qtr_classes = self._determine_avail_classes(qtr_index)
        self.build_c



    def _determine_avail_classes(self,qtr_index):
        """Determines the available classes based on the qtr_index, the current
        classes available, and the classes taken

        Returns a set of classes that can be taken
        """
        result = set()
        for k,v in self.prereqs.items:
            for rule in v:
                if (rule <= self.current_classes and k in
                    self.available_classes[qtr_index]):
                    break
                    result.add(k)

        return result


    def courses(self, class_set):
        """Sets the initial set of courses we have taken
        """
        if self.current_classes is None:
            self.current_classes = class_set
        else:
            self.current_classes.update(class_set) 
