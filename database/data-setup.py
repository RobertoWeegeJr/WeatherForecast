import json

text_file = open("data-setup.sql", "w", encoding="utf8")

text_file.write("USE CitiesForecast;\n")

with open('country.list.json', encoding="utf8") as f:
    data = json.load(f)

iterator = iter(data)

for line in iterator:
    output = ""
    output += "INSERT INTO t_countries (code, name) VALUES ('"
    output += line['Code']
    output += "', '"
    output += line['Name'].replace("'", "''")
    output += "');\n"
    text_file.write(output)

output = ""
output += "INSERT INTO t_countries (code, name) VALUES ('"
output += "XK"
output += "', '"
output += "Kosovo"
output += "');\n"
text_file.write(output)    

with open('city.list.json', encoding="utf8") as f:
    data = json.load(f)

iterator = iter(data)

for line in iterator:
    if line['country']:
        output = ""
        output += "INSERT INTO t_cities (id, name, country) VALUES ("
        output += str(line['id'])
        output += ", '"
        output += line['name'].replace("'", "''")
        output += "', '"
        output += line['country']
        output += "');\n"
        text_file.write(output)

text_file.close()