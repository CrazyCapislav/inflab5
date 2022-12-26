import xmltodict
import json
with open('core.xml', encoding='utf-8') as fd:
    doc = xmltodict.parse(fd.read())
print(doc)
string = str(doc)
string = string[8:-1]
doc = eval(string)
string = json.dumps(doc, indent=4, sort_keys=True, ensure_ascii=False)
print(string)

JSON_file = open("json_file", "w", encoding="utf-8")
JSON_file.write(string)

