def parsing(txt, idx):
    data = {}
    while True:
        if idx >= len(txt) or "}" in txt[idx]:
            break
        elif "{" in txt[idx]:
            temp_data, temp_idx = parsing(txt, idx + 1)
            data[txt[idx - 1]] = temp_data
            idx = temp_idx
        elif ": " in txt[idx]:
            data[txt[idx - 1]] = txt[idx + 1]
        idx += 1
    return data, idx


def sealing(data, file, lvl):
    for key in data:
        file.write("\t" * lvl + "<{}>".format(key))
        if isinstance(data[key], dict):
            file.write("\n")
            sealing(data[key], file, lvl + 1)
            file.write("\t" * lvl + "</{}>\n".format(key))
        else:
            file.write(data[key])
            file.write("</{}>\n".format(key))
    return 0


JSON_file = open("coreres.json", encoding="utf-8")
text = JSON_file.read().split('"')
JSON_file.close()
# text, index = parsing(text, 1)
# print(text, index)
data = {}
idx = 1
txt = text
while True:
    if idx >= len(txt) or "</>" in txt[idx]:
        break
    elif "{" in txt[idx]:
        temp_data, temp_idx = parsing(txt, idx + 1)
        data[txt[idx - 1]] = temp_data
        idx = temp_idx
    elif ": " in txt[idx]:
        data[txt[idx - 1]] = txt[idx + 1]
    idx += 1
print(data)
# XML_file = open("XML-1.XML", "w", encoding="utf-8")
# XML_file.write("<xml>\n")
# sealing(text, XML_file, 1)
# XML_file.write("</xml>")
# XML_file.close()
