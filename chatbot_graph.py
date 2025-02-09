#!/usr/bin/env python3
# coding: utf-8

from question_classifier import *
from question_parser import *
from answer_search import *

'''chatBot'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = 'Hello I am a Medical Bot Assistant. I can answer your queries by looking for them in my database(neo4j). Please state your query:'
        
        
        
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        



        res_sql = self.parser.parser_main(res_classify)




        final_answers = self.searcher.search_main(res_sql)






        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)
        



if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('user:')
        answer = handler.chat_main(question)
        print('Medical Bot:', answer)

