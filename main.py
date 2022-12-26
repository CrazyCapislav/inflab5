XML_file = open('core.xml', encoding='utf-8').readlines()
string = str()
flag = True
text = str()
for k in range(len(XML_file)):
    text = text + XML_file[k]
text = text.replace('<xml>', '{')
text = text.replace('</xml>', '}')
for k1 in range(len(text)):
    if text[k1] == "/":
        string = string[0:-1] + '",'
        flag = False
    elif flag == False and text[k1] == ">":
        flag = True
    elif flag:
        string = string + text[k1]
text = string.replace('<', '<<')
string = ''
flag = True
for k2 in range(len(text)):
    if text[k2] == ">" and text[k2 + 1] == '\n':
        string += '": {'
    else:
        string += text[k2]
text = string.replace(">", '>>: <<')
string = ''
count = 0
i = 0
flag = True
for k3 in range(len(text) - 3):
    if flag and text[k3] == ',' and text[k3 + 1] == '\n':
        flag = False
        i = k3 + 2
        count = 0
        while not flag:
            if text[i] == '\n':
                flag = True
            elif text[i] != '"' and text[i] != ' ' and text[i] != ',':
                count += 1
            i += 1
        if count == 0:
            continue
        else:
            string += text[k3]
    else:
        string += text[k3]
string += '\n' + '}'
string = string.replace('"', '}')
string = string.replace('<<', '"')
text = string
string = ''
for k4 in range(len(text)):
    if text[k4] == '}' and text[k4 - 1] != ' ' and text[k4 - 1] != '\n':
        string += '"'
    else:
        string += text[k4]
string = string.replace('>>', '"')
print(string)
JSON_file = open("json_file", "w", encoding="utf-8")
JSON_file.write(string)
