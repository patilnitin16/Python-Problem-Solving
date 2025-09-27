'''
You are given an XML document. Your task is to compute the maximum depth of the XML tree. The depth of an element is the number of levels of nested tags from the root.

The root element is at depth 0 (or 1 if you count from 1 — your code starts from -1 so root = 0).

Child elements increase the depth by 1.

📥 Input Format
The first line contains an integer N, the number of lines in the XML document.
The next N lines contain the XML content.

📤 Output Format
Print a single integer: the maximum depth of the XML tree.

'''

#Code
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level+=1
    maxdepth = max(maxdepth,level)
    for el in elem:
        depth(el,level)
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)