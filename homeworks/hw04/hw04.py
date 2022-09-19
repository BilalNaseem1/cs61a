def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    prev = 0
    curr = 1

    i = 2
    fib_count = 0

    fib_list = [prev, curr]

    def fib_generator():
        nonlocal prev, curr, i, fib_count

        while True:
            yield fib_list[fib_count]
            fib_count += 1

            if fib_count >= i:
                prev, curr = curr, prev + curr
                fib_list.append(curr)
                i += 1
    
    fib = fib_generator()
    return lambda: next(fib)


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    pwd_log = []
    MAX_PWD_ATTEMPTS = 3
    def withdraw(amount, usr_pwd):
        nonlocal balance

        if usr_pwd != password and len(pwd_log) < MAX_PWD_ATTEMPTS:
            pwd_log.append(usr_pwd)
            return 'Incorrect password'
        elif len(pwd_log) == MAX_PWD_ATTEMPTS:
            return 'Your account is locked. Attempts: [\'{p1}\', \'{p2}\', \'{p3}\']'.format(p1 = pwd_log[0], p2 = pwd_log[1], p3 = pwd_log[2])
        elif amount > balance:
            return 'Insufficient funds'
        else:
            balance -= amount
            return balance
    return withdraw


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2019
    >>> dime = mint.create(Dime)
    >>> dime.year
    2019
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2019
    >>> nickel.worth()  # 5 cents + (81 - 50 years)
    36
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (106 - 50 years)
    116
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (106 - 50 years)
    126

    """
    current_year = 2019

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)
         

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.current_year

class Coin:
    VALUE_TRESHOLD_YRS = 50
    def __init__(self, year):
        self.year = year
        self.age = Mint.current_year - self.year 

    def worth(self):
        "*** YOUR CODE HERE ***"
        if self.has_added_value():
            return self.cents + self.get_added_value()
        else:
            return self.cents
    
    def has_added_value(self):
        return self.get_age() > self.VALUE_TRESHOLD_YRS

    def get_added_value(self):
        return self.get_age() - self.VALUE_TRESHOLD_YRS 

    def get_age(self):
        return Mint.current_year - self.year


class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.deposit_amount = 0

    def is_out_of_stock(self):
        return self.stock == 0

    def has_insuficient_funds(self):
        return self.deposit_amount < self.price

    def get_out_of_stock_msg(self):
        return 'Machine is out of stock.'

    def get_stock_msg(self):
        return 'Current {product} stock: {stock}'.format(product = self.product, stock = self.stock)

    def get_here_is_your_msg(self, item):
        return 'Here is your {item}'.format(item = item)

    def get_format_money_msg(self, amount):
        return '${amount}'.format(amount = amount)

    def get_insuficient_funds_msg(self):
        return 'You must deposit {amount} more.'.format(amount = self.get_format_money_msg(self.price - self.deposit_amount))

    def deposit(self, amount):
        if self.is_out_of_stock():
            return self.get_out_of_stock_msg() + ' ' + self.get_here_is_your_msg(self.get_format_money_msg(amount)) + '.'
        else:
            self.deposit_amount += amount
            return 'Current balance: {balance}'.format(balance = self.get_format_money_msg(self.deposit_amount))

    def restock(self, amount):
        self.stock += amount
        return self.get_stock_msg()

    def vend(self):
        if self.is_out_of_stock():
            return self.get_out_of_stock_msg()
        elif self.has_insuficient_funds():
            return self.get_insuficient_funds_msg()
        else:
            self.stock -= 1
            self.change = self.deposit_amount - self.price
            self.deposit_amount = 0
            return (self.get_here_is_your_msg(self.product)) + (' and {change} change.'.format(change = self.get_format_money_msg(self.change)) if self.change > 0 else '.')

def remove_all(link , value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    while link.rest is not Link.empty:
        if link.rest.first != value:
            link = link.rest
        else:
            link.rest = link.rest.rest


def generate_paths(t, x):
    """Yields all possible paths from the root of t to a node with the label x
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    #"*** YOUR CODE HERE ***"
    root = t.label
    print(root)
    #for _______________ in _________________:
    #    for _______________ in _________________:

            #"*** YOUR CODE HERE ***"

## Link Class ##

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

## Tree Class ##

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
