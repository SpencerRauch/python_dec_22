#this code was generated when I was asked if you can return more than one thing in python, yes, it becomes a tuple

class Test:
    def test(self):
        print("running test func")
        return self, 2




test_instance = Test()

return_val = test_instance.test()

return_val[0].test()