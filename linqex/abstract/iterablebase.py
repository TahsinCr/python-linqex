from linqex._typing import *

from typing import Dict, List, Callable, Union as _Union, NoReturn, Optional, Tuple, Type, Generic, overload
from collections.abc import Iterable
from abc import ABCMeta, abstractmethod

class AbstractEnumerableBase(Iterable[Tuple[_TK, _TV]], Generic[_TK, _TV], metaclass=ABCMeta):
    
    @overload # iterlist, iteritem
    def __init__(self, iterable:Optional[List[_TV]]=None): ...
    @overload # iterdict
    def __init__(self, iterable:Optional[Dict[_TK,_TV]]=None): ...
    @abstractmethod
    def __init__(self, iterable=None): ...
    
    @overload # iterlist, iteritem
    def Get(self, *key:int) -> _Union[List[_TV],_TV]: ...
    @overload # iterdict
    def Get(self, *key:_TK) -> _Union[Dict[_TK,_TV],_TV]: ...
    @abstractmethod
    def Get(self, *key): ...
        
    @overload # iterlist, iteritem
    def GetKey(self, value:_TV) -> int: ...
    @overload # iterdict
    def GetKey(self, value:_TV) -> _TK: ...
    @abstractmethod
    def GetKey(self, value): ...

    @overload # iterlist, iteritem
    def GetKeys(self) -> List[int]: ...
    @overload # iterdict
    def GetKeys(self) -> List[_TK]: ...
    @abstractmethod
    def GetKeys(self): ...

    @overload # iterlist, iteritem, iterdict
    def GetValues(self) -> List[_TV]: ...   
    @abstractmethod
    def GetValues(self): ...
        
    @overload # iterlist, iteritem
    def GetItems(self) -> List[Tuple[int,_TV]]: ...
    @overload # iterdict
    def GetItems(self) -> List[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def GetItems(self): ...

    @overload # iterlist, iteritem
    def Copy(self) -> List[_TV]: ...
    @overload # iterdict
    def Copy(self) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def Copy(self): ...



    @overload # iterlist, iteritem
    def Take(self, count:int) -> List[_TV]: ...
    @overload # iterdict
    def Take(self, count:int) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def Take(self, count): ...

    @overload # iterlist, iteritem
    def Take(self, count:int) -> List[_TV]: ...
    @overload # iterdict
    def TakeLast(self, count:int) -> Dict[_TK,_TV]: ... 
    @abstractmethod
    def Take(self, count): ...
        
    @overload # iterlist, iteritem
    def Skip(self, count:int) -> List[_TV]: ...
    @overload # iterdict
    def Skip(self, count:int) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def Skip(self, count): ...
        
    @overload # iterlist, iteritem
    def SkipLast(self, count:int) -> List[_TV]: ...
    @overload # iterdict
    def SkipLast(self, count:int) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def SkipLast(self, count): ...
        
    @overload # iterlist
    def Select(self, selectFunc:Callable[[_TV],_TFV]) -> List[_TFV]: ...
    @overload # iteritem
    def Select(self, selectFunc:Callable[[int,_TV],_TFV]) -> List[_TFV]: ...
    @overload # iterdict
    def Select(self, 
        selectFunc:Callable[[_TK,_TV],_TFV], 
        selectFuncByKey:Callable[[_TK,_TV],_TFK]
    ) -> Dict[_TFK,_TFV]: ...
    @abstractmethod
    def Select(self, selectFunc,  selectFuncByKey=...): ...  
    
    @overload # iterlist
    def Distinct(self, distinctFunc:Callable[[_TV],_TFV]) -> List[_TV]: ...
    @overload # iteritem
    def Distinct(self, distinctFunc:Callable[[int,_TV],_TFV]) -> List[_TV]: ...
    @overload # iterdict
    def Distinct(self, distinctFunc:Callable[[_TK,_TV],_TFV]) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def Distinct(self, distinctFunc): ...
    
    @overload # iterlist
    def Except(self, *value:_TV) -> List[_TV]: ...
    @overload # iteritem
    def Except(self, *value:_TV) -> List[_TV]: ...
    @overload # iterdict
    def Except(self, *value:_TV) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def Except(self, *value): ...
    
    @overload # iterlist
    def Join(self, iterable: List[_TV2], 
        innerFunc:Callable[[_TV],_TFV], 
        outerFunc:Callable[[_TV2],_TFV], 
        joinFunc:Callable[[_TV,_TV2],_TFV2],
        joinType:JoinType=JoinType.INNER
    ) -> List[_TFV2]: ...
    @overload # iteritem
    def Join(self, iterable: List[_TV2], 
        innerFunc:Callable[[int,_TV],_TFV], 
        outerFunc:Callable[[int,_TV2],_TFV], 
        joinFunc:Callable[[int,_TV,int,_TV2],_TFV2],
        joinType:JoinType=JoinType.INNER
    ) -> List[_TFV2]: ...
    @overload # iterdict
    def Join(self, iterable: Dict[_TK2,_TV2], 
        innerFunc:Callable[[_TK,_TV],_TFV], 
        outerFunc:Callable[[_TK2,_TV2],_TFV], 
        joinFunc:Callable[[_TK,_TV,_TK2,_TV2],_TFV2],
        joinFuncByKey:Callable[[_TK,_TV,_TK2,_TV2],_TFK2],
        joinType:JoinType=JoinType.INNER
    ) -> Dict[_TFK2,_TFV2]: ...
    @abstractmethod
    def Join(self, iterable, 
        innerFunc, 
        outerFunc, 
        joinFunc,
        joinFuncByKey=...,
        joinType=...
    ): ...

    @overload # iterlist
    def OrderBy(self, *orderByFunc:Tuple[Callable[[_TV],_Union[Tuple[_TFV],_TFV]],_Desc]) -> List[_TV]: ...
    @overload # iteritem
    def OrderBy(self, *orderByFunc:Tuple[Callable[[int,_TV],_Union[Tuple[_TFV],_TFV]],_Desc]) -> List[_TV]: ...
    @overload # iterdict
    def OrderBy(self, *orderByFunc:Tuple[Callable[[_TK,_TV],_Union[Tuple[_TFV],_TFV]],_Desc]) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def OrderBy(self, *orderByFunc): ...
    
    @overload # iterlist
    def GroupBy(self, groupByFunc:Callable[[_TV],_Union[Tuple[_TFV],_TFV]]) -> List[Tuple[_Union[Tuple[_TFV],_TFV], List[_TV]]]: ...        
    @overload # iteritem
    def GroupBy(self, groupByFunc:Callable[[int,_TV],_Union[Tuple[_TFV],_TFV]]) -> List[Tuple[_Union[Tuple[_TFV],_TFV], List[_TV]]]: ...
    @overload # iterdict
    def GroupBy(self, groupByFunc:Callable[[_TK,_TV],_Union[Tuple[_TFV],_TFV]]) -> Dict[_Union[Tuple[_TFV],_TFV], Dict[_TK,_TV]]: ...
    @abstractmethod
    def GroupBy(self, groupByFunc): ...

    @overload # iterlist, iteritem
    def Reverse(self) -> List[_TV]: ...
    @overload # iterdict
    def Reverse(self) -> Dict[_TK,_TV]: ... 
    @abstractmethod
    def Reverse(self): ...

    @overload # iterlist
    def Zip(self, iterable:List[_TV2], zipFunc:Callable[[_TV,_TV2],_TFV]) -> List[_TFV]: ...
    @overload # iteritem
    def Zip(self, iterable:List[_TV2], zipFunc:Callable[[int,_TV,int,_TV2],_TFV]) -> List[_TFV]: ...
    @overload # iterdict
    def Zip(self, iterable:Dict[_TK2,_TV2], 
        zipFunc:Callable[[_TK,_TV,_TK2,_TV2],_TFV],
        zipFuncByKey:Callable[[_TK,_TV,_TK2,_TV2],_TFK]
    ) -> Dict[_TFK,_TFV]: ...
    @abstractmethod
    def Zip(self, iterable, zipFunc, zipFuncByKey=...): ...


    
    @overload # iterlist
    def Where(self, conditionFunc:Callable[[_TV],bool]) -> List[Tuple[int,_TV]]: ...
    @overload # iteritem
    def Where(self, conditionFunc:Callable[[int,_TV],bool]) -> List[Tuple[int,_TV]]: ...
    @overload # iterdict
    def Where(self, conditionFunc:Callable[[_TK,_TV],bool]) -> List[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def Where(self, conditionFunc): ...
       
    @overload # iterlist, iteritem
    def OfType(self, *type:Type) -> List[Tuple[int,_TV]]: ...
    @overload # iterdict
    def OfType(self, *type:Type) -> List[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def OfType(self, *type): ...
        
    @overload # iterlist
    def First(self, conditionFunc:Callable[[_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iteritem
    def First(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iterdict
    def First(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def First(self, conditionFunc): ...
        
    @overload # iterlist
    def Last(self, conditionFunc:Callable[[_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iteritem
    def Last(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iterdict
    def Last(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional[Tuple[_TK,_TV]]: ...
    @overload # iterlist
    def Last(self, conditionFunc): ...
            
    @overload # iterlist
    def Single(self, conditionFunc:Callable[[_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iteritem
    def Single(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional[Tuple[int,_TV]]: ...
    @overload # iterdict
    def Single(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def Single(self, conditionFunc): ...


    
    @overload # iterlist
    def Any(self, conditionFunc:Callable[[_TV],bool]) -> bool: ...
    @overload # iteritem
    def Any(self, conditionFunc:Callable[[int,_TV],bool]) -> bool: ...
    @overload # iterdict
    def Any(self, conditionFunc:Callable[[_TK,_TV],bool]) -> bool: ...
    @abstractmethod
    def Any(self, conditionFunc): ...
        
    @overload # iterlist
    def All(self, conditionFunc:Callable[[_TV],bool]) -> bool: ...
    @overload # iteritem
    def All(self, conditionFunc:Callable[[int,_TV],bool]) -> bool: ...
    @overload # iterdict
    def All(self, conditionFunc:Callable[[_TK,_TV],bool]) -> bool: ...
    @abstractmethod
    def All(self, conditionFunc): ...
    
    @overload # iterlist, iteritem
    def SequenceEqual(self, iterable:List[_TV2]) -> bool: ...
    @overload # iterdict
    def SequenceEqual(self, iterable:Dict[_TK2,_TV2]) -> bool: ...
    @abstractmethod
    def SequenceEqual(self, iterable): ...



    @overload # iterlist
    def Accumulate(self, accumulateFunc:Callable[[_TV,_TV],_TFV]) -> List[_TFV]: ...
    @overload # iteritem
    def Accumulate(self, accumulateFunc:Callable[[_TV,int,_TV],_TFV]) -> List[_TFV]: ...
    @overload # iterdict
    def Accumulate(self, accumulateFunc:Callable[[_TV,_TK,_TV],_TFV]) -> Dict[_TK,_TFV]: ...
    @abstractmethod
    def Accumulate(self, accumulateFunc): ...
    
    @overload # iterlist
    def Aggregate(self, accumulateFunc:Callable[[_TV,_TV],_TFV]) -> _TFV: ...
    @overload # iteritem
    def Aggregate(self, accumulateFunc:Callable[[_TV,int,_TV],_TFV]) -> _TFV: ...
    @overload # iterdict
    def Aggregate(self, accumulateFunc:Callable[[_TV,_TK,_TV],_TFV]) -> _TFV: ...
    @abstractmethod
    def Aggregate(self, accumulateFunc): ...



    @overload # iterlist, iteritem, iterdict
    def Count(self, value:_TV) -> int: ...
    @abstractmethod
    def Count(self, value): ...

    @overload # iterlist, iteritem, iterdict
    def Lenght(self) -> int: ...        
    @abstractmethod
    def Lenght(self): ...

    @overload # iterlist, iteritem, iterdict
    def Sum(self) -> Optional[_TV]: ... 
    @abstractmethod
    def Sum(self): ...

    @overload # iterlist, iteritem, iterdict
    def Avg(self) -> Optional[_TV]: ...     
    @abstractmethod
    def Avg(self): ...

    @overload # iterlist, iteritem, iterdict
    def Max(self) -> Optional[_TV]: ...     
    @abstractmethod
    def Max(self): ...

    @overload # iterlist, iteritem, iterdict
    def Min(self) -> Optional[_TV]: ...     
    @abstractmethod
    def Min(self): ...



    @overload # iterlist
    def Add(self, value:_Value): ...
    @overload # iteritem
    def Add(self, key:Optional[int], value:_Value): ...
    @overload # iterdict
    def Add(self, key:_Key, value:_Value): ...
    @abstractmethod
    def Add(self, value): ...
    
    @overload # iterlist, iteritem
    def Update(self, key:int, value:_Value): ...
    @overload # iterdict
    def Update(self, key:_TK, value:_Value): ...
    @abstractmethod
    def Update(self, key, value): ...
    
    @overload # iterlist, iteritem
    def Concat(self, *iterable:List[_Value]): ...
    @overload # iterdict
    def Concat(self, *iterable:Dict[_TK2,_TV2]): ...
    @abstractmethod
    def Concat(self, *iterable): ...
    
    @overload # iterlist, iteritem
    def Union(self, *iterable:List[_Value]): ...
    @overload # iterdict
    def Union(self, *iterable:Dict[_TK2,_TV2]): ...
    @abstractmethod
    def Union(self, *iterable): ...
    
    @overload # iterlist, iteritem
    def Delete(self, *key:int): ...
    @overload # iterdict
    def Delete(self, *key:_TK): ...
    @abstractmethod
    def Delete(self, *key): ...
    
    @overload # iterlist, iteritem, iterdict
    def Remove(self, *value:_TV): ...
    @abstractmethod
    def Remove(self, *value): ...
    
    @overload # iterlist, iteritem, iterdict
    def RemoveAll(self, *value:_TV): ...
    @abstractmethod
    def RemoveAll(self, *value): ...
    
    @overload # iterlist, iteritem, iterdict
    def Clear(self): ...
    @abstractmethod
    def Clear(self): ...



    @abstractmethod
    def Loop(self, loopFunc:Callable[[_TV],NoReturn]): ...
    def Loop(self, loopFunc:Callable[[int,_TV],NoReturn]): ...
    def Loop(self, loopFunc:Callable[[_TK,_TV],NoReturn]): ...
    @abstractmethod
    def Loop(self, loopFunc): ...



    @overload # iterlist, iteritem, iterdict
    def ToDict(self) -> Dict[int,_TV]: ...
    @abstractmethod
    def ToDict(self): ...
    
    @overload # iterlist, iteritem, iterdict
    def ToList(self) -> List[_TV]: ...
    @abstractmethod
    def ToList(self): ...

    @overload # iterlist, iteritem, iterdict
    def ToItem(self) -> List[Tuple[int,_TV]]: ...
    @abstractmethod
    def ToItem(self): ...


    @overload # iterlist, iteritem, iterdict
    def IsEmpty(self) -> bool: ...
    @abstractmethod
    def IsEmpty(self): ...
    
    @overload # iterlist, iteritem
    def ContainsByKey(self, *key:int) -> bool: ...
    @overload # iterdict
    def ContainsByKey(self, *key:_TK) -> bool: ...
    @abstractmethod
    def ContainsByKey(self, *key): ...
    
    @overload # iterlist, iteritem, iterdict
    def Contains(self, *value:_TV) -> bool: ...
    @abstractmethod
    def Contains(self, *value): ...



    @overload # iterlist, iteritem
    def __neg__(self) -> List[_TV]: ...
    @overload # iterdict
    def __neg__(self) -> Dict[_TK,_TV]: ...
    @abstractmethod
    def __neg__(self): ...
    
    @overload # iterlist, iteritem
    def __add__(self, iterable:List[_TV2]) -> List[_Union[_TV,_TV2]]: ...
    @overload # iterdict
    def __add__(self, iterable:Dict[_TK2,_TV2]) -> Dict[_Union[_TK,_TK2],_Union[_TV,_TV2]]: ...
    @abstractmethod
    def __add__(self, iterable): ...
        
    @overload # iterlist, iteritem
    def __iadd__(self, iterable:List[_TV2]): ...
    @overload # iterdict
    def __iadd__(self, iterable:Dict[_TK2,_TV2]): ...
    @abstractmethod
    def __iadd__(self, iterable): ...

    @overload # iterlist, iteritem
    def __sub__(self, iterable:List[_TV2]) -> List[_Union[_TV,_TV2]]: ...    
    @overload # iterdict
    def __sub__(self, iterable:Dict[_TK2,_TV2]) -> Dict[_Union[_TK,_TK2],_Union[_TV,_TV2]]: ...
    @abstractmethod
    def __sub__(self, iterable): ...
        
    @overload # iterlist, iteritem
    def __isub__(self, iterable:List[_TV2]): ...
    @overload # iterdict
    def __isub__(self, iterable:Dict[_TK2,_TV2]): ...
    @abstractmethod
    def __isub__(self, iterable): ...

    

    @overload # iterlist, iteritem
    def __eq__(self, iterable:List[_TV2]) -> bool: ...
    @overload # iterdict
    def __eq__(self, iterable:Dict[_TK2,_TV2]) -> bool: ...
    @abstractmethod
    def __eq__(self, iterable:List[_TV2]) -> bool: ...
    
    @overload # iterlist, iteritem
    def __ne__(self, iterable:List[_TV2]) -> bool: ...
    @overload # iterdict
    def __ne__(self, iterable:Dict[_TK2,_TV2]) -> bool: ...
    @abstractmethod
    def __ne__(self, iterable): ...

    @overload # iterlist, iteritem, iterdict
    def __contains__(self, value:_Value) -> bool: ... 
    @abstractmethod
    def __contains__(self, value): ...


    
    @overload # iterlist, iteritem, iterdict
    def __bool__(self) -> bool: ...
    @abstractmethod
    def __bool__(self): ...

    @overload # iterlist, iteritem, iterdict
    def __len__(self) -> int: ...    
    @abstractmethod
    def __len__(self): ...

    @overload # iterlist, iteritem, iterdict
    def __str__(self) -> str: ...
    @abstractmethod
    def __str__(self): ...


    
    @overload # iterlist
    def __iter__(self) -> Iterable[_TV]: ...
    @overload # iteritem
    def __iter__(self) -> Iterable[Tuple[int,_TV]]: ...
    @overload # iterdict
    def __iter__(self) -> Iterable[Tuple[_TK,_TV]]: ...
    @abstractmethod
    def __iter__(self): ...

    @abstractmethod # iterlist, iteritem, iterdict
    def __next__(self): ...

    @overload # iterlist, iteritem
    def __getitem__(self, key:int) -> _TV: ... 
    @overload # iterdict
    def __getitem__(self, key:_TK) -> _TV: ... 
    @abstractmethod
    def __getitem__(self, key): ...

    @overload # iterlist, iteritem
    def __setitem__(self, key:int, value:_Value): ...
    @overload # iterdict
    def __setitem__(self, key:_TK, value:_Value): ...
    @abstractmethod
    def __setitem__(self, key, value): ...
    
    @overload # iterlist, iteritem
    def __delitem__(self, key:int): ...
    @overload # iterdict
    def __delitem__(self, key:_TK): ...
    @abstractmethod
    def __delitem__(self, key): ...



__all__ = ["ABCEnumerableBase"]

