import sys
import os
import re
import sys

Percentage = 0
Parsed = 0
NumberOfFiles =0

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

class Node:
    def __init__(self,key):
        self.key = key
        self.documents = []
        self.frequency = 0
        self.right = None
        self.left = None
def TreeSearch(root,search):

    if  root is None or root.key == search :
        return root
    if root.key < search :
        return TreeSearch(root.right,search)
    if root.key > search :
        return TreeSearch(root.left,search)

def insertTree(root, child, document):
    if (root.key > child.key):
        if (root.left == None):
            root.left = child
            child.documents.append(document)
        else:
            insertTree(root.left,child,document)
    elif (root.key < child.key):
        if (root.right == None):
            root.right = child
            child.documents.append(document)
        else:
            insertTree(root.right,child,document)
    elif (root.key == child.key):
        root.documents.append(document)
def BuildBalancedBST(sortedList,left,right,document):
    mid = int((left+right)/2)
    root = Node(sortedList[mid])
    if (left > right):
        return None
    root.documents.append(document)
    root.left = BuildBalancedBST(sortedList,left,mid -1,document)
    root.right = BuildBalancedBST(sortedList,mid + 1,right,document)
    return root

# mn awel hena

def BuildBalancedBST_Nodes(sortedList,left,right):
    mid = int((left+right)/2)
    root = sortedList[mid]
    if (left > right):
        return None
    root.left = BuildBalancedBST_Nodes(sortedList,left,mid -1)
    root.right = BuildBalancedBST_Nodes(sortedList,mid + 1,right)
    return root


traversal_result = []
def traversal_in_order(root):
    global traversal_result
    x = "not"

    if root.left is None:
        traversal_result.append(root)
        if root.right is None:
            return "Done"
        elif root.right is not None:
            return traversal_in_order(root.right)
    elif root.left is not None:
        x = traversal_in_order(root.left)
        traversal_result.append(root)
        if root.right is None:
            return "Done"
        elif root.right is not None:
            return traversal_in_order(root.right)
        return x

# l7ad hena



def Parse(Path,progress,loading_root,percentage):
    Tokens = []
    global Percentage
    global Parsed
    global NumberOfFiles
    NumberOfFiles = len(os.listdir(Path))
    #print('Parsing started')


    with os.scandir(Path) as entries:
        beginningFlag = 0
        for entry in entries:
            with open(Path + '\\' + entry.name, 'r', encoding = 'utf-8') as f:
                Untokenized = f.read()
            Tokens = list(filter(None, re.split("[, \n./:() +]", Untokenized)))
            Tokens = Remove(Tokens)
            if (beginningFlag == 0):
                Tokens.sort()
                root = BuildBalancedBST(Tokens, 0, len(Tokens) - 1, entry.name)
                beginningFlag = 1
            else:
                for index1 in Tokens:
                    insertTree(root, Node(index1), entry.name)
            Parsed += 1
            Percentage = Parsed / NumberOfFiles * 100

            # change percentage here
            #percentage = calculate_perc()
            progress['value'] = Percentage
            loading_root.update_idletasks()
            Percentage += 1  # httzbt lma el function bta3tha t5ls
            # time.sleep(1)
            # print(percentage)
            progress.grid(row=2, column=1, padx=10, pady=15)
            print(Percentage, '%')
    #print('Parsing ended')
    # w mn awel hena
    traversal_in_order(root)
    root = BuildBalancedBST_Nodes(traversal_result, 0, len(traversal_result) - 1)
    # l7ad hena
    return root
def calculate_perc():
    global Parsed
    global NumberOfFiles
    return  Parsed / NumberOfFiles * 100
def search(root,searchkey):
    found = TreeSearch(root,searchkey)
    files_list=[]
    if found is None:
        print('not found')
    else:
        print('found in')
        for doc in found.documents:
            print(doc)
            files_list.append(doc)

    return files_list

'''''
root = Parse(r"D:\Desktop\TASLEMAT\Data_Structure\questions")


while(1):
    searchkey = input("Enter word")
    search(root,searchkey)
'''


