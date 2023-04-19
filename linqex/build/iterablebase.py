from linqex._typing import *
from linqex.build.iterdictbase import EnumerableDictBase
from linqex.build.iterlistbase import EnumerableListBase

from typing import Dict, List, Union, Generic


class EnumerableBase(Generic[_TK,_TV]):
    def __new__(cls, iterable:Union[List[_TV],Dict[_TK,_TV]]):
        return cls.Iterable(iterable)
    @classmethod
    def Iterable(cls, iterable:Union[List[_TV],Dict[_TK,_TV]]) -> Union[EnumerableListBase[_TV], EnumerableDictBase[_TK,_TV]]:
        if isinstance(iterable, list):
            return cls.List(iterable)
        elif isinstance(iterable, dict):
            return cls.Dict(iterable)
        else:
            raise TypeError()

    @classmethod
    def List(cls, iterlist:List[_TV]=None) -> EnumerableListBase[_TV]:
        if iterlist is None:
            iterlist:List[_TV]=list()
        return EnumerableListBase(iterlist)
    
    @staticmethod
    def Range(start:int, stop:int, step:int=1) -> "EnumerableListBase[int]":
        return EnumerableListBase.Range(start, stop, step)
    
    @staticmethod
    def Repeat(value:_Value, count:int) -> "EnumerableListBase[int]":
        return EnumerableListBase.Repeat(value, count)

    @classmethod
    def Dict(cls, iterdict:Dict[_TK,_TV]=None) -> EnumerableDictBase[_TK,_TV]:
        if iterdict is None:
            iterdict:Dict[_TK,_TV]=dict()
        return EnumerableDictBase(iterdict)



__all__ = ["EnumerableBase"]
