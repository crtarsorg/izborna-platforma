
import unittest

class FooTest(unittest.TestCase):
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_:begin"

        testName = self.shortDescription()
        if (testName == "Test routine A"):
            print "setting up for test A"

        elif (testName == "Test routine B"):
            print "setting up for test B"

        else:
            print "UNKNOWN TEST ROUTINE"

        print "FooTest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_:begin"

        testName = self.shortDescription()
        if (testName == "a"):
            print "cleaning up after test A"

        elif (testName == "Test routine B"):
            print "cleaning up after test B"

        else:
            print "UNKNOWN TEST ROUTINE"

        print "FooTest:tearDown_:end"

    # test routine A
    def testA(self):
        """Test routine A"""
        print "FooTest:testA"

        # test routine B


    def testB(self):
        """Test routine B"""
        print "FooTest:testB"


if __name__ == '__main__':
    unittest.main()