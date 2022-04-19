# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/9}

class AnonymousSurvey():
    """手机匿名调查的问卷"""

    def __init__(self, question):
        """存储一个答案，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
