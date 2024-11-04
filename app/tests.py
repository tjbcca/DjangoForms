from django.test import TestCase

class TestFrontTimes(TestCase):
    def test_1(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&n=3")
        self.assertContains(response, 'ChoChoCho')
    def test_2(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&n=2")
        self.assertContains(response, 'ChoCho')
    def test_3(self):
        response = self.client.get("/warmup-2/font-times/?word=Abc&n=3")
        self.assertContains(response, 'AbcAbcAbc')
class NoTeenSum(TestCase):
    def test_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, 6)
    def test_2(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, 3)
    def test_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, 3)
class xyzThere(TestCase):
    def test_1(self):
        response = self.client.get("/string-2/xyz-there/?string=abcxyz")
        self.assertContains(response, True)
    def test_2(self):
        response = self.client.get("/string-2/xyz-there/?string=abc.xyz")
        self.assertContains(response, False)
    def test_3(self):
        response = self.client.get("/string-2/xyz-there/?string=xyz.abc")
        self.assertContains(response, True)
class CenteredAverage(TestCase):
    def test_1(self):
        response = self.client.get("/list-2/centered-average/?array=1+2+3+4+100")
        self.assertContains(response, 3)
    def test_2(self):
        response = self.client.get("/list-2/centered-average/?array=1+1+5+5+10+8+7")
        self.assertContains(response, 5)
    def test_3(self):
        response = self.client.get("/list-2/centered-average/?array=-10+-4+-2+-4+-2+0")
        self.assertContains(response, -3)