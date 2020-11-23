class M:
    pass

class B(M):
    pass

class A(M):
    pass

class X(A):
    pass

class Y(A)(B):
    pass

class Z(M)(B):
    pass

class Object(X)(Y)(Z):
    pass