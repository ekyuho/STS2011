class A(object):
    def foo(self):
        print( 'A.foo()')

class B(object):
    def foo(self):
        print( 'B.foo()')

class C(A, B):
    def foo(self):
        print( 'C.foo()')
        A.foo(self)
        B.foo(self)

class D(C, A):
    def foo(self):
        print('D.foo()')
        C.foo(self)
        A.foo(self)
    

k = D()
k.foo()
