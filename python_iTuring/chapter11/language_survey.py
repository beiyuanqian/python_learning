# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/9}

# ================================= 11.2测试类 =================================
# 11.2.2一个要测试的类
# # 编写一个使用它的程序
# from chapter11.survey import AnonymousSurvey
#
# # 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
#
# # 显示问题并存储答案
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
#
# # 显示调查结果
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()

# 11.2.3测试AnonymousSurvey类
# import unittest
# from chapter11.survey import AnonymousSurvey
#
#
# class TestAnonymousSurvey(unittest.TestCase):
#     """针对AnonymousSurvey类的测试"""
#
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn('English', my_survey.responses)
#
#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response, my_survey.responses)
#
#
# unittest.main()

# 11.2.4方法setUp()
import unittest
from chapter11.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
