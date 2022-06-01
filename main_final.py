class Node():                                           #node classi yaradiriq ve atributlari qeyd edirik
   def __init__(self,value):
       self.value = value                                    #yeni node her zaman qirmizi oldugu ucun colour 1 olur yeni qirmizi
       self.parent = None
       self.left = None
       self.right = None
       self.colour = 1            

class red_black_tree():                         #red black tree classi node classi ile oxsardir. burada ferqli artibut node dur cunki tree nodelardan ibaretdir
   def __init__(self):
       self.NULL = Node ( 0 )
       self.NULL.colour = 0
       self.NULL.left = None
       self.NULL.right = None
       self.root = self.NULL


   def insertion(self, key):
       node = Node(key)
       node.parent = None
       node.value = key
       node.left = self.NULL
       node.right = self.NULL
       node.colour = 1

       a = None
       b = self.root

       while b != self.NULL :
           a = b
           if node.value < b.value :
               b = b.left
           else :
               b = b.right

       node.parent = a
       if a == None :
           self.root = node
       elif node.value < a.value :
           a.left = node
       else :
           a.right = node

       if node.parent == None :
           node.colour = 0
           return

       if node.parent.parent == None :
           return




   def min(self, node):
       while node.left != self.NULL:
           node = node.left
       return node


   def left_rotation ( self , b ) :
       a = b.right
       b.right = a.left
       if a.left != self.NULL :
           a.left.parent = b

       a.parent = b.parent
       if b.parent == None :
           self.root = a
       elif b == b.parent.left :
           b.parent.left = a
       else :
           b.parent.right = a
       a.left = b
       b.parent = a


   def right_rotation ( self , b ) :
       a = b.left
       b.left = a.right
       if a.right != self.NULL :
           a.right.parent = b

       a.parent = b.parent
       if b.parent == None :
           self.root = a
       elif b == b.parent.right :
           b.parent.right = a
       else :
           b.parent.left = a
       a.right = b
       b.parent = a




   def __rb_transplant ( self , u , v ) :
       if u.parent == None :
           self.root = v
       elif u == u.parent.left :
           u.parent.left = v
       else :
           u.parent.right = v
       v.parent = u.parent


   def _delete_help_ ( self , node , key ) :
       c = self.NULL
       while node != self.NULL :
           if node.value == key :
               c = node

           if node.value <= key :
               node = node.right
           else :
               node = node.left

       if c == self.NULL :
           print ( "Wrong value" )
           return

       a = c
       y_original_color = a.colour
       if c.left == self.NULL :
           b = c.right
           self.__rb_transplant ( c , c.right )
       elif (c.right == self.NULL) :
           b = c.left
           self.__rb_transplant ( c , c.left )
       else :
           a = self.min ( c.right )
           y_original_color = a.colour
           b = a.right
           if a.parent == c :
               b.parent = a
           else :
               self.__rb_transplant ( a , a.right )
               a.right = c.right
               a.right.parent = a

           self.__rb_transplant ( c , a )
           a.left = c.left
           a.left.parent = a
           a.colour = c.colour
       if y_original_color == 0 :
           self.fixDelete ( b )


   def delete_node ( self , value ) :
       self._delete_help_ ( self.root , value )


   def __printCall ( self , node , indent , last ) :
       if node != self.NULL :
           print(indent, end=' ')
           if last :
               print ("R----",end= ' ')
               indent += "     "
           else :
               print("L----",end=' ')
               indent += "|    "

           s_color = "RED" if node.colour == 1 else "BLACK"
           print ( str ( node.value ) + "(" + s_color + ")" )
           self.__printCall ( node.left , indent , False )
           self.__printCall ( node.right , indent , True )

   def print_tree ( self ) :
       self.__printCall ( self.root , "" , True )


if __name__ == "__main__":
   bst = red_black_tree()

   bst.insertion(1)
   bst.insertion(25)
   bst.insertion(71)
   bst.insertion(4)
   bst.insertion(27)
   bst.insertion(8)

   bst.print_tree()

   print("\nDeletion:")
   bst.delete_node(71)
   bst.print_tree()