import re

XML_file = open('core.xml', encoding='utf-8').readlines()
string = str()
flag = True
text = str()
for k in range(len(XML_file)):
    text = text + XML_file[k]
string = re.sub(r'<xml>', '{', text)
string = re.sub(r'</xml>', '}', string)
string = re.sub(r'</.*>', '",', string)
string = re.sub(r'>\n', '": {\n', string)
string = re.sub(r' ",\n', ' },\n', string)
string = re.sub(r'<', '"', string)
string = re.sub(r'>', '": "', string)
string = re.sub(r',(\n\s*)}', '\g<1>}', string)
print(string)
JSON_file = open("json_file", "w", encoding="utf-8")
JSON_file.write(string)
