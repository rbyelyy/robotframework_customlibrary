class MyLibrary(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, arg_one):
        self.i_arg = arg_one

    def keyword_1(self):
        print 'Hello' + str(self.i_arg)

    def keyword_2(self, arg_one):
        return arg_one.upper()

    def keyword_3(self, *args):
        for i in args:
            print i




