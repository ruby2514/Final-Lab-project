

# Project 506
# Here are some problem-solving challenges that can be tackled using various data structures in Python.
# Use these exercises to explore the practical application of various data structures in solving a range of problem-solving challenges.
# The goal is to implement and utilize different data structures within Python to tackle diverse problem scenarios effectively.
# This project aims to foster a deeper appreciation and proficiency in leveraging Python's data structures for effective problem-solving.




# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# 1- Use a stack to check if a given string is a palindrome.
# Problem Statement: Palindrome Checker
# Write a Python function is_palindrome() that takes a string as input and uses a stack to determine if the input string is a palindrome or not.
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# Your function should return True if the input string is a palindrome and False otherwise.
def isPalindrome(inputStr):
    charStack = []
    cleanedStr = ''.join(c.lower() for c in inputStr if c.isalpha())

    for char in cleanedStr:
        charStack.append(char)

    for char in cleanedStr:
        if char != charStack.pop():
            return False
    return True

# Example tests
print(isPalindrome("level"))  # True
print(isPalindrome("race car"))  # True
print(isPalindrome("Hello"))  # False


#Example:
"""
Input: "racecar"
Output: True


Input: "hello"
Output: False
"""


# Guidelines:


# - Implement a stack data structure using a list.
# - Ignore spaces and punctuation when checking for a palindrome.
# - Use Python's built-in string manipulation functions (such as lower(), isalpha(), etc.) as needed for preprocessing the input string.


# Test Cases: # Test your function with the following test cases:
# Input: "level"
# Expected Output: True
# Input: "A man, a plan, a canal, Panama"
# Expected Output: True
# Input: "hello"
# Expected Output: False
# Input: "Was it a car or a cat I saw?"
# Expected Output: True


# Feel free to explore different approaches and use the stack concept to validate whether a given string is a palindrome or not.








# ---------------------------------------------------------------------------------------------------------------------------
# 2- Create a queue data structure using two stacks and implement its enqueue and dequeue operations.
# Problem Statement: Implementing a Queue using Stacks
# Create a Python class QueueWithStacks that implements a queue data structure using two stacks. Implement the enqueue() and dequeue() operations for this queue.
# The enqueue() operation should add an element to the queue, and the dequeue() operation should remove and return the first element added to the queue.
# Use two stacks (stack_1 and stack_2) to simulate the queue behavior. You can use Python lists to represent the stacks.

class QueueWithStacks:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def enqueue(self, value):
        self.stackIn.append(value)

    def dequeue(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        if self.stackOut:
            return self.stackOut.pop()
        return None

# Test sequence
queue = QueueWithStacks()
for val in [5, 10, 15]:
    queue.enqueue(val)
print(queue.dequeue())  #value 5
print(queue.dequeue())  #value 10
queue.enqueue(20)
queue.enqueue(25)
print(queue.dequeue())  #value 15



#Example:
"""
queue = QueueWithStacks()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)


print(queue.dequeue())  # Output: 5
print(queue.dequeue())  # Output: 10


"""


#Guidelines:


#Implement the queue using two stacks (lists).
#For the enqueue() operation, add elements to stack_1.
#For the dequeue() operation, if stack_2 is empty, transfer elements from stack_1 to stack_2 to simulate FIFO behavior.
#Ensure that the dequeue() operation returns elements in the order they were added (FIFO).
#Test Cases: Test your implementation with the following test cases:


"""
Enqueue 3 elements: 5, 10, 15
 - Perform dequeue(). Expected Output: 5
 - Perform dequeue(). Expected Output: 10
Enqueue elements: 20, 25, 30, 35
 - Perform dequeue() twice. Expected Output: 20, 25
Enqueue elements: 'a', 'b', 'c', 'd', 'e'
 - Perform dequeue() thrice. Expected Output: 'a', 'b', 'c'


"""
# Make sure that the queue operations (enqueue() and dequeue()) follow the FIFO (First-In-First-Out) order, simulating the behavior of a queue using two stacks.










# ---------------------------------------------------------------------------------------------------------------------------
# 3- Use a dictionary to count the frequency of words in a given text.
# Problem Statement: Word Frequency Counter
# Create a Python function word_frequency_counter() that takes a text string as input and uses a dictionary to count the frequency of each word in the text.
# Your function should return a dictionary where the keys are unique words in the text, and the values are the frequencies of those words.
import re
from collections import defaultdict

def getWordFrequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    wordCountMap = defaultdict(int)

    for word in words:
        wordCountMap[word] += 1

    return dict(wordCountMap)

# Example
sampleText = "Python is a very powerful programming language. I love and enjoy coding with python"
print(getWordFrequency(sampleText))


#Example
"""
text = "This is a sample text. This text will be used to count word frequency."
result = word_frequency_counter(text)
print(result)


"""


#Expected Output
"""
{
    'This': 2,
    'is': 1,
    'a': 1,
    'sample': 1,
    'text': 2,
    'will': 1,
    'be': 1,
    'used': 1,
    'to': 1,
    'count': 1,
    'word': 1,
    'frequency': 1
}
"""
# Guidelines:
# Use a dictionary to store word frequencies.
# Split the text into words and iterate through each word.
# Update the dictionary by incrementing the count for each word encountered.




# Test Cases: Test your function with the following test cases:
# Input: "Python is a powerful programming language. Python is used in various domains."
"""
{
    'Python': 2,
    'is': 2,
    'a': 1,
    'powerful': 1,
    'programming': 1,
    'language': 1,
    'used': 1,
    'in': 1,
    'various': 1,
    'domains': 1
}
"""












# ---------------------------------------------------------------------------------------------------------------------------
# 4- Implement a function to check if a given string of parentheses is balanced using a stack.
# Problem Statement: Balanced Parentheses Checker
# Create a Python function is_balanced_parentheses() that takes a string containing only parentheses (( and )) as input and uses a stack to check if the parentheses are balanced.
# A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they occur in the correct order.
# Your function should return True if the parentheses are balanced and False otherwise.
def isBalancedParentheses(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Sample tests
print(isBalancedParentheses("((()))"))  # well-balanced parenthesis
print(isBalancedParentheses("(()"))     # Not well-balanced parenthesis


# Example:
"""
string_1 = "()((()))"
string_2 = "(()())("
print(is_balanced_parentheses(string_1))  # Output: True
print(is_balanced_parentheses(string_2))  # Output: False
"""


# Guidelines:
# Use a stack to keep track of opening parentheses.
# Iterate through the string, pushing opening parentheses onto the stack and popping the stack when encountering a closing parenthesis.
# Check for balance by ensuring that for every closing parenthesis encountered, there exists a corresponding opening parenthesis in the stack.


# Test Cases: Test your function with the following test cases:


"""
Input: "((()))()"
Expected Output: True
Input: "((())"
Expected Output: False
Input: "()()()()"
Expected Output: True
"""


# Ensure that the function accurately determines whether a given string of parentheses is balanced or not using a stack-based approach.










# ---------------------------------------------------------------------------------------------------------------------------
# 5-Implement operations such as insertion, deletion, and searching in a binary search tree.


# Problem Statement: Binary Search Tree (BST) Operations
# Create a Python class BinarySearchTree that represents a binary search tree. Implement operations such as insertion, deletion, and searching in the binary search tree.
# The class should have the following methods:


# insert(value): Inserts a new node with the given value into the binary search tree.
# delete(value): Deletes a node with the given value from the binary search tree, if present.
# search(value): Searches for a node with the given value in the binary search tree. Returns True if the value is found, False otherwise.
# Ensure that the binary search tree maintains its property where for each node:


# The left subtree of a node contains only nodes with values less than the node's value.
# The right subtree of a node contains only nodes with values greater than the node's value.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def insertRec(node, value):
            if not node:
                return TreeNode(value)
            if value < node.val:
                node.left = insertRec(node.left, value)
            else:
                node.right = insertRec(node.right, value)
            return node

        self.root = insertRec(self.root, value)

    def search(self, value):
        def searchRec(node):
            if not node:
                return False
            if node.val == value:
                return True
            return searchRec(node.left) if value < node.val else searchRec(node.right)
        return searchRec(self.root)

    def delete(self, value):
        def getMinNode(node):
            while node.left:
                node = node.left
            return node

        def deleteRec(node, value):
            if not node:
                return node
            if value < node.val:
                node.left = deleteRec(node.left, value)
            elif value > node.val:
                node.right = deleteRec(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                tempNode = getMinNode(node.right)
                node.val = tempNode.val
                node.right = deleteRec(node.right, tempNode.val)
            return node

        self.root = deleteRec(self.root, value)

# Tree test
bst = BinarySearchTree()
for num in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(num)
print(bst.search(7))   # return True
print(bst.search(20))  # return False
bst.delete(15)
print(bst.search(15))  # return False

# Example
"""
# Create an instance of the BinarySearchTree class
bst = BinarySearchTree()


# Insert values into the binary search tree
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)


# Search for values in the binary search tree
print(bst.search(7))  # Output: True
print(bst.search(11))  # Output: False


# Delete a value from the binary search tree
bst.delete(15)
print(bst.search(15))  # Output: False


"""


# Guidelines:


# Implement the BinarySearchTree class with appropriate methods to perform insertion, deletion, and searching operations.
# Ensure that after deletion, the BST property is maintained.
# Consider edge cases such as deleting nodes with no children, one child, or two children.
# For deletion, you may choose to implement any method (like replacing with the minimum value from the right subtree or the maximum value from the left subtree) for maintaining the BST property.


# Test Cases:
# Test your implementation with various scenarios including insertion, deletion, and searching for values in the binary search tree. Ensure that the operations are correctly performed while maintaining the BST property.


# ---------------------------------------------------------------------------------------------------------------------------
# 6-	Graph Traversal: Implement depth-first search (DFS) and breadth-first search (BFS) algorithms for traversing a graph.

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, fromNode, toNode):
        self.adjacencyList[fromNode].append(toNode)

    def dfs(self, startNode, visited=None):
        if visited is None:
            visited = set()
        visited.add(startNode)
        print(startNode, end=' ')
        for neighbor in self.adjacencyList[startNode]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, startNode):
        visited = set()
        queue = deque([startNode])
        visited.add(startNode)

        while queue:
            current = queue.popleft()
            print(current, end=' ')
            for neighbor in self.adjacencyList[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Creating graph and test traversal
graph = Graph()
for u, v in [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]:
    graph.addEdge(u, v)
#displaying output
print("Resultant DFS Traversal:")
graph.dfs(0)
print("\nResultant BFS Traversal:")
graph.bfs(0)





# ---------------------------------------------------------------------------------------------------------------------------
# 7- Use a set to find duplicates in an array or list efficiently.
# Problem Statement: Finding Duplicates
# Create a Python function find_duplicates() that takes a list or array as input and efficiently finds and returns a set containing all the duplicate elements present in the input list.
# Your function should utilize a set to efficiently identify and collect duplicate elements from the given list.

def findDuplicates(inputList):
    seenItems = set()
    duplicateItems = set()
#iterative statement
    for item in inputList:
        if item in seenItems:
            duplicateItems.add(item)
        else:
            seenItems.add(item)

    return duplicateItems

# Checking duplicates in a set
print('Duplicated Values in the set are:')
print(findDuplicates([1, 2, 3, 4, 2, 5, 3]))  #  digits 2, 3
print(findDuplicates(['a', 'b', 'a', 'c']))  # character 'a'



# Example
"""
arr_1 = [1, 2, 3, 4, 4, 2, 5, 6, 3]
arr_2 = ['a', 'b', 'c', 'b', 'd', 'e', 'a']


result_1 = find_duplicates(arr_1)
result_2 = find_duplicates(arr_2)


print(result_1)  # Output: {2, 3, 4}
print(result_2)  # Output: {'b', 'a'}
"""


# Guidelines:


# Iterate through the input list.
# Use a set to store elements seen so far.
# When iterating, if an element is already in the set, add it to the duplicates set.
# Test Cases: Test your function with the following test cases:
"""
Input: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
Expected Output: {1, 2, 3, 4, 5}
Input: ['x', 'y', 'z', 'x', 'y', 'x', 'z']
Expected Output: {'x', 'y', 'z'}
Input: [1, 2, 3, 4, 5]
Expected Output: set()
"""
#Ensure that the find_duplicates() function efficiently identifies and returns a set containing all the duplicate elements present in the given list without modifying the original list.




# ---------------------------------------------------------------------------------------------------------------------------
# 8- Implement a function to reverse a linked list using pointers.
# Problem Statement: Reverse a Linked List


# Create a Python function reverse_linked_list() that takes the head of a linked list as input and reverses the linked list by manipulating pointers.
# The function should return the new head of the reversed linked list.
# Each node in the linked list is represented by a class Node having value and next attributes.


# Example
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


# Reverse the linked list
reversed_head = reverse_linked_list(head)


# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
print("None")
"""


# Guidelines:


# Use three pointers to reverse the linked list: prev, current, and next_node.
# Traverse through the linked list while manipulating pointers to reverse the direction of the links.


# Test Cases: Test your function with various linked list scenarios:


# Input: 1 -> 2 -> 3 -> 4 -> 5
# Expected Output: 5 -> 4 -> 3 -> 2 -> 1
# Input: 2 -> 4 -> 6 -> 8 -> 10
# Expected Output: 10 -> 8 -> 6 -> 4 -> 2


# Ensure that the reverse_linked_list() function correctly reverses the given linked list by manipulating pointers, resulting in a reversed linked list with its head node returned.


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# These challenges cover a range of data structures—stacks, queues, dictionaries, sets, graphs, heaps, linked lists, and trees—allowing for practical application and understanding of different data structure functionalities in problem-solving scenarios.
