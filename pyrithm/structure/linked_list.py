
####################################################################################################
# Linked List - The default form which is a Singly Linked List
# Implemented using two clasees, one for a single element or Node and one for the Linked List data
# structure itself. The LinkedList class has a set of methods for basic operations. Nodes can
# each carry a payload of any kind of data, i.e. a single reference to any object.


class Node():
    """Node of a linked-list which is a single element of the linked-list structure, which is an
    ordered sequence of elements. Each node instance has two fields, obj and child. obj is an
    object of any type of data. child is a reference to the next item in the linked-list.
    """
    def __init__(self, obj, child_node = None):
        self.obj = obj  # obj can be of any data type. This is the payload/data the node contains.
        self.child = child_node  # A refernce to the single child node of this node.


class LinkedList():
    """Creates a singly-linked list. An ordered sequence of elements or nodes. The constructor
    defines the head of the linked-list which is not a Node instance but is a reference to the
    first Node instance. The last node's child field is a reference to null.
    """
    def __init__(self):
        # The head is not a separate node, just a reference to the first node in the linked-list.
        self.head = None

    # def _find(self, node, obj):
    #     if Node is None:
    #         return False
    #     # TODO: The following comparison == might not always work. We should more explicitly
    #     # compare the unique identifier of the object instance of obj.
    #     # This might be better:
    #     # if node.obj.id() == obj.id()
    #     if node.obj == obj  # This must be a comparison of the unique object/instance identity
    #         return node
    #     return self._find(node.get_next(), data)
    
    def export(self):
        working_node = self.head
        export_list = []
        while working_node:
            export_list.append(working_node.obj)
            working_node = working_node.next
        
        return export_list

    def insert_first(self, obj):
        if self.head is None:
            self.head = Node(obj)
        else:
            new_node = Node(obj)
            new_node.child = self.head
            # Or combining the previous two steps:  new_node = Node(obj, self.head)
            self.head = new_node

    def insert_last(self, obj):
        new_node = Node(obj)
        working_node = self.head
        # Locating the last node must be done by traversal in the current implementation.
        while working_node.child is not None:
            working_node = working_node.child

        working_node.child = new_node

    




