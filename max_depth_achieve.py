class A:

    def m1(self):
        return 20
class B(A):

    def m1(self):
        val = super().m1()+30
        return val

class C(B):
    """
    in this class  i should clear on what is self. sef is current object
    so they call m1 again and agin and max recursion depth reach 
    """

    def m1(self):
        val = self.m1() + 20
        return val
obj = C()
print(obj.m1())