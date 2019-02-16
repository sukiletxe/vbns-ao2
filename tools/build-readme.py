import markdown, os
os.chdir(os.pardir)
markdown.markdownFromFile(input = "readme.md", encoding = "utf-8", output = "readme.html")
