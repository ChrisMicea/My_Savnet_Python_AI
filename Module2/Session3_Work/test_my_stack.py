import unittest
from my_stack import MyStack

class TestMyStack(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.stack = MyStack()
    
    def test_init_empty_stack(self):
        """Test that new stack is empty."""
        self.assertEqual(str(self.stack), "[]")
    
    def test_push_single_item(self):
        """Test pushing a single item."""
        self.stack.push(1)
        self.assertEqual(str(self.stack), "[1]")
    
    def test_push_multiple_items(self):
        """Test pushing multiple items."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(str(self.stack), "[3, 2, 1]")
    
    def test_pop_single_item(self):
        """Test popping a single item."""
        self.stack.push(1)
        result = self.stack.pop()
        self.assertEqual(result, 1)
        self.assertEqual(str(self.stack), "[]")
    
    def test_pop_multiple_items(self):
        """Test popping multiple items (LIFO order)."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        # Should pop in reverse order (LIFO)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(str(self.stack), "[2, 1]")
        
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(str(self.stack), "[1]")
        
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(str(self.stack), "[]")
    
    def test_push_and_pop_mixed(self):
        """Test mixed push and pop operations."""
        self.stack.push(1)
        self.stack.push(2)
        
        # Pop one item
        result = self.stack.pop()
        self.assertEqual(result, 2)
        self.assertEqual(str(self.stack), "[1]")
        
        # Push another item
        self.stack.push(3)
        self.assertEqual(str(self.stack), "[3, 1]")
        
        # Pop remaining items
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(str(self.stack), "[]")
    
    def test_pop_empty_stack(self):
        """Test popping from empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()
    
    def test_different_data_types(self):
        """Test stack with different data types."""
        self.stack.push("hello")
        self.stack.push(42)
        self.stack.push([1, 2, 3])
        self.stack.push({"key": "value"})
        
        self.assertEqual(self.stack.pop(), {"key": "value"})
        self.assertEqual(self.stack.pop(), [1, 2, 3])
        self.assertEqual(self.stack.pop(), 42)
        self.assertEqual(self.stack.pop(), "hello")
    
    def test_large_stack(self):
        """Test stack with many items."""
        # Push 100000 items
        for i in range(100000):
            self.stack.push(i)
        
        # Pop and verify LIFO order
        for i in range(99999, -1, -1):
            self.assertEqual(self.stack.pop(), i)
        
        # Stack should be empty
        self.assertEqual(str(self.stack), "[]")
    
    def test_string_representation_empty(self):
        """Test string representation of empty stack."""
        self.assertEqual(str(self.stack), "[]")
    
    def test_string_representation_single_item(self):
        """Test string representation with single item."""
        self.stack.push("test")
        self.assertEqual(str(self.stack), "['test']")
    
    def test_string_representation_multiple_items(self):
        """Test string representation shows LIFO order."""
        self.stack.push("first")
        self.stack.push("second")
        self.stack.push("third")
        self.assertEqual(str(self.stack), "['third', 'second', 'first']")
    
    def test_stack_is_lifo(self):
        """Test that stack follows Last-In-First-Out principle."""
        items = ["a", "b", "c", "d", "e"]
        
        # Push items
        for item in items:
            self.stack.push(item)
        
        # Pop and verify reverse order
        popped_items = []
        while str(self.stack) != "[]":
            popped_items.append(self.stack.pop())
        
        self.assertEqual(popped_items, ["e", "d", "c", "b", "a"])
    
    def test_multiple_independent_stacks(self):
        """Test that multiple stacks don't interfere with each other."""
        stack1 = MyStack()
        stack2 = MyStack()
        
        stack1.push(1)
        stack1.push(2)
        stack2.push("a")
        stack2.push("b")
        
        # Each stack should have its own data
        self.assertEqual(str(stack1), "[2, 1]")
        self.assertEqual(str(stack2), "['b', 'a']")
        
        # Operations on one stack shouldn't affect the other
        stack1.pop()
        self.assertEqual(str(stack1), "[1]")
        self.assertEqual(str(stack2), "['b', 'a']")

if __name__ == '__main__':
    unittest.main()
