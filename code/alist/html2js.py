import argparse

def html_to_js(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.readlines()
    
    js_lines = []
    for line in html_content:
        line = line.strip()
        line = line.replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'")
        js_lines.append(f'document.writeln("{line}");')
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(js_lines))
    
    print(f"轉換完成，JavaScript 已儲存至 {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML to JavaScript string.")
    parser.add_argument("--input", "-i", help="Path to input HTML file", default="./alist_head.html")
    parser.add_argument("--output", "-o", help="Path to output JavaScript file", default="./alist_head.js")
    args = parser.parse_args()

    html_to_js(args.input, args.output)
