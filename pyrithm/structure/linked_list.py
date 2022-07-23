####################################################################################################
# Singly-Linked List
# This is an object-oriented implementation of a singly-linked list.
# Implemented using two classes; one for a single element or node and one for the linked-list data
# structure itself. The SinglyLinkedList class has a set of methods for basic operations. Nodes can
# each carry a payload of any kind of data, i.e. a single reference to any kind of object.
#


class _NodeSinglyLinked:
    """Node of a singly-linked list which is a single element of the linked-list structure, which is an
    ordered sequence of elements. Each node instance has two fields, obj and child. obj is an
    object of any type of data. child is a reference to the next item in the linked-list.
    """
    def __init__(self, obj, child_node=None):
        self.obj = obj  # obj can be of any data type. This is the payload/data the node contains.
        self.child = child_node  # A reference to the single child node of this node, if one exists (or None).


class SinglyLinkedList:
    """Creates a singly-linked list. An ordered sequence of elements or nodes. The constructor
    defines the head of the linked-list which is not a Node instance but is a reference to the
    first Node instance. The last node's child field is a reference to None. If the linked-list
    is empty, then the head is a reference to None.
    """
    def __init__(self):
        # The head is not a separate node, just a reference to the first node in the linked-list.
        # This is all the instance is; a single attribute/field called 'head' which contains a reference
        # to the first node or None for an empty list.
        self.head = None

    def insert_first(self, obj):
        """Insert a node with the payload obj at the start position of the linked-list, thus
        making the old list begin as a child of this new node. The head will point to this new
        first node.
        """
        if self.head is None:
            self.head = _NodeSinglyLinked(obj)
        else:
            new_node = _NodeSinglyLinked(obj)
            new_node.child = self.head
            # Or combining the previous two steps:  new_node = _NodeSinglyLinked(obj, self.head)
            self.head = new_node

    def insert_last(self, obj):
        """Insert a node with the payload obj at the last position of the linked-list. This
        operation does not change the head or the existing nodes of the list but it does require
        traversal of the entire list in order to locate the last node so that the new node can be
        made a child of the last node. If the linked-list is empty then a new node is created and
        head is pointed to it.
        """
        new_node = _NodeSinglyLinked(obj)

        if self.head is None:
            self.head = new_node
            return

        # Prepare for traversal
        current_node = self.head
        
        # Locating the last node must be done by traversal.
        # NOTE: It is interesting how simple this traversal code is. Think through what it is doing. It is recursing
        # down the list of references to nodes, starting at head, repeating for each child until it finds 'None'.
        # We know this 'recursion' will end eventually and we can use this coding style because of the nature of our
        # data structure as we have defined it. This LOOKS a bit like recursive traversal, but because there is no
        # function call or stack involved, I personally tend not to call it recursion, although it does resemble that.
        # TODO: Research this a little. Folks might call this a simple form of recursion or the
        #   actual definition of recursion might require function calls and a stack.
        #   I'm really not sure and I like terminology and semantics to be accurate.
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
          NOTE: This private _find() method is not currently used in this class but is included for illustration.
          This method is not very useful for singly-linked lists because for many practical operations
          you do need to know which node is the parent node or the previous node etc. So this shows
          that doubly-linked lists are often more useful since each node knows its parent, or one might
          also say that this _find() needs some additional features to actually be useful within this class.
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
        """Delete the node with the matching obj payload.
        """
        if self.head is None:
            raise ValueError('Cannot perform delete on an empty linked-list.')

        if self.head.obj == obj:
            self.head = self.head.child  # Effectively discards the first node.
            return

        # Prepare for traversal
        previous_node = None
        current_node = self.head

        # See comments above in _find() about equality comparisons of obj using == or !=.
        while (current_node is not None) and (current_node.obj != obj):
            # Loop continues when the two conditions are both NOT met:
            # 1. We have not currently on the last node yet.
            # 2. We do not have a match for obj
            # Conversely, we exit the loop when we have passed the last node and arrived at None
            # or we have matched obj.
            previous_node = current_node  # This changes during this loop but is not conditional for our loop
            current_node = current_node.child  # This changes our while condition so we might exit the while now.
            # The whole point of this loop is what values for previous_node and current_node
            # we are left with when we exit the loop.
        
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

        # Prepare for traversal
        previous_node = None  # No node exists in this position before the actual first node.
        current_node = self.head

        # We locate the node to insert_before exactly as we did above in the delete method where
        # the comments provide some additional detail.
        while (current_node is not None) and (current_node.obj != locator_obj):
            previous_node = current_node
            current_node = current_node.child

        if current_node is not None:  # Unless we have gone past the end of the linked-list
            previous_node.child = _NodeSinglyLinked(obj, current_node)
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

        # Prepare for traversal
        current_node = self.head

        # Again, same method of location.
        while (current_node is not None) and (current_node.obj != locator_obj):
            current_node = current_node.child

        if current_node is not None:
            current_node.child = _NodeSinglyLinked(obj, current_node.child)


####################################################################################################
# Doubly-Linked List
# This is an object-oriented implementation of a doubly-linked list.
# Implemented using two classes; one for a single element or node and one for the linked-list data
# structure itself. The DoublyLinkedList class has a set of methods for basic operations. Nodes can
# each carry a payload of any kind of data, i.e. a single reference to any kind of object.
#


class _NodeDoublyLinked:
    """Node of a doubly-linked list which is a single element of the linked-list structure, which is an
    ordered sequence of elements. Each node instance has three fields, obj, parent and child. obj is an
    object of any type of data. parent is a reference to the previous item in the linked-list.
    child is a reference to the next item in the linked-list. the first node will always have a parent
    value of None. the last node will always have a child value of None.
    """
    def __init__(self, obj, parent_node=None, child_node=None):
        self.obj = obj  # obj can be of any data type. This is the payload/data the node contains.
        self.parent = parent_node  # A reference to the single parent node of this node, if one exists (or None).
        self.child = child_node  # A reference to the single child node of this node, if one exists (or None).


class DoublyLinkedList:
    """Creates a doubly-linked list. An ordered sequence of elements or nodes. The constructor
    defines the head of the linked-list which is not a node instance but is a reference to the
    first node instance. The last node's child field is a reference to None. The first node's parent
    field is a reference to None. Each Node contains two attributes in its node class (_NodeDoublyLinked)
    of parent and child which contain references to these respective nodes as defined. Each node also has
    an object attribute which contains a reference to the data/payload of that node. If the linked-list
    is empty, then the head is a reference to None.
    """
    def __init__(self):
        # The head is not a separate node, just a reference to the first node in the linked-list.
        # This is all the instance is; a single attribute/field called 'head' which contains a reference
        # to the first node or None for an empty list.
        self.head = None

    def insert_first(self, obj):
        """Insert a node with the payload obj at the start position of the linked-list, thus
        making the old list begin as a child of this new node. The head will point to this new
        first node. The original first node will have it's parent attribute changed from None
        to be the new first node which will itself then have a parent attribute of None.
        """
        if self.head is None:
            # This node constructor give us a parent and child of None by default, which is what is required here.
            self.head = _NodeDoublyLinked(obj)
        else:
            new_node = _NodeDoublyLinked(obj)
            # We need de-reference and save the prior first node so that we can fix its parent before moving it
            # down the list and also, this makes the code easier to understand.
            prior_first_node = self.head  # De-reference and save this.
            prior_first_node.parent = new_node  # Fix the parent value to be correct for the new position.
            new_node.child = prior_first_node  # Fix the child value for the new node to be the prior first node.
            self.head = new_node  # Make this doubly-linked list's instance's head point to the new first node.

    def insert_last(self, obj):
        """Insert a node with the payload obj at the last position of the linked-list. This
        operation does not change the head or the existing nodes of the list but it does require
        traversal of the entire list in order to locate the last node so that the new node can be
        made a child of the last node. If the linked-list is empty then a new node is created and
        head is pointed to it.
        """
        new_node = _NodeDoublyLinked(obj)

        if self.head is None:
            self.head = new_node
            # By default this new node will have None for both parent and child attributes. These are the defaults
            # from the _NodeDoublyLinked class constructor, but they are also the correct values for this new node here.
            return

        # Prepare for traversal
        current_node = self.head

        while current_node.child is not None:
            current_node = current_node.child

        new_node.parent = current_node  # Fix the new node's parent to be the current (last) node.
        # None is already the value of new_node.child because of the _NodeDoublyLinked constructor defaults.
        current_node.child = new_node  # Now link the new node as the child of the current, thus making a new last node.

    def export(self):
        """Return a standard list object consisting of a sequence of all of the payload objects
        from all of the nodes of the linked-list, in the same order as they exist in the
        linked-list.
        """
        current_node = self.head  # Start at first node as the entire list will be exported.
        export_list = []
        while current_node:
            export_list.append(current_node.obj)
            current_node = current_node.child  # At the last node, this will be None, thus exiting the loop.

        return export_list

    def dump(self):
        # TODO: Make dump return a chunk of text. It should not be printing itself. The caller should handle output.
        """Iterate over the nodes of the doubly-linked list and display the contents, including the references in the
        parent and child attributes so that it is possible to validate correct parent and child reference setting
        and reference fixing for operations like delete and others. This is a deeper debug output to show references.
        """
        print(f"CURRENT INSTANCE of DoublyLinkedList: self: \n{self.__dict__}\n")
        current_node = self.head  # Start at first node as the entire list will be dumped.
        node_counter = 0
        while current_node:
            print(f"CURRENT NODE INDEX: {node_counter}")
            print(f"CURRENT NODE ADDRESS/ID (hex): {hex(id(current_node))}")
            # print(f"CURRENT NODE ADDRESS/ID (decimal): {id(current_node)}")
            if current_node.parent is not None:
                print(f"CURRENT NODE PARENT ID (hex): {current_node.parent}")
            else:
                print(f"CURRENT NODE PARENT: None")

            if current_node.obj is not None:
                print(f"CURRENT NODE DATA/PAYLOAD: {current_node.obj}")
            else:
                print(f"CURRENT NODE DATA/PAYLOAD: None")

            if current_node.child is not None:
                print(f"CURRENT NODE CHILD ID (hex): {current_node.child}")
            else:
                print(f"CURRENT NODE CHILD: None")

            print()

            current_node = current_node.child  # At the last node, this will be None, thus exiting the loop.
            node_counter += 1

    def _find(self, node, obj):
        """Locate the node with the matching obj payload and return the node itself if found.
        The node argument is the starting point for the search which progresses towards the
        end of the linked-list in a recursive manner. Returns False if the end of the list is
        reached before a match is found.
          NOTE: This private _find() method is not currently used in this class but is included for illustration.
          Since this method is for doubly-linked lists, it might be more useful to the class methods, sice nodes
          know about their parents as well as their children and this makes finding a node a more useful thing
          for a special private function, because we have to maintain this info separatly if the node cannot
          provide it and then such a find function would really only make code more confusing and not better;
          referring to the singly-linked list case. We might consider putting it to use in this doubly-linked
          class, but again it is here for illustrative purposes primarily.
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

        # TODO: Since we have the parent attributes we can implement a reverse find, which might be a great
        #         illustration and in-fact we might want to implement other things that operate in reverse because
        #         that is essentially the big power boost that the 'double' aspect of 'doubly-linked' gives you.

        # Recursively call _find again, passing the child node of the current node.
        return self._find(node.child, obj)

    def delete(self, obj):
        """Delete the node with the matching obj payload.
        """
        if self.head is None:
            raise ValueError('Cannot perform delete on an empty linked-list.')

        if self.head.obj == obj:
            # Before discarding the first node, we will need to fix the parent attribute of the second node by making
            # its parent attribute None, then we can put it into place. This takes two steps since we have to first
            # de-reference that current first node's child out of head.
            new_first_node = self.head.child
            new_first_node.parent = None
            self.head = new_first_node  # Effectively discards the first node.
            return

        # Prepare for traversal
        previous_node = None
        current_node = self.head

        # See comments above in DoublyLinkedList._find() about equality comparisons of obj using == or !=.
        while (current_node is not None) and (current_node.obj != obj):
            previous_node = current_node
            current_node = current_node.child

        if current_node is None:  # Reached the end
            raise ValueError('The node specified for deletion could not be found.')

        # We are going to pull the list up to re-connect after we cut out the delete target, but first we need to
        # fix the parent the lower end of the list will reconnect to. With doubly-linked lists, you have to fix two
        # references for some operations, whereas with a singly-linked list, you only have to fix one reference.
        # NOTE: The wording of these variable names is with respect to the node being deleted and its position.
        #         It is current_node which is being deleted.
        #
        new_child_of_previous_node = current_node.child  # Effective delete. Splices the bottom part back up.
        # NOTE: This could be None if we are trying to delete the last Node, so we need special handling for that
        #         case in one of our following steps, in which we try to reference an attribute of a node instance,
        #         because at the last node, that child is not an instance with attributes; it is just None.
        #
        new_parent_of_current_node_child = previous_node  # De-references and clarifies as preparation for next step.
        #
        # This is where we need special handling since we can't fix a parent in the case of the last node's child
        # attribute which is None. None has no parent attribute to fix so we cannot attempt that (i.e. reference it.)
        if new_child_of_previous_node is not None:
            new_child_of_previous_node.parent = new_parent_of_current_node_child
        # If it is None, we just leave it that way and it will become the new end of list indicator in the next step.

        # This can all be done is fewer steps and without verbose variables, but is gained? More room for confusion
        # and bugs. Being very explicit and clear like I have done here has negligible cost on resources in almost
        # all contexts yet it greatly clarifies exactly what is happening and breaks things up in steps that are
        # easily coded and understood and can therefore more easily be made to be correct. Another very important
        # benefit, is this code is now easy for the NEXT programmer to understand and work with correctly.

        # Now we complete the 3 preceding splicing/deleting and fixing steps.
        previous_node.child = new_child_of_previous_node

    def insert_before(self, locator_obj, obj):
        """Locate the node with the obj payload that matches locator_obj and insert a node before
        that new node with the provided payload obj. If this occurs between existing nodes, fix the
        references for child and parent in the two nodes around the insertion point. If a new first
        node is inserted or last node is appended, assign None to the correct child/parent and adjust
        head if it is a new first node and fix affected child or parent.
        (Actually, insert_first() is leveraged.) Error if this is an empty list
        or the locator object cannot be found.
        """
        if self.head is None:
            raise ValueError('Cannot perform insert_before on an empty linked-list.')

        # TODO: We do test insert_first() in an example but this pathway deserves its own test.
        #         As time allows, it will be good to add a full suite of unit tests, which is an
        #         upcoming project for all of Pyrithm. I want to get some more algorithms and
        #         structures in place before going full throttle with a test harness and thorough
        #         unit test suites because that is a pretty massive topic and deserves the very
        #         best treatment. Top-notch unit-testing and other testing is very important
        #         in this industry and as a core skill for leading professional developers.
        if self.head.obj == locator_obj:
            self.insert_first(obj)  # Leverage the existing insert_first method
            return

        # Prepare for traversal
        previous_node = None  # No node exists in this position before the actual first node.
        current_node = self.head

        # We locate the node to insert_before exactly as we did above in the delete method where
        # the comments provide some additional detail.
        while (current_node is not None) and (current_node.obj != locator_obj):
            previous_node = current_node
            current_node = current_node.child

        if current_node is not None:  # Unless we have gone past the end of the linked-list
            # The new node is instantiated with the links correct for this insert_before().
            new_node = _NodeDoublyLinked(obj,
                                         parent_node=previous_node,
                                         child_node=current_node)
            previous_node.child = new_node  # This is the insert but one link fix remains.

            # Now also fix the parent link of the current/found node.
            current_node.parent = new_node
            return

        # If we arrive here in this method, it means we could not find locator_obj.
        raise ValueError('The node specified to insert_before could not be found.')

