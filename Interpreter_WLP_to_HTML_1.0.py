import re
import sys

def wlp_to_html(wlp_code: str) -> str:
    html_head = ""
    html_body = ""
    page_style = ""

    # Usuń linie startowe/końcowe WLP
    wlp_code = re.sub(r'^start-web-page;.*\n', '', wlp_code)
    wlp_code = re.sub(r'code-end;.*', '', wlp_code)

    lines = wlp_code.splitlines()
    for line in lines:
        line = line.strip()

        if line.startswith("title="):
            title = re.findall(r'title="(.*?)"', line)
            if title:
                html_head += f"<title>{title[0]}</title>\n"

        elif line.startswith("wlp-pro-key="):
            key = re.findall(r'wlp-pro-key="(.*?)"', line)
            if key:
                html_head += f'<meta name="wlp-pro-key" content="{key[0]}">\n'

        elif line.startswith("background-color="):
            bg = re.findall(r'background-color="(.*?)"', line)
            if bg:
                page_style += f"background-color:{bg[0]};"

        elif line.startswith("text-color="):
            tc = re.findall(r'text-color="(.*?)"', line)
            if tc:
                page_style += f"color:{tc[0]};"

        elif line.startswith("textbox("):
            text_match = re.search(r'text="(.*?)"', line)
            text = text_match.group(1) if text_match else ""
            onclick_match = re.search(r'onclick="(.+?)"\)', line)
            onclick = onclick_match.group(1) if onclick_match else ""
            onclick = onclick.replace('"', "&quot;")
            html_body += f'<span onclick="{onclick}">{text}</span><br>\n'

        elif line.startswith("inputtext("):
            text_match = re.search(r'text="(.*?)"', line)
            text = text_match.group(1) if text_match else ""
            html_body += f'<input type="text" value="{text}"><br>\n'

        elif line.startswith("button("):
            text_match = re.search(r'text="(.*?)"', line)
            onclick_match = re.search(r'onclick="(.+?)"\)', line)
            text = text_match.group(1) if text_match else "Kliknij"
            onclick = onclick_match.group(1) if onclick_match else ""
            onclick = onclick.replace('"', "&quot;")
            html_body += f'<button onclick="{onclick}">{text}</button><br>\n'

    html = f"""<!DOCTYPE html>
<html>
<head>
{html_head}
<style>
body {{
{page_style}
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    return html


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wlp_converter.py filename.wlp")
        sys.exit(1)

    wlp_filename = sys.argv[1]

    with open(wlp_filename, "r", encoding="utf-8") as f:
        wlp = f.read()

    html = wlp_to_html(wlp)

    output_filename = "output.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"WLP code converted to HTML → {output_filename}")
