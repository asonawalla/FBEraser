__author__ = 'azim.sonawalla@gmail.com'
from selenium import webdriver
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from time import sleep


class Eraser:
    """
    Eraser class to remove Facebook content
    Set up, log in, go to activity page, then repeat delete
    If having trouble, use scroll down method or increase wait time
    Don't forget to quit in the end
    """

    def __init__(self, email, password, wait=None):
        """
        Set up the eraser
        :return: Null
        """
        self.driver = webdriver.Firefox()
        self.email = email
        self.password = password
        self.profile_name = None            # this will end up being the facebook user name
        self.count = 0                      # counter of number of elements deleted
        if args.timeout:
            self.wait_time = wait
        else:
            self.wait_time = 1              # default timeout if no argument passed

    def quit(self):
        """
        Quit the program (close out the browser)
        :return: Null
        """
        self.driver.quit()

    def login(self):
        """
        Log in to Facebook, set profile name
        :return: Null
        """
        self.driver.get('https://www.facebook.com/login/')
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email)
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password)
        password_element.submit()

        soup = BeautifulSoup(self.driver.page_source)
        profile_link = soup.find('a', {'title': 'Profile'})
        self.profile_name = profile_link.get('href')[25:]    # link appears as http://www.facebook.com/PROFILE

    def go_to_activity_page(self):
        """
        Go to the activity page and prepare to start deleting
        :return: Null
        """
        # go to the activity page (filter by 'Your Posts')
        activity_link = 'https://www.facebook.com/' + self.profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
        self.driver.get(activity_link)
        sleep(self.wait_time)

    def scroll_down(self):
        """
        Executes JS to scroll down on page.
        Use if having trouble seeing elements
        :return:
        """
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(self.wait_time)

    def delete_element(self):
        """
        Find the first available element and delete it
        :return: Null
        """

        # click hidden from timeline so the delete button shows up
        soup = BeautifulSoup(self.driver.page_source)
        # Priority: highlights, allowed, hidden
        menu_button = soup.find('a', {'aria-label': 'Highlighted on Timeline'})
        if menu_button is None:
            menu_button = soup.find('a', {'aria-label': 'Allowed on Timeline'})
        if menu_button is None:
            menu_button = soup.find('a', {'aria-label': 'Hidden from Timeline'})
        self.driver.find_element_by_id(menu_button.get('id')).click()
        sleep(self.wait_time)

        # now that the delete button comes up, find the delete link and click
        self.driver.find_element_by_link_text('Delete').click()
        sleep(self.wait_time)

        # click the confirm button, increment counter and display success
        self.driver.find_element_by_class_name('layerConfirm').click()
        self.count += 1
        print '[+] Element Deleted (' + str(self.count) + ' in total)'
        sleep(self.wait_time)


if __name__ == '__main__':
    """
    Main section of script
    """
    # set up the command line argument parser
    parser = ArgumentParser(description='Delete your Facebook activity.  Requires Firefox')
    parser.add_argument('email', help='Facebook email login')
    parser.add_argument('password', help='Facebook password')
    parser.add_argument('--wait', help='Explicit wait time between page loads (default 1 second)')
    args = parser.parse_args()

    # execute the script
    eraser = Eraser(email=args.email, password=args.password, wait=args.wait)
    eraser.login()
    eraser.go_to_activity_page()
    while True:
        try:
            eraser.delete_element()
        except Exception, e:
            print e