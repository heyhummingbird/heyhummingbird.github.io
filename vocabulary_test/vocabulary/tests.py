from django.test import TestCase

from vocabulary.models import Word

import json

class WordModelTest(TestCase):

    def test_word_default_text(self):
        word = Word()
        self.assertEqual(word.prob, "")
        self.assertEqual(word.ans, "")

    def test_saving_and_retrieving_item(self):
        word1 = Word()
        word1.prob = "elite"
        word1.ans  = "菁英"
        word1.save()

        word2 = Word()
        word2.prob = "csie"
        word2.ans  = "肥宅"
        word2.save()

        all_word = Word.objects.all()
        self.assertEqual(all_word[0], word1)
        self.assertEqual(all_word[1], word2)

class WordViewTest(TestCase):

    def test_redirect_after_post(self):
        response = self.client.generic('POST', '/data/', '{"prob":"apple", "ans":"蘋果"}')
        #self.assertEqual(response.status_code, 302)

    def test_can_post_new_a_word(self):
        self.client.generic('POST', '/data/', '{"prob":"apple", "ans":"蘋果"}')
        self.client.generic('POST', '/data/', '{"prob":"banana", "ans":"香蕉"}')
        
        self.assertEqual(Word.objects.count(), 2)

    def test_new_a_prob(self):
        self.client.generic('POST', '/data/', '{"prob":"apple", "ans":"蘋果"}')

        response = self.client.get('/new/') 
        content = response.content.decode('unicode_escape')
        data = json.loads(content)
        self.assertEqual(data['prob'], 'apple')
        self.assertEqual(data['ans'], '蘋果')

    def test_show_problem_set(self):
        self.client.generic('POST', '/data/', '{"prob":"apple", "ans":"蘋果"}')
        self.client.generic('POST', '/data/', '{"prob":"banana", "ans":"香蕉"}')
        self.client.generic('POST', '/data/', '{"prob":"rilak", "ans":"拉拉"}')

        response = self.client.get('/show/')
        html = response.content.decode('utf8')

        self.assertIn("apple: 蘋果", html)
        self.assertIn("banana: 香蕉", html)
        self.assertIn("rilak: 拉拉", html)