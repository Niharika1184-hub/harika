# n = int(input())
# num_str = str(n)  
# num_digits = len(num_str)
# armstrong_sum = 0

# for digit in num_str:
#     armstrong_sum += int(digit) ** num_digits

# if armstrong_sum == n:
#     print(n, "is an Armstrong number")
# else:
#     print(n, "is not an Armstrong number")

# =================min heap=============
# def heapify(arr,n,i):
#     smallest=i
#     left=(2*i)+1
#     right=(2*i)+2
#     if left < n and arr[i]>arr[left]:
#         smallest=left
#     if right < n and arr[smallest]>arr[right]:
#        smallest=right
#     if smallest != i:
#         arr[i],arr[smallest]=arr[smallest],arr[i]
#         heapify(arr,n,smallest)
# def min_heap(arr):
#     n=len(arr)
#     for i in range(n//2,-1,-1):
#         heapify(arr,n,i)
# nums=[4,10,3,5,1]
# print("Original list:",nums)
# min_heap(nums)
# print("Min heap:",nums)

# ============product and sum============
# def product_and_sum(a,b):
#     sum=a+b
#     difference=a-b
#     product=sum*difference 
#     return product
# a=5
# b=3
# print(product_and_sum(a,b))

    
# def get_tic_tac_toe_winner(board):
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2] and row[0] != "":
#             return row[0]

#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
#             return board[0][col]

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
#         return board[0][2]

#     # If no winner, return None
#     return None

# # Example usage
# board = [["x", "x", "x"], ["0", "x", "0"], ["x", "0", "0"]]
# print(get_tic_tac_toe_winner(board))  # Output: "x"

# def count(lst):
#     dict = {}
#     for item in lst:
#         if item in dict:
#             dict[item] += 1
#         else:
#             dict[item] = 1
#     return dict

# # Example usage:
# my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(count(my_list)) 

# Queue=[]
# #enqueue
# Queue.append("1")
# Queue.append("2")
# Queue.append("3")
# Queue.append("4")
# Queue.append("5")
# print(Queue)
# #dequeue
# element=Queue.pop(0)
# print("pop element:",element)
# print(Queue)
# #peek
# top=Queue[0]
# print("Peek element:",top)
# #is empty
# empty=not bool(Queue)
# print("is empty:",empty)
# #Size
# size=len(Queue)
# print("Size:",size)

# ========bubblesort==========
# arr=[9,8,7,6,5,4,3,2,3]
# n=len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print("Sorted array:",arr)



#Selection sort:
# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         min_val=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_val]:
#                 arr[j],arr[min_val]=arr[min_val],arr[j]
# arr=[5,7,3,8,2,6,1]
# selection_sort(arr)
# print("Sorted array:",arr)

# ==========second_largest========
# def second_largest(list):
#     n=len(list)
#     l=list(set(l))
#     list.sort()
#     return(list[-2])
# list=[6,3,1,5,2]
# print(second_largest(list))

#[1,2,3,5,6] can u change  the list to set

#[1,2,3,5,6]


list1=[1,2,3,4,5]
list2=[1,2,3,7,6]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

# ===========linkedlist=============
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def add_end(head, data):
#     if head is None:
#         return Node(data)
#     current = head
#     while current.next:
#         current = current.next
#     current.next = Node(data)
#     return head

# def add_front(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node

# def printLL(head):
#     if head is None:
#         print("List is empty")
#         return
#     current = head
#     while current:
#         print(current.data, end=" --> " if current.next else "")
#         current = current.next
#     print()

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("Original List:")
# printLL(node1)

# node1 = add_end(node1, 60)
# print("Adding a node at the end:")
# printLL(node1)

# node1 = add_front(node1, 70)
# print("Adding a node at the beginning:")
# printLL(node1)

