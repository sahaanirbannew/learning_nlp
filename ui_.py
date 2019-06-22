def write_to_file(filename, content):
    str_content = ''
    for term in content:
        str_content = str_content + ',' + str(term)

    str_content = str_content + '\n'
    file_path = filename+'.csv'
    try:
        file = open(file_path, 'a', encoding='utf-8')
    except:
        file = open(file_path, 'w', encoding='utf-8')
    file.write(str_content)
    file.close()
