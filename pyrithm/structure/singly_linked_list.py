####################################################################################################
# SinglyLinked List
# This is the default form which is a singly-linked-list.
# Implemented using two classes; one for a single element or Node and one for the linked-list data
# structure itself. The SinglyLinkedList class has a set of methods for basic operations. Nodes can
# each carry a payload of any kind of data, i.e. a single reference to any object.


class Node:
    """Node of a singly-linked list which is a single element of the linked-list structure, which is an
    ordered sequence of elements. Each node instance has two fields, obj and child. obj is an
    object of any type of data. child is a reference to the next item in the linked-list.
    """
    def __init__(self, obj, child_node=None):
        self.obj = obj  # obj can be of any data type. This is the payload/data the node contains.
        self.child = child_node  # A reference to the single child node of this node.


class SinglyLinkedList:
    """Creates a singly-linked list. An ordered sequence of elements or nodes. The constructor
    defines the head of the linked-list which is not a Node instance but is a reference to the
    first Node instance. The last node's child field is a reference to None. If the linked-list
    is empty, then the head is a reference to None.
    """
    def __init__(self):
        # The head is not a separate node, just a reference to the first node in the linked-list.
        self.head = None

    def insert_first(self, obj):
        """Insert a node with the payload obj at the start position of the linked-list, thus
        making the old list begin as a child of this new node. The head will point to this new
        first node.
        """
        if self.head is None:
            self.head = Node(obj)
        else:
            new_node = Node(obj)
            new_node.child = self.head
            # Or combining the previous two steps:  new_node = Node(obj, self.head)
            self.head = new_node

    def insert_last(self, obj):
        """Insert a node with the payload obj at the last position of the linked-list. This
        operation does no change the head or the existing nodes of the list but it does require
        traversal of the entire list in order to locate the last node so that the new node can be
        made a child of the last node. If the linked-list is empty then a new node is created and
        head is pointed to it.
        """
        new_node = Node(obj)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        
        # Locating the last node must be done by traversal.
        while current_node.child is not None:
            current_node = current_node.child

        current_node.child = new_node

    def export(self):
        """Return a standard list object consisting of a sequence of all of the payload objects
        from all of the nodes of the linked-list, in the same order as they exist in the
        linked-list.
        """
        node = self.head  # Start at first node as the entire list will be exported.
        export_list = []
        while node:
            export_list.append(node.obj)
            node = node.child  # At the last node, this will be None, thus exiting the loop.
        
        return export_list

    def _find(self, node, obj):
        """Locate the node with the matching obj payload and return the node itself if found.
        The node argument is the starting point for the search which progresses towards the
        end of the linked-list in a recursive manner. Returns False if the end of the list is
        reached before a match is found.
        """
        if node is None:
            return False
        # The == operator used in the following comparison is really an over-simplification.
        # Depending on the potential data types of obj, there are many critical factors involved
        # in making such an equivalence comparison. A more robust implementation would detect
        # or enforce specific data types for obj and handle the comparison appropriately.
        # == will not work in all cases but is fine for this illustrative implementation.
        if node.obj == obj:
            return node
        
        # Recursively call _find again, passing the child node of the current node.
        return self._find(node.child, obj)

    def delete(self, obj):
        """Delete the node with the matching obj payload. This method uses the private _find()
        method to locate the node to delete.
        """
        if self.head is None:
            raise ValueError('Cannot perform delete on an empty linked-list.')

        if self.head.obj == obj:
            self.head = self.head.child  # Effectively discards the first node.
            return

        current_node = self.head
        previous_node = None

        # See comments above in _find() about equality comparisons of obj using == or !=.
        while (current_node is not None) and (current_node.obj != obj):
            # Loop continues when the two conditions are both NOT met:
            # 1. We have not currently on the last node yet.
            # 2. We do not have a match for obj
            # Conversely, we exit the loop when we have passed the last node and arrived at None
            # or we have matched obj.
            previous_node = current_node
            current_node = current_node.child
        
        if current_node is None:  # Reached the end
            raise ValueError('The node specified for deletion could not be found.')

        previous_node.child = current_node.child  # Effectively discards the current node
        # and splices the remainder of the list up to child, even if it is None as is the
        # case when we delete the last node.

    def insert_before(self, locator_obj, obj):
        """Locate the node with the obj payload that matches locator_obj and insert a node before
        that new node with the provided payload obj.
        """
        if self.head is None:
            raise ValueError('Cannot perform insert_before on an empty linked-list.')
        
        if self.head.obj == locator_obj:
            self.insert_first(obj)  # Leverage the existing insert_first method
            return

        previous_node = None  # No node exists in this position before the actual first node.
        current_node = self.head

        # We locate the node to insert_before exactly as we did above in the delete method where
        # the comments provide some additional detail.
        while (current_node is not None) and (current_node.obj != locator_obj):
            previous_node = current_node
            current_node = current_node.child

        if current_node is not None:  # Unless we have gone past the end of the linked-list
            previous_node.child = Node(obj, current_node)
            return

        # For consistency, as we did in the delete method, if we cannot find the specified
        # locator_obj, we raise a specific error. It is best to be explicit, but conventions
        # such as returning nothing silently are OK to use as long as that behavior is done
        # consistently and makes logical sense to the user of the class such that returning
        # nothing will not be misinterpreted or be inconsistent with how other methods of
        # a class or a larger API behave. When in doubt, be explicit, whether you use special
        # return values or specific exceptions.
        # So if we arrive here in this method, it means we could not find locator_obj.
        raise ValueError('The node specified to insert_before could not be found.')

    def insert_after(self, locator_obj, obj):
        """Locate the node with the obj payload that matches locator_obj and insert a node after
        that new node with the provided payload obj.
        """
        # What is the most correct behavior when the linked-list is empty and an insert_after is
        # attempted? We will allow the insert_after to be the insertion of the first node, but
        # we could also disallow it with the following error. What is most correct is up to
        # the designer of the class to determine, especially if the most-correct behavior is
        # not logical or obvious. In this case we will allow it, so this error-check will be
        # be disabled:
        # if self.head == None:
        #     raise ValueError('Cannot perform insert_after on an empty linked-list.')

        current_node = self.head

        # Again, same method of location.
        while (current_node is not None) and (current_node.obj != locator_obj):
            current_node = current_node.child

        if current_node is not None:
            current_node.child = Node(obj, current_node.child)
        
