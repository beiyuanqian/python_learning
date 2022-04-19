from selenium import webdriver
from cfg import *
import time

class WebOpLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def open_browser(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)

    def close_browser(self):
        self.wd.quit()

    def teacher_login(self,username,password):
        self.wd.get(g_teacher_login_url)
        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        self.wd.find_element_by_id('topbar')


    def get_teacher_homepage_info(self):
        self.wd.find_element_by_css_selector('a[href="#/home"] > li').click()

        self.wd.find_element_by_id('home_div')

        time.sleep(2)

        eles = self.wd.find_elements_by_css_selector('#home_div .ng-binding')
        return [ele.text for ele in eles]





    def get_teacher_class_students_info(self):
        self.wd.find_element_by_css_selector('.main-menu >ul> li:nth-of-type(4)').click()

        self.wd.find_element_by_css_selector('a[href="#/student_group"] span').click()

        time.sleep(2)

        classes = self.wd.find_elements_by_css_selector('div.panel')

        if not classes:
            return {}

        classStudentTab = {}

        for cla in classes:
            gradeclass = cla.find_element_by_class_name('panel-heading').text.replace(' ','')

            cla.click()

            time.sleep(2)

            self.wd.implicitly_wait(1)
            nameEles = cla.find_elements_by_css_selector('tr > td:nth-child(2)')
            self.wd.implicitly_wait(10)

            names = [nameEle.text for nameEle in nameEles]

            classStudentTab[gradeclass]=names

        return classStudentTab



    def student_login(self):
        pass

    def get_student_homepage_info(self):
        pass

    def get_student_wrongquestions(self):
        pass