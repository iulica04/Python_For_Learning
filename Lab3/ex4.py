#  The build_xml_element function receives the following parameters:
#  tag, content, and key-value elements given as name-parameters.
#  Build and return a string that represents the corresponding XML element.
#  Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
#  returns  the string = "<a href="http://python.org" _class="my-link" id="someid">Hello there</a>"

def build_xml_element(tag, content, **attributes):
    attributes_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())

    if attributes_str:
        xml_element = f'<{tag} {attributes_str}> {content} </{tag}>'
    else:
        xml_element = f'<{tag}> {content} </{tag}>'

    return xml_element

if __name__ == "__main__":
    print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))