#-----------------------------------------------------------------------
# testregoverviews.py
# Author: Arnold Jiang and Amanda Chan
#-----------------------------------------------------------------------

import sys
import time
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

    parser.add_argument(
        'delay', metavar='delay', type=int,
        help='the number of seconds that this program should delay '
            + 'between interactions with the browser')

    args = parser.parse_args()

    return (args.serverURL, args.browser, args.delay)

#-----------------------------------------------------------------------

def print_flush(message):

    print(message)
    sys.stdout.flush()

#-----------------------------------------------------------------------

def run_test(server_url, browser_process, delay, input_values):

    print_flush(UNDERLINE)
    for key, value in input_values.items():
        print_flush(key + ': |' + value + '|')

    try:
        page = browser_process.new_page()
        page.goto(server_url)

        if 'dept' in input_values:
            dept_input = page.locator('#deptInput')
            dept_input.fill(input_values['dept'])
            time.sleep(delay) # Wait for the AJAX call to finish.

        if 'coursenum' in input_values:
            coursenum_input = page.locator('#coursenumInput')
            coursenum_input.fill(input_values['coursenum'])
            time.sleep(delay) # Wait for the AJAX call to finish.

        if 'area' in input_values:
            area_input = page.locator('#areaInput')
            area_input.fill(input_values['area'])
            time.sleep(delay) # Wait for the AJAX call to finish.

        if 'title' in input_values:
            title_input = page.locator('#titleInput')
            title_input.fill(input_values['title'])
            time.sleep(delay) # Wait for the AJAX call to finish.

        overviews_table = page.locator('#overviewsTable')
        print_flush(overviews_table.inner_text())

    except Exception as ex:
        print(str(ex), file=sys.stderr)

#-----------------------------------------------------------------------

def main():

    server_url, browser, delay = get_args()

    with playwright.sync_api.sync_playwright() as pw:

        if browser == 'chrome':
            browser_process = pw.chromium.launch()
        else:
            browser_process = pw.firefox.launch()

        run_test(server_url, browser_process, delay,
            {'dept':'COS'})
        run_test(server_url, browser_process, delay,
            {'dept':'COS', 'coursenum':'2', 'area':'qr',
            'title':'intro'})

        # Add more tests here.
        # Coverage Case Testing
        run_test(server_url, browser_process, delay, {})
        run_test(server_url, browser_process, delay, {'dept':'COS'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'333'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'240'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'226'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'217'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'445'})
        run_test(server_url, browser_process, delay,
                 {'coursenum':'320'})
        run_test(server_url, browser_process, delay, {
            'coursenum':'333',
            'area':'STX'
        })
        run_test(server_url, browser_process, delay, {
            'coursenum':'342',
            'area':'QR'
        })
        run_test(server_url, browser_process, delay, {
            'dept':'CHM',
            'coursenum':'408'
        })
        run_test(server_url, browser_process, delay, {
            'area':'EM',
            'title':'Ethics',
        })
        run_test(server_url, browser_process, delay, {'coursenum':'b'})
        run_test(server_url, browser_process, delay, {'area':'QR'})
        run_test(server_url, browser_process, delay, {'title': 'intro'})
        run_test(server_url, browser_process, delay,
                 {'title': 'science'})
        run_test(server_url, browser_process, delay, {'title': 'C_S'})
        run_test(server_url, browser_process, delay, {'title': 'c%S'})
        run_test(server_url, browser_process, delay, {
            'dept': 'cos', 'coursenum': '3'
        })
        run_test(server_url, browser_process, delay, {
            'dept': 'COS',
            'area': 'qr',
            'coursenum': '2',
            'title': 'intro'
        })
        run_test(server_url, browser_process, delay, {
            'dept': 'COS',
            'area': 'ST',
            'coursenum': '233',
            'title': 'An'
        })
        run_test(server_url, browser_process, delay, {
            'dept':'COS',
            'area': 'qr',
            'coursenum': '2',
            'title': 'apple'
        })
        run_test(server_url, browser_process, delay, {
            'title': 'Independent Study'
        })
        run_test(server_url, browser_process, delay, {
            'title': 'Independent Study '
        })
        run_test(server_url, browser_process, delay, {
            'title': 'Independent Study  '
        })
        run_test(server_url, browser_process, delay, {
            'title': ' Independent Study'
        })
        run_test(server_url, browser_process, delay, {
            'title': '  Independent Study'
        })
        run_test(server_url, browser_process, delay, {
            'title': '-c'
        })

if __name__ == '__main__':
    main()
