'''
Created on Sep 13, 2017

@author: dushyant.sapra
'''
from asyncio.tasks import sleep
from _hashlib import new

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def  __init__(self, root_node):
        self.root_node = root_node
    
    def insert(self, head_node, data):
        if data > head_node.data:
            if head_node.right:
                self.insert(head_node.right, data)
            else:
                head_node.right = BinaryTreeNode(data)
        else:
            if head_node.left:
                self.insert(head_node.left, data)
            else:
                head_node.left = BinaryTreeNode(data)
    
    def preorder_traversal(self, head_node):
        if head_node is None:
            return

        print(head_node.data, end=" ")

        if head_node.left:
            self.preorder_traversal(head_node.left)

        if head_node.right:
            self.preorder_traversal(head_node.right)

    def inorder_traversal(self, head_node):
        if head_node is None:
            return

        if head_node.left:
            self.inorder_traversal(head_node.left)

        print(head_node.data, end=" ")

        if head_node.right:
            self.inorder_traversal(head_node.right)

    def postorder_traversal(self, head_node):
        if head_node is None:
            return

        if head_node.left:
            self.postorder_traversal(head_node.left)

        if head_node.right:
            self.postorder_traversal(head_node.right)

        print(head_node.data, end=" ")
    
    def height(self, head_node):
        left_tree_height = 0
        right_tree_height = 0

        if head_node.left:
            left_tree_height = self.height(head_node.left)
        if head_node.right:
            right_tree_height = self.height(head_node.right)

        return (left_tree_height + 1) if left_tree_height > right_tree_height else (right_tree_height + 1)

    def get_level(self, current_node, data, current_level=1):
        if current_node.data == data:
            return current_level

        if current_node.data < data:
            if current_node.right:
                return self.get_level(current_node.right, data, current_level + 1)
            else:
                return -1
        else:
            if current_node.left:
                return self.get_level(current_node.left, data, current_level + 1)
            else:
                return -1

    def contains(self, head_node, data):
        if head_node.data == data:
            return True

        if head_node.data < data:
            if head_node.right:
                return self.contains(head_node.right, data)
            else:
                return False
        else:
            if head_node.left:
                return self.contains(head_node.left, data)
            else:
                return False

    def count_childerens(self, head_node):
        child_count = 0

        if head_node.left:
            child_count += 1
        if head_node.right:
            child_count += 1

        return child_count

    def find_left_leaf_node(self, head_node):
        if head_node.left:
            return self.find_left_leaf_node(head_node.left)
        else:
            return head_node

    def get_node_with_parent(self, head_node, parent_node, data):
        if head_node.data == data:
            return head_node, parent_node

        if head_node.data < data:
            if head_node.right:
                return self.get_node_with_parent(head_node.right, head_node, data)
            else:
                return None, None
        else:
            if head_node.left:
                return self.get_node_with_parent(head_node.left, head_node, data) 
            else:
                return None, None

    def delete(self, data):
        new_node = None
        data_node, parent_node = self.get_node_with_parent(self.root_node, None, data)
        if data_node:
            if data_node.right:
                leaf_left_node = self.find_left_leaf_node(data_node.right)
                leaf_left_node.left = data_node.left
                new_node = data_node.right 
            elif data_node.left:
                new_node = data_node.left
            else:
                new_node = None
            if parent_node:
                if parent_node.left is data_node:
                    parent_node.left = new_node
                else:
                    parent_node.right = new_node
            else:
                self.root_node = new_node
    
    def level_order_traversal_using_queue(self, head_node):
        node_list = []
        node_list.append(head_node)
       
        while len(node_list) > 0:
            current_size = len(node_list)
            while current_size > 0:
                current_node = node_list.pop(0)
                print(current_node.data, end=" ")
                current_size -= 1
               
                if current_node.left:
                    node_list.append(current_node.left)

                if current_node.right:
                    node_list.append(current_node.right)

    def level_order_traversal_using_recursion_helper(self, head_node, current_level):
        if current_level == 0:
            print(head_node.data, end=" ")

        if head_node.left:
            self.level_order_traversal_using_recursion_helper(head_node.left, current_level - 1)
        if head_node.right:
            self.level_order_traversal_using_recursion_helper(head_node.right, current_level - 1)

    def level_order_traversal_using_recursion(self, head_node):
        max_level = self.height(head_node)

        for current_level in range(max_level):
            self.level_order_traversal_using_recursion_helper(head_node, current_level)

    def inorder_traversal_using_stack(self, head_node):
        current_node = head_node

        node_stack = []
        while current_node is not None or len(node_stack) > 0:
            if current_node:
                node_stack.insert(0, current_node)
                current_node = current_node.left
            else:
                current_node = node_stack.pop(0)
                print(current_node.data, end=" ")
                current_node = current_node.right

    def post_order_traversal_using_single_stack(self, head_node):
        current_node = head_node

        node_stack = []
        while current_node is not None or len(node_stack) > 0:
            if current_node:
                if current_node.right:
                    node_stack.insert(0, current_node.right)
                    node_stack.insert(0, current_node)
                    
                    current_node = current_node.left
            else:
                current_node = node_stack.pop(0)
                probably_right_node = node_stack.pop(0)
                
    def post_order_traversal_using_two_stack(self, head_node):
        pass

if __name__ == '__main__':
    binary_tree = BinaryTree(BinaryTreeNode(20))
    binary_tree.insert(binary_tree.root_node, 40)
    binary_tree.insert(binary_tree.root_node, 50)
    binary_tree.insert(binary_tree.root_node, 30)
    binary_tree.insert(binary_tree.root_node, 8)
    binary_tree.insert(binary_tree.root_node, 15)
    binary_tree.insert(binary_tree.root_node, 18)
    binary_tree.insert(binary_tree.root_node, 19)
    binary_tree.insert(binary_tree.root_node, 3)
    binary_tree.insert(binary_tree.root_node, 1)
    binary_tree.insert(binary_tree.root_node, 5)
    binary_tree.insert(binary_tree.root_node, 13)

    print("Pre-Order Traversal : ")
    binary_tree.preorder_traversal(binary_tree.root_node)
    print("\nIn-Order Traversal : ")
    binary_tree.inorder_traversal(binary_tree.root_node)
    print("\nPost-Order Traversal : ")
    binary_tree.postorder_traversal(binary_tree.root_node)
    print("\nLevel-Order Traversal Using Queue: ")
    binary_tree.level_order_traversal_using_queue(binary_tree.root_node)
    print("\nLevel-Order Traversal Using Recursion: ")
    binary_tree.level_order_traversal_using_recursion(binary_tree.root_node)
    print("\nIn-Order Traversal Using Stack: ")
    binary_tree.inorder_traversal_using_stack(binary_tree.root_node)

    print("\nTree Height : {}".format(binary_tree.height(binary_tree.root_node)))

    value_to_check = 80
    print("\nIs {} Present : {}".format(value_to_check, binary_tree.contains(binary_tree.root_node, value_to_check)))

    get_level_for = 19
    print("\nLevel of {} is : {}".format(get_level_for, binary_tree.get_level(binary_tree.root_node, get_level_for)))

    value_to_delete = 8
    binary_tree.delete(value_to_delete)
    print("Pre-Order Traversal After Deletion of {}: ".format(value_to_delete))
    binary_tree.preorder_traversal(binary_tree.root_node)
