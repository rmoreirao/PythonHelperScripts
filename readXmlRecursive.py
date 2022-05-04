import xml.etree.ElementTree as ET


def iterate_recur(current_node,path):
    path = path + "/" + current_node.tag
    children = [child for child in current_node]

    if len(current_node.attrib) > 0:
        for key in current_node.attrib:
            print(path + "/@" + key + "=" + current_node.attrib[key])

    if len(children) > 0:
        for child in children:
            iterate_recur(child,path)
    else:
        if current_node.text:
            print(path + "=" + current_node.text)

file = 'sample.xml'
tree = ET.parse(file)

root = tree.getroot()
iterate_recur(root,"")


# for elem in tree.iter():
#     print(elem.tag, elem.text)
