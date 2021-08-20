import re
stripped = []


with open('training_data/output.txt') as f:
    lines = f.readlines()
    for line in lines[4:-3]:
        if(line.startswith('\n')
           or line.startswith("Joined the server.")
           or line.startswith("https://")
           or line.startswith("http://")
           or "https://" in line
           or "http://" in line
           or line.startswith("{Attachments}")
           or line.startswith("{Embed}")
           or line.startswith("{Reactions}")):
            continue
        chat_header = re.match(
            r"(\[[z0-9][z0-9]-[A-Za][a-z][a-z]-[z0-9][z0-9] [z0-9][z0-9]:[z0-9][z0-9] [A-Za][A-Za]\] (.*))", line)
        if(chat_header):
            continue
        stripped.append(line.strip())
f.close()

with open("output1.txt", "w") as o:
    for line in stripped:
        o.write(line + "\n")
o.close()
