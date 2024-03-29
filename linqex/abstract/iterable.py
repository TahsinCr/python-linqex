from linqex._typing import *

from typing import Dict, List, Callable, Union as _Union, NoReturn, Optional, Tuple, Type, Generic, overload
from collections.abc import Iterable
from abc import ABCMeta, abstractmethod, abstractproperty

class AbstractEnumerable(Iterable[Tuple[_TK, _TV]], Generic[_TK, _TV], metaclass=ABCMeta):
    
    @overload # iterlist, iteritem
    def __init__(self, iterable:List[_TV]=None): ...
    @overload # iterdict
    def __init__(self, iterable:Dict[_TK,_TV]=None): ...
    @abstractmethod
    def __init__(self, iterable=None): ...

    @overload # iterlist, iteritem
    def __call__(self, iterable:List[_TV]=None): ...
    @overload # iterdict
    def __call__(self, iterable:Dict[_TK,_TV]=None): ...
    @abstractmethod
    def __call__(self, iterable=None): ...
    
    @overload # iterlist, iteritem
    def Get(self, *key:int) -> _Union["AbstractEnumerable[_TV]",_TV]: ...
    @overload # iterdict
    def Get(self, *key:_TK) -> _Union["AbstractEnumerable[_TK,_TV]",_TV]: ...
    @abstractmethod
    def Get(self, *key): ...
        
    @overload # iterlist, iteritem
    def GetKey(self, value:_TV) -> int: ...
    @overload # iterdict
    def GetKey(self, value:_TV) -> _TK: ...
    @abstractmethod
    def GetKey(self, value): ...

    @overload # iterlist, iteritem0
    def GetKeys(self) -> "AbstractEnumerable[int]": ...
    @overload # iterdict
    def GetKeys(self) -> "AbstractEnumerable[_TK]": ...
    @abstractmethod
    def GetKeys(self): ...

    @overload # iterlist, iteritem, iterdict
    def GetValues(self) -> "AbstractEnumerable[_TV]": ...   
    @abstractmethod
    def GetValues(self): ...
        
    @overload # iterlist, iteritem
    def GetItems(self) -> "AbstractEnumerable[Tuple[int,_TV]]": ...
    @overload # iterdict
    def GetItems(self) -> "AbstractEnumerable[Tuple[_TK,_TV]]": ...
    @abstractmethod
    def GetItems(self): ...

    @overload # iterlist, iteritem
    def Copy(self) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Copy(self) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Copy(self): ...



    @overload # iterlist, iteritem
    def Take(self, count:int) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Take(self, count:int) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Take(self, count): ...

    @overload # iterlist, iteritem
    def Take(self, count:int) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def TakeLast(self, count:int) -> "AbstractEnumerable[_TK,_TV]": ... 
    @abstractmethod
    def Take(self, count): ...
        
    @overload # iterlist, iteritem
    def Skip(self, count:int) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Skip(self, count:int) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Skip(self, count): ...
        
    @overload # iterlist, iteritem
    def SkipLast(self, count:int) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def SkipLast(self, count:int) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def SkipLast(self, count): ...
        
    @overload # iterlist
    def Select(self, selectFunc:Callable[[_TV],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iteritem
    def Select(self, selectFunc:Callable[[int,_TV],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iterdict
    def Select(self, 
        selectFunc:Callable[[_TK,_TV],_TFV], 
        selectFuncByKey:Callable[[_TK,_TV],_TFK]
    ) -> "AbstractEnumerable[_TFK,_TFV]": ...
    @abstractmethod
    def Select(self, selectFunc,  selectFuncByKey=...): ...  
    
    @overload # iterlist
    def Distinct(self, distinctFunc:Callable[[_TV],_TFV]) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def Distinct(self, distinctFunc:Callable[[int,_TV],_TFV]) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Distinct(self, distinctFunc:Callable[[_TK,_TV],_TFV]) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Distinct(self, distinctFunc): ...
    
    @overload # iterlist
    def Except(self, *value:_TV) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def Except(self, *value:_TV) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Except(self, *value:_TV) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Except(self, *value): ...
    
    @overload # iterlist
    def Join(self, iterable: List[_TV2], 
        innerFunc:Callable[[_TV],_TFV], 
        outerFunc:Callable[[_TV2],_TFV], 
        joinFunc:Callable[[_TV,_TV2],_TFV2],
        joinType:JoinType=JoinType.INNER
    ) -> "AbstractEnumerable[_TFV2]": ...
    @overload # iteritem
    def Join(self, iterable: List[_TV2], 
        innerFunc:Callable[[int,_TV],_TFV], 
        outerFunc:Callable[[int,_TV2],_TFV], 
        joinFunc:Callable[[int,_TV,int,_TV2],_TFV2],
        joinType:JoinType=JoinType.INNER
    ) -> "AbstractEnumerable[_TFV2]": ...
    @overload # iterdict
    def Join(self, iterable: Dict[_TK2,_TV2], 
        innerFunc:Callable[[_TK,_TV],_TFV], 
        outerFunc:Callable[[_TK2,_TV2],_TFV], 
        joinFunc:Callable[[_TK,_TV,_TK2,_TV2],_TFV2],
        joinFuncByKey:Callable[[_TK,_TV,_TK2,_TV2],_TFK2],
        joinType:JoinType=JoinType.INNER
    ) -> "AbstractEnumerable[_TFK2,_TFV2]": ...
    @abstractmethod
    def Join(self, iterable, 
        innerFunc, 
        outerFunc, 
        joinFunc,
        joinFuncByKey=...,
        joinType=...
    ): ...

    @overload # iterlist
    def OrderBy(self, orderByFunc:Callable[[_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def OrderBy(self, orderByFunc:Callable[[int,_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def OrderBy(self, orderByFunc:Callable[[_TK,_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def OrderBy(self, orderByFunc, desc=False): ...
    
    @overload # iterlist
    def ThenBy(self, orderByFunc:Callable[[_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def ThenBy(self, orderByFunc:Callable[[int,_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def ThenBy(self, orderByFunc:Callable[[_TK,_TV],_Union[Tuple[_TFV],_TFV]], desc:bool=False) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def ThenBy(self, orderByFunc, desc=False): ...

    @overload # iterlist
    def GroupBy(self, groupByFunc:Callable[[_TV],_Union[Tuple[_TFV],_TFV]]) -> "AbstractEnumerable[Tuple[_Union[Tuple[_TFV],_TFV], List[_TV]]]": ...        
    @overload # iteritem
    def GroupBy(self, groupByFunc:Callable[[int,_TV],_Union[Tuple[_TFV],_TFV]]) -> "AbstractEnumerable[Tuple[_Union[Tuple[_TFV],_TFV], List[_TV]]]": ...
    @overload # iterdict
    def GroupBy(self, groupByFunc:Callable[[_TK,_TV],_Union[Tuple[_TFV],_TFV]]) -> "AbstractEnumerable[_Union[Tuple[_TFV],_TFV], Dict[_TK,_TV]]": ...
    @abstractmethod
    def GroupBy(self, groupByFunc): ...

    @overload # iterlist, iteritem
    def Reverse(self) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def Reverse(self) -> "AbstractEnumerable[_TK,_TV]": ... 
    @abstractmethod
    def Reverse(self): ...

    @overload # iterlist
    def Zip(self, iterable:List[_TV2], zipFunc:Callable[[_TV,_TV2],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iteritem
    def Zip(self, iterable:List[_TV2], zipFunc:Callable[[int,_TV,int,_TV2],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iterdict
    def Zip(self, iterable:Dict[_TK2,_TV2], 
        zipFunc:Callable[[_TK,_TV,_TK2,_TV2],_TFV],
        zipFuncByKey:Callable[[_TK,_TV,_TK2,_TV2],_TFK]
    ) -> "AbstractEnumerable[_TFK,_TFV]": ...
    @abstractmethod
    def Zip(self, iterable, zipFunc, zipFuncByKey=...): ...


    
    @overload # iterlist
    def Where(self, conditionFunc:Callable[[_TV],bool]) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def Where(self, conditionFunc:Callable[[int,_TV],bool]) -> "AbstractEnumerable[int,_TV]": ...
    @overload # iterdict
    def Where(self, conditionFunc:Callable[[_TK,_TV],bool]) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def Where(self, conditionFunc): ...
       
    @overload # iterlist
    def OfType(self, *type:Type) -> "AbstractEnumerable[_TV]": ...
    @overload # iteritem
    def OfType(self, *type:Type) -> "AbstractEnumerable[int,_TV]": ...
    @overload # iterdict
    def OfType(self, *type:Type) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def OfType(self, *type): ...
        
    @overload # iterlist
    def First(self, conditionFunc:Callable[[_TV],bool]) -> Optional["AbstractEnumerable[_TV]"]: ...
    @overload # iteritem
    def First(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional["AbstractEnumerable[int,_TV]"]: ...
    @overload # iterdict
    def First(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional["AbstractEnumerable[_TK,_TV]"]: ...
    @abstractmethod
    def First(self, conditionFunc): ...
        
    @overload # iterlist
    def Last(self, conditionFunc:Callable[[_TV],bool]) -> Optional["AbstractEnumerable[_TV]"]: ...
    @overload # iteritem
    def Last(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional["AbstractEnumerable[int,_TV]"]: ...
    @overload # iterdict
    def Last(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional["AbstractEnumerable[_TK,_TV]"]: ...
    @overload # iterlist
    def Last(self, conditionFunc): ...
            
    @overload # iterlist
    def Single(self, conditionFunc:Callable[[_TV],bool]) -> Optional["AbstractEnumerable[_TV]"]: ...
    @overload # iteritem
    def Single(self, conditionFunc:Callable[[int,_TV],bool]) -> Optional["AbstractEnumerable[int,_TV]"]: ...
    @overload # iterdict
    def Single(self, conditionFunc:Callable[[_TK,_TV],bool]) -> Optional["AbstractEnumerable[_TK,_TV]"]: ...
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
    def Accumulate(self, accumulateFunc:Callable[[_TV,_TV],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iteritem
    def Accumulate(self, accumulateFunc:Callable[[_TV,int,_TV],_TFV]) -> "AbstractEnumerable[_TFV]": ...
    @overload # iterdict
    def Accumulate(self, accumulateFunc:Callable[[_TV,_TK,_TV],_TFV]) -> "AbstractEnumerable[_TK,_TFV]": ...
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
    @abstractproperty
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



    @overload # iterlist, iteritem, iterdict
    def Set(self): ...
    @overload # iterlist, iteritem, iterdict
    def Set(self, value:_Value): ...
    @abstractmethod
    def Set(self, value=...): ...

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
    
    @overload # iterlist, iteritem, iterdict
    def Delete(self): ...
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



    @overload # iterlist
    def Loop(self, loopFunc:Callable[[_TV],NoReturn]): ...
    @overload # iteritem
    def Loop(self, loopFunc:Callable[[int,_TV],NoReturn]): ...
    @overload # iterdict
    def Loop(self, loopFunc:Callable[[_TK,_TV],NoReturn]): ...
    @abstractmethod
    def Loop(self, loopFunc): ...



    @overload # iterlist, iteritem
    def ToKey(self) -> int: ...
    @overload # iterdict
    def ToKey(self) -> _TK: ...
    @abstractproperty
    def ToKey(self): ...
    
    @overload # iterdict, iterlist, iteritem
    def ToValue(self) -> _TV: ...
    @abstractproperty
    def ToValue(self): ...
    
    @overload # iterlist, iteritem, iterdict
    def ToList(self) -> List[_TV]: ...
    @abstractproperty
    def ToList(self): ...

    @overload # iterlist, iteritem, iterdict
    def ToItem(self) -> List[Tuple[int,_TV]]: ...
    @abstractproperty
    def ToItem(self): ...

    @overload # iterlist, iteritem
    def ToDict(self) -> Dict[int,_TV]: ...
    @overload # iterdict
    def ToDict(self) -> Dict[_TK,_TV]: ...
    @abstractproperty
    def ToDict(self): ...

    


    @overload # iterlist, iteritem, iterdict
    def IsEmpty(self) -> bool: ...
    @abstractproperty
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
    def __neg__(self) -> "AbstractEnumerable[_TV]": ...
    @overload # iterdict
    def __neg__(self) -> "AbstractEnumerable[_TK,_TV]": ...
    @abstractmethod
    def __neg__(self): ...
    
    @overload # iterlist, iteritem
    def __add__(self, iterable:List[_TV2]) -> "AbstractEnumerable[_Union[_TV,_TV2]]": ...
    @overload # iterdict
    def __add__(self, iterable:Dict[_TK2,_TV2]) -> "AbstractEnumerable[_Union[_TK,_TK2],_Union[_TV,_TV2]]": ...
    @abstractmethod
    def __add__(self, iterable): ...
        
    @overload # iterlist, iteritem
    def __iadd__(self, iterable:List[_TV2]): ...
    @overload # iterdict
    def __iadd__(self, iterable:Dict[_TK2,_TV2]): ...
    @abstractmethod
    def __iadd__(self, iterable): ...

    @overload # iterlist, iteritem
    def __sub__(self, iterable:List[_TV2]) -> "AbstractEnumerable[_Union[_TV,_TV2]]": ...    
    @overload # iterdict
    def __sub__(self, iterable:Dict[_TK2,_TV2]) -> "AbstractEnumerable[_Union[_TK,_TK2],_Union[_TV,_TV2]]": ...
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
    def __delitem__(self, key):
        self.Delete(key)



__all__ = ["ABCEnumerable"]

