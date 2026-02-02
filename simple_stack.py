# simple_stack.py

class SimpleStack:
    """
    A simple stack implementation using only Python lists.
    Provides push, pop, peek operations without using built-in stack libraries.
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty stack.
        
        Args:
            max_size (int, optional): Maximum capacity of the stack. 
                                     If None, stack has unlimited capacity.
        """
        self._items = []  # Internal list to store stack items
        self._max_size = max_size
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to add to the stack.
        
        Returns:
            bool: True if successful, False if stack is full.
        
        Raises:
            OverflowError: If stack has a max size and is full.
        """
        if self.is_full():
            raise OverflowError("Cannot push to a full stack")
        
        self._items.append(item)
        return True
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        
        # Remove and return the last item
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def is_full(self):
        """
        Check if the stack is full (only relevant if max_size is set).
        
        Returns:
            bool: True if stack is full, False otherwise.
        """
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size
    
    def size(self):
        """
        Get the current number of items in the stack.
        
        Returns:
            int: Number of items in the stack.
        """
        return len(self._items)
    
    def clear(self):
        """
        Remove all items from the stack.
        """
        self._items.clear()
    
    def __str__(self):
        """
        String representation of the stack (top to bottom).
        
        Returns:
            str: String representation.
        """
        if self.is_empty():
            return "Stack: [] (empty)"
        
        # Show stack from top to bottom
        items_repr = ", ".join(str(item) for item in reversed(self._items))
        return f"Stack (top -> bottom): [{items_repr}]"
    
    def __len__(self):
        """
        Return the size of the stack.
        """
        return self.size()


# Example usage and testing
def test_stack():
    """Test function to demonstrate stack operations."""
    print("=" * 50)
    print("Simple Stack Implementation Test")
    print("=" * 50)
    
    # Create a stack
    stack = SimpleStack()
    
    # Test push operations
    print("\n1. Pushing items onto the stack:")
    test_items = [10, 20, 30, 40, 50]
    for item in test_items:
        stack.push(item)
        print(f"   Pushed: {item:3} | Stack size: {stack.size():2} | Stack: {stack}")
    
    # Test peek
    print(f"\n2. Peek at top: {stack.peek()}")
    
    # Test pop operations
    print("\n3. Popping items from the stack:")
    while not stack.is_empty():
        item = stack.pop()
        print(f"   Popped: {item:3} | Stack size: {stack.size():2} | Stack: {stack}")
    
    # Test error handling
    print("\n4. Error handling tests:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"   ✓ Correctly caught pop from empty: {e}")
    
    try:
        stack.peek()
    except IndexError as e:
        print(f"   ✓ Correctly caught peek on empty: {e}")
    
    # Test fixed size stack
    print("\n5. Fixed size stack test:")
    fixed_stack = SimpleStack(max_size=3)
    
    # Push to capacity
    for i in [100, 200, 300]:
        fixed_stack.push(i)
        print(f"   Pushed: {i} | Stack: {fixed_stack}")
    
    try:
        fixed_stack.push(400)
    except OverflowError as e:
        print(f"   ✓ Correctly caught push to full: {e}")


# Main program
if __name__ == "__main__":
    # Run the test
    test_stack()
    
    # Demonstrate practical use
    print("\n" + "=" * 50)
    print("Practical Example: Parentheses Checker")
    print("=" * 50)
    
    def check_parentheses(expression):
        """
        Check if parentheses in an expression are balanced using our SimpleStack.
        
        Args:
            expression (str): The expression to check.
        
        Returns:
            bool: True if parentheses are balanced, False otherwise.
        """
        stack = SimpleStack()
        matching_pairs = {')': '(', '}': '{', ']': '['}
        
        for i, char in enumerate(expression):
            if char in "({[":
                stack.push(char)
            elif char in ")}]":
                if stack.is_empty():
                    print(f"Error: Unmatched '{char}' at position {i}")
                    return False
                
                top_char = stack.pop()
                if top_char != matching_pairs[char]:
                    print(f"Error: Mismatched '{top_char}' and '{char}' at position {i}")
                    return False
        
        if not stack.is_empty():
            print("Error: Unmatched opening parentheses")
            return False
        
        return True
    
    # Test expressions
    test_expressions = [
        "((2+3)*[4-5])",      # Balanced
        "({[()]})",           # Balanced
        "((2+3)*[4-5]",       # Unbalanced - missing closing
        "((2+3)*[4-5]))",     # Unbalanced - extra closing
        "[{]}",               # Unbalanced - mismatched
    ]
    
    for expr in test_expressions:
        result = check_parentheses(expr)
        status = "✓ Balanced" if result else "✗ Unbalanced"
        print(f"{status}: {expr}")