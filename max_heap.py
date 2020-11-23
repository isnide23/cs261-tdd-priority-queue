# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# Ian Snyder

class MaxHeap:

   def __init__(self):
      self._data = []
      
   def _size(self):
      return len(self._data)

   def _is_empty(self):
      return len(self._data) == 0

   def _last_index(self):
      if self._is_empty():
         return -1
      else:
         return self._size() - 1

   def _value_at(self, index):
      if index >= self._size():
         raise IndexError("no index found")
      else:
         return self._data[index]

   def _left_child_index(self, parent_index):
      return 2 * parent_index + 1

   def _right_child_index(self, parent_index):
      return 2 * parent_index + 2

   def _parent_index(self, child_index):
      if child_index == 0:
         return -1
      else:
         return (child_index - 1) // 2

   def _parent(self, child_index):
      if self._is_empty() is True:
         raise IndexError("no index found")
      else:
         return self._data[self._parent_index(child_index)]

   def _left_child(self, child_index):
      if self._left_child_index(child_index) > self._size():
         return None
      else:
         return self._data[self._left_child_index(child_index)]


      
   



   

   


   

   

   

   

   

   

   

   

   

   



      
