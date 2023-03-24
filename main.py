# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import lxml.etree
from lxml.etree import _Element, _ElementTree
import lxml

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def ensure_lxml():
    """
    tests we can import lxml
    :return:
    """
    xml_string = "<foo><bar>baz</bar></foo>"
    foo_bar = lxml.etree.fromstring(xml_string)
    print (f"foo xml {foo_bar}")
    assert len(foo_bar.xpath("bar")) == 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    ensure_lxml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
