#  Web Technologies Lab 5 | Author: Javier Pardos | javier.pardos10@e-uvt.ro 
# DOM libs
import xml.dom.minidom as mdom
# SAX
import xml
from xml.sax import handler, make_parser, SAXParseException
# timer libs
import time



def parse_with_sax(xml_file : str) -> float:
    
    # Define a class that inherits from ContentHandler
    class MySAXHandler(handler.ContentHandler):
        def __init__(self):
            pass
        
        def startDocument(self):
            #print('Entering document')
            pass

        def endDocument(self):
            #print('Leaving document')      
            pass

        def startElement(self, name, attrs):
            pass
            #print(f'Found element: {name}')
            
            #for attr_name, value in attrs.items():
            #    print(f'Found attribute: {attr_name} with value: {value}')

        def endElement(self, name):
            #print(f'Leaving element: {name}')
            pass

        def characters(self, content):
            #print(f'Found text node: {content}')
            pass


    # start timer
    start_time = time.time()

    # controll the parser errors 
    try:
        # create the SAX parser 
        sax_parser = xml.sax.make_parser()

        # set the content handler
        sax_parser.setContentHandler(MySAXHandler())
        
        # finally parse the xml file with our custom handler
        sax_parser.parse(xml_file)

    # care the possible SAX exceptions
    except xml.sax.SAXParseException:
        print('SAX: The document is not well formed')
    
    # end timer
    end_time = time.time()

    # calculate total time
    total = end_time - start_time
    
    # return the total time
    return total


def parse_with_dom(xml_file : str) -> (str, float):

    # aux function to follow the nodes, and to know how many there are in the original XML
    def follow_nodes(node, parent) -> None:
        
        # create new element, to represent the node/tag for the new xml
        element = dom_new.createElement(node.nodeName)

        # for each node/tag in the original xml, retrieve the attributes and add them to the new xml
        for attribute_name, attribute_value in node.attributes.items():
            element.setAttribute(attribute_name, attribute_value)

        # if the element has a child, we follow the child in a recursive way
        for c in node.childNodes:
            # compare if the node is an element or a text node
            if c.nodeType == mdom.Node.ELEMENT_NODE:
                # recursive call
                follow_nodes(c, element)
            else:
                # if the element has no child, we add the text to the new xml
                text_node = dom_new.createTextNode(c.nodeValue)
                element.appendChild(text_node)

        # finally, add child to parent
        parent.appendChild(element)


    # start timer
    start_time = time.time()

    # create new xml document
    dom_new = mdom.Document()
    

    try:
        # parse the original xml file
        dom_original = mdom.parse(xml_file)
    except:
        print('DOM: Document is not well formed')
        exit(1)

    # for each child in original xml call the aux function
    # only if its an element node
    for i in dom_original.childNodes:
        if i.nodeType == mdom.Node.ELEMENT_NODE:
            follow_nodes(i, dom_new)
    
    content = dom_new.toprettyxml(indent='  ')

    # end timer
    end_time = time.time()
    # calculate total time
    total = end_time - start_time

    return content, total


def main(xml_file : str) -> None:

    # Print out the parsing time of each method 
    # (hint: use time.time() to get the start and end time).

    # print SAX parser data
    print(f'\nParsing with SAX ...')
    timeSAX = parse_with_sax(xml_file)
    print(f'-Time required SAX: {timeSAX} seconds')

    # print DOM parser data
    print(f'\nParsing with DOM ...')
    xml_DOM, timeDOM = parse_with_dom(xml_file)
    print(f'-Time required DOM: {timeDOM} seconds')

    print()
    print(xml_DOM)
    

    # print faster parser 
    if timeDOM < timeSAX:
        print(f'\nDOM ({timeDOM} segs) is faster than SAX ({timeSAX} segs) by {timeSAX - timeDOM} seconds')
    else:
        print(f'\nSAX ({timeSAX} segs) is faster than DOM ({timeDOM} segs) by {timeDOM - timeSAX} seconds')
    

if __name__ == '__main__':
    
    # define XML file to test
    XML_FILE = 'main.xml'

    # call main function
    main(XML_FILE)


