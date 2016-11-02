import unittest
from attribute_injection import MinimalClass


class TestMinimalClass(unittest.TestCase):

    __uut = None

    def setUp(self):
        self.__uut = MinimalClass()

    def test_get_the_list_fails_when_it_doesnt_exist(self):
        try:
            theList = self.__uut.theList
        except Exception as ex:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    @unittest.expectedFailure
    def test_get_the_list_fails_when_it_doesnt_exist_at_expectedFailure(self):
        theList = self.__uut.theList

    def test_get_the_list(self):
        # inject the list attribute into __uut
        self.__uut.__dict__.__setitem__("theList", list())
        theList = self.__uut.theList
        self.assertIsNotNone(theList)

    def test_get_the_list_checking_content(self):
        # inject the list into __uut
        self.__uut.__dict__.__setitem__("theList", list('listItem'))
        theList = self.__uut.theList
        item = theList[0]
        self.assertEqual('l',item)

    def test_alternate_creation_of_attribute(self):
        self.__uut.theList = list('ListItems')
        aList = self.__uut.theList
        self.assertIsNotNone(aList)
        self.assertEqual('I', aList[4])



