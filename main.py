import os
import time
import unittest
import HTMLTestRunner

cur_path = os.path.dirname(os.path.realpath(__file__))

def run_case(reportName='reports'):
    '''
    作用：执行所有的用例，并把执行结果写入HTML测试报告中
    :param all_case:
    :param reportName:
    :return:
    '''
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_path = os.path.join(cur_path, reportName)
    print(report_path)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + 'result.html')
    suite = unittest.TestSuite()
    testcate = unittest.defaultTestLoader.discover("scripts")
    print(testcate)
    for test in testcate:
        for test_case in test:
            print(test_case)
            suite.addTest(test_case)
    # re_open= open(report_abspath,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=re_open, verbosity=2, title='外勤365web自动化测试报告', description='用例执行情况')
    # runner.run(suite)
    with open(report_abspath, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='外勤365web自动化测试报告', description='用例执行情况')
        runner.run(suite)

if __name__ == '__main__':
    run_case()
    # # unittest.TextTestRunner().run(suite)
    # now = time.strftime('%Y_%m_%d_%H_%M_%S')
    # report_path = os.path.join(cur_path, reportName)
    # if not os.path.exists(report_path): os.mkdir(report_path)
    # report_abspath = os.path.join(report_path, now + 'result.html')
    # with open(report_abspath, 'wb') as fp:
    #     runner = HTMLTestRunner(stream=fp, report_title='外勤365web自动化测试报告', descriptions='用例执行情况')
    #     runner.run(suite)
