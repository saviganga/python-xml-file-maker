#THIS SCRIPT CREATES AND SAVES STANDARD XML FILES FROM USER INPUT




#import your xml pyhton module
import xml.etree.ElementTree as Element_Object

#import the minidom module and save it as an object to pretty print our xml file
import xml.dom.minidom as xml_pprint


def xml_doc():

    global y_answer
    global n_answer
    global root_xml

    #get the number of xml documents to be created
    num_xml_documents = int(input('Enter the NUMBER of XML DOCUMENTS: '))

    #create the root
    # create a loop and make the document
    for a in range(1, num_xml_documents + 1):
        # create the root

        print('YOU ARE NOW IN ROOT ' + str(a) + ' \n')

        #create root
        create_root(a, num_xml_documents)

        #ask for root child tags
        is_rootchild = input('Does the ROOT have CHILD TAGS (Y/N): ')
        y_answer = 'y'
        n_answer = 'n'
        #create a condition

        if is_rootchild.lower() == y_answer:
            create_rootchild()
        elif is_rootchild.lower() == n_answer:
            pass
        else:
            print('Sorry, the system does not understand your command.')

        print('\n')
        Element_Object.dump(root_xml)

        #pretty print your xml document
        prettyprint_xml(root_xml)

        #save to a file
        save_xml()

    return root_xml




def create_root(a, num_xml_documents):

    global root_xml

    # create a variable to store the string name of the inventory
    root = input('\nEnter the NAME of your ROOT ELEMENT ' + str(a) + ': ')
    # create a variable to store the element object with the string variable
    root_xml = Element_Object.Element(root)

    # dump it
    Element_Object.dump(root_xml)
    return root_xml



def create_rootchild():

    global root_xml
    global y_answer
    global n_answer
    global rootchild
    global rootchild_xml
    num_rootchild = int(input('Enter the NUMBER of ROOT CHILDREN: '))

    for b in range(1, num_rootchild+1):

        #store the ROOT CHILD TAG in a variable
        rootchild = input('\nEnter the NAME of ROOTCHILD ' +str(b)+ ': ')


        #ask if there are attributes
        is_attribute = input('DOES this ROOT CHILD TAG have ATTRIBUTES (Y/N) :')

        answers = [y_answer, n_answer]

        #create a condition

        if is_attribute.lower() == y_answer:

            ### create an empty dictionary
            attrib_dict = {}

            ### create a flag
            is_attribute = True

            create_attribute(is_attribute, attrib_dict)

        elif is_attribute.lower() == n_answer:
            rootchild_xml = Element_Object.SubElement(root_xml, rootchild)
            Element_Object.dump(root_xml)

        else:
            print('Sorry the system did not understand your command')

            # ADD it as a SUBELEMENT of the ROOT
            rootchild_xml = Element_Object.SubElement(root_xml, rootchild)


        #ask for ROOTCHILD_CHILD TAGS
        is_rootchild_child = input('DOES this ROOT CHILD have CHILD TAGS (Y/N): ')

        #create a condition
        if is_rootchild_child == y_answer:
            create_rootchild_child()

        elif is_rootchild_child.lower() == n_answer:
            pass

        else:
            print('Sorry, the system did not understand your command')

    return root_xml




def create_attribute(is_attribute, attrib_dict):

    global y_answer
    global n_answer
    global rootchild
    global root_xml
    global rootchild_xml

    while is_attribute:
        #prompt user for id and value
        atrib_id = input('\nEnter your ROOT CHILD ATTRIBUTE ID: ')
        attrib_value = input('Enter your ROOT CHILD ATTRIBUTE VALUE: ')

        #store the responses in our dictionary
        attrib_dict[atrib_id] = attrib_value

        #ask if the user has any oother attributes
        ismore_attrib = input('\nDo you have MORE ROOT CHILD ARRTIBUTES (Y/N): ')
        if ismore_attrib == y_answer:
            is_attribute = True
        elif ismore_attrib == n_answer:
            is_attribute = False

    for id, value in attrib_dict.items():
        print(id, ' : ', value)

    # create the subelement of the root with the attributes
    rootchild_xml = Element_Object.SubElement(root_xml, rootchild, attrib=attrib_dict)

    # dump it
    Element_Object.dump(root_xml)

    return root_xml




def create_rootchild_child():

    global rootchild_child_xml
    global rootchild_xml
    global root_xml
    global y_answer
    global n_answer

    # ask for the number of root children
    num_rootchild_child = int(input('Enter the NUMBER of ROOTCHILD_CHILD tags: '))

    # create a for loop with the number of rootchild_child tags
    for c in range(1, num_rootchild_child + 1):
        print('YOU ARE NOW IN ROOTCHILD_CHILD ' + str(c) + '\n')

        # create the tag names
        rootchild_child = input('Enter the NAME of ROOTCHILD_CHILD ' + str(c) + ': ')

     # add it as a subelement of your root child
        rootchild_child_xml = Element_Object.SubElement(rootchild_xml, rootchild_child)
        Element_Object.dump(root_xml)

        #ask if the rootchild_child has content
        is_content = input('DOES this ROOTCHILD_CHILD have CONTENT (Y/N): ')

        #create condition
        if is_content == y_answer:
            create_content()
        elif is_content == n_answer:
            pass
        else:
            print('Sorry, the system did not understand your command \n')

        Element_Object.dump(root_xml)




def create_content():
    global rootchild_child_xml
    global root_xml

    #create a variable to store user content
    rootchild_child_xml.text = input('\nENTER YOUR CONTENT: ')
    return rootchild_child_xml




def prettyprint_xml(root_xml):

    global xml_docc

    xml_docc = xml_pprint.parseString(Element_Object.tostring(root_xml)).toprettyxml()
    print(xml_docc)
    return xml_docc




def save_xml():
    global xml_docc
    xml_doc_bytes = str.encode(xml_docc, 'utf-8')

    filename = input('Enter a filename to store your xml document: ')

    with open(filename, 'wb') as f:
        f.write(xml_doc_bytes)





xml_doc()