from linqex._typing import *
from linqex.linq.iterdict import EnumerableDict
from linqex.linq.iterlist import EnumerableList

from typing import Dict, List, Union, Generic


class Enumerable(Generic[_TK,_TV]):
    def __new__(cls, iterable:Union[List[_TV],Dict[_TK,_TV]]):
        return cls.Iterable(iterable)
    @classmethod
    def Iterable(cls, iterable:Union[List[_TV],Dict[_TK,_TV]]) -> Union[EnumerableList[_TV], EnumerableDict[_TK,_TV]]:
        if isinstance(iterable, list):
            return cls.List(iterable)
        elif isinstance(iterable, dict):
            return cls.Dict(iterable)
        else:
            raise TypeError()

    @classmethod
    def List(cls, iterlist:List[_TV]=None) -> EnumerableList[_TV]:
        if iterlist is None:
            iterlist:List[_TV]=list()
        return EnumerableList(iterlist)
    
    @staticmethod
    def Range(start:int, stop:int, step:int=1) -> "EnumerableList[int]":
        return EnumerableList.Range(start, stop, step)
    
    @staticmethod
    def Repeat(value:_Value, count:int) -> "EnumerableList[int]":
        return EnumerableList.Repeat(value, count)

    @classmethod
    def Dict(cls, iterdict:Dict[_TK,_TV]=None) -> EnumerableDict[_TK,_TV]:
        if iterdict is None:
            iterdict:Dict[_TK,_TV]=dict()
        return EnumerableDict(iterdict)


__all__ = ["Enumerable"]
