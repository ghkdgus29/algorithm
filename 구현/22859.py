import re

html = input()

chunks = html.split("<div title=")

for s in chunks:
    title = re.search(r'"([^"]+)"', s)
    if not title:
        continue
    print("title : " + title.group(1))
    paragraphs = re.findall(r'<p>(.*?)<\/p>', s)
    paragraphs = [re.sub(r'<[^>]+>', '', p) for p in paragraphs]
    paragraphs = [re.sub(r'\s+', ' ', p.strip()) for p in paragraphs]
    for p in paragraphs:
        print(p)
