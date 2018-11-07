import json
from urllib.parse import quote


class TableOfContents:

    def __init__(self, fname):
        toc = ["<ul>"]
        with open(fname) as file:
            nb = json.load(file)
        prev_level = 1
        for cell in nb["cells"]:
            if cell["cell_type"] != "markdown":
                continue
            for line in cell["source"]:
                if line.startswith("#"):
                    level, title = line.strip().split(maxsplit=1)
                    level = len(level)
                    optional_slash = "/" if prev_level > level else ""
                    for _ in range(abs(prev_level - level)):
                        toc.append(f"<{optional_slash}ul>")
                    anchor = quote(title, safe=" ").replace(" ", "-")
                    toc.append(f'<li><a href="#{anchor}">{title}</a></li>')
                    prev_level = level
        toc.append("</ul>")
        self.toc = "\n".join(toc)

    # def __repr__(self):
    def _repr_html_(self):
        return self.toc
