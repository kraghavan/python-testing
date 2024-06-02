import coverage
import unittest
from unittest.mock import patch
# import sys
# sys.path.append('..')

class TestChild(unittest.TestCase):

    @patch('family.SupportResource')  # Changed this line
    def test_foo(self, mock_resource):
        mock_resource.return_value.supportresource.return_value = "mock_bar"  
        from family import Child
        child = Child()
        child.foo()
        mock_resource.return_value.use_resource.assert_called_once()
if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  # catch-all except clause
        pass

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")