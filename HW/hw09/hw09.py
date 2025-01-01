def label_squarer(t):
    """Mutates a Tree t by squaring all its elements.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> label_squarer(t)
    >>> t
    Tree(1, [Tree(9, [Tree(25)]), Tree(49)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        t.label = t.label ** 2
        
    for b in t.branches:
        t.label = t.label ** 2
        label_squarer(b)

    
    


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(8, [Tree(2), Tree(9, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> print(numbers)
    8
      2
      9
        4
        5
      6
        7
    >>> preorder(numbers)
    [8, 2, 9, 4, 5, 6, 7]
    """
    res = [t.label]
    
    if t is None:
        return [ ]
    
    for branch in t.branches:
        res.extend(preorder(branch))
    return res


class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

