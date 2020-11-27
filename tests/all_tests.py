import unittest
from tests.test_database import MyDatabaseTest
from tests.test_index import IndexPageTest


def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [MyDatabaseTest, IndexPageTest]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
    return results


if __name__ == '__main__':
    run_some_tests()