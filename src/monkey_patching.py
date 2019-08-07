# In Python, the term monkey patch only refers to dynamic modifications of a class or module at runtime, motivated by
# the intent to patch existing third-party code as a workaround to a bug or feature which does not act as you desire.

# Testing Example
# How can we use this knowledge, for example, in testing?
#
# Say we need to simulate a data retrieval call to an outside data source that results in an error, because we want to
# ensure correct behavior in such a case. We can monkey patch the data structure to ensure this behavior.
# (So using a similar method name as suggested by Daniel Roseman:)

import datasource

def get_data(self):
    '''monkey patch datasource.Structure with this to simulate error'''
    raise datasource.DataRetrievalError

datasource.Structure.get_data = get_data

# And when we test it for behavior that relies on this method raising an error, if correctly implemented,
# we'll get that behavior in the test results.
#
# Just doing the above will alter the Structure object for the life of the process, so you'll want to use setups and
# teardowns in your unittests to avoid doing that, e.g.:

def setUp(self):
    # retain a pointer to the actual real method:
    self.real_get_data = datasource.Structure.get_data
    # monkey patch it:
    datasource.Structure.get_data = get_data


def tearDown(self):
    # give the real method back to the Structure object:
    datasource.Structure.get_data = self.real_get_data

# (While #  the above is fine, it would probably be a better idea to use the mock library to patch the code.mock's patch
# decorator would be less error prone than doing the above, which would require more lines of code and thus more
# opportunities to introduce errors. I have yet to review the code in mock but I imagine it uses monkey-patching
# in a similar way.)
