class A:
    # def __init__(self, text):
    #     self.text = text

    def get_text(self):
        pass
        # print(self.text)

class B:

    def test(self):
        pass

class C(A, B):
    pass


c1 = C()
c1.get_text()
c1.test()