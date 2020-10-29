from typing import Callable, Tuple
from functools import reduce
from types import FunctionType

def pure(f): return FunctionType(f.__code__, dict())

@pure
def idf(x): return x

def mu(*fs: Tuple[Callable]): return reduce(lambda f, g: lambda x: f(g(x)), fs, idf)
