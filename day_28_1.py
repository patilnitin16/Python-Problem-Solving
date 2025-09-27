'''
TASK : 

You are given an XML document as input. Your task is to count the total number of attributes present in the entire XML tree (including the root, its children, grandchildren, and so on).

📥 Input format

The first line contains an integer N, the number of lines in the XML document.

The next N lines contain the XML data.

📤 Output format

Print a single integer: the total number of attributes in the XML.

'''

#Code

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    countNodes = len(node.attrib)
    for child in node:
        countNodes += get_attr_number(child)
    return countNodes

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))