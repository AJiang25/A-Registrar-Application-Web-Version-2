#-----------------------------------------------------------------------
# testregdetails.py
# Author: Arnold Jiang and Amanda Chan
#-----------------------------------------------------------------------

import sys
import argparse
import playwright.sync_api

#-----------------------------------------------------------------------

MAX_LINE_LENGTH = 72
UNDERLINE = '-' * MAX_LINE_LENGTH

#-----------------------------------------------------------------------

def get_args():

    parser = argparse.ArgumentParser(
        description='Test the ability of the reg application to '
            + 'handle "primary" (class overviews) queries')

    parser.add_argument(
        'serverURL', metavar='serverURL', type=str,
        help='the URL of the reg application')

    parser.add_argument(
        'browser', metavar='browser', type=str,
        choices=['firefox', 'chrome'],
        help='the browser (firefox or chrome) that you want to use')

    args = parser.parse_args()

    return (args.serverURL, args.browser)

#-----------------------------------------------------------------------

def print_flush(message):
    print(message)
    sys.stdout.flush()

#-----------------------------------------------------------------------

def run_test(server_url, browser_process, classid):

    print_flush(UNDERLINE)

    try:
        page = browser_process.new_page()
        page.goto(server_url)

        link = page.get_by_text(classid).first
        link.click()
        
        page.wait_for_selector('#classDetailsTable')
        class_details_table = page.locator('#classDetailsTable')
        print_flush(class_details_table.inner_text())

        page.wait_for_selector('#courseDetailsTable')
        course_details_table = page.locator('#courseDetailsTable')
        print_flush(course_details_table.inner_text())

    except Exception as ex:
        print(str(ex), file=sys.stderr)

#-----------------------------------------------------------------------

def main():

    server_url, browser = get_args()

    with playwright.sync_api.sync_playwright() as pw:

        if browser == 'chrome':
            browser_process = pw.chromium.launch()
        else:
            browser_process = pw.firefox.launch()

        run_test(server_url, browser_process, '8321')

        # Add more tests here.
        # Coverage Case Testing
        run_test(server_url, browser_process, '9032')
        run_test(server_url, browser_process, '8293')
        run_test(server_url, browser_process, '9977')
        run_test(server_url, browser_process, '9012')
        run_test(server_url, browser_process, '10188')
        run_test(server_url, browser_process, '10261')
        run_test(server_url, browser_process, '10262')
        run_test(server_url, browser_process, '10263')
        run_test(server_url, browser_process, '10264')
        run_test(server_url, browser_process, '9158')
        run_test(server_url, browser_process, '9897')
        run_test(server_url, browser_process, '8390')
        run_test(server_url, browser_process, '10260')
        run_test(server_url, browser_process, '10250')
        run_test(server_url, browser_process, '9980')
        run_test(server_url, browser_process, '10244')
        run_test(server_url, browser_process, '8333')
        run_test(server_url, browser_process, '8334')

if __name__ == '__main__':
    main()
