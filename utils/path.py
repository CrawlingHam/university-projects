from typing import Callable, TypeVar, Union
from sys import path as sys_path
from os import path

T = TypeVar('T')

def with_path(current_dir: str, relative_path: Union[str, tuple[str, ...]], fn: Callable[[], T]) -> T:
    if isinstance(relative_path, tuple):
        target_path = path.join(current_dir, *relative_path)
    else:
        target_path = path.join(current_dir, relative_path)
    
    abs_path = path.abspath(target_path)
    sys_path.insert(0, abs_path)
    
    try:
        return fn()
    finally:
        try:
            sys_path.remove(abs_path)
        except ValueError:
            pass
