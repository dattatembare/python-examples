import xml.etree.ElementTree as ET

xml_string = """<main>
                    <child from="ABC" to="1"/>
                    <child from="DEF" to="2"/>
                </main>"""

element = ET.XML(xml_string)
for el in element:
    print(el.tag, el.text, el.attrib)

# child None {'from': 'ABC', 'to': '1'}
# child None {'from': 'DEF', 'to': '2'}

my_dict = {attrs.get('from'): attrs.get('to') for attrs in [e.attrib for e in element]}
print(my_dict)  # {'ABC': '1', 'DEF': '2'}
