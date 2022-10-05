from typing import List, Optional
from msvcrt import getch

from .extension import Extension

def input():
   pass

class Inputter:
   def __init__(
      self,
      prompt:Optional[str]=None,
      *,
      extensions:Optional[List[Extension]]=None,
      maxlength:Optional[int]=None,
      minlength:Optional[int]=None,
      placeholder:Optional[str]=None,
   ) -> None:
      
      self.prompt = prompt or ""
      self.extensions = extensions or []
      self.maxlength = maxlength or None
      self.minlength = minlength or None
      self.placeholder = placeholder or ""

      self.input_loop = []
      self.current_values = []

   def input(
      self,
      prompt:Optional[str]=None,
      *,
      extensions:Optional[List[Extension]]=None,
      maxlength:Optional[int]=None,
      minlength:Optional[int]=None,
      placeholder:Optional[str]=None,
   ) -> str:

      prompt = prompt or self.prompt
      extensions = extensions or self.extensions
      maxlength = maxlength or self.maxlength
      minlength = minlength or self.minlength
      placeholder = placeholder or self.placeholder

      if minlength and maxlength:
         for _ in range(maxlength):
            self.input_loop.append(getch)
         for f in self.input_loop:
            if self._input_handler(f()) == -1:
               print()
               self.current_values.clear()
               break
            else:
               print("".join(self.current_values), end="", flush=True)
         
   def _input_handler(self, key:bytes):
      if key == ENTER:
         return -1
      elif key == BACKSPACE:
         self.current_values.pop()
         return
      else:
         self.current_values.append(key.decode("utf-8"))
         return

BACKSPACE = b'\x08'
ENTER = b"\r"