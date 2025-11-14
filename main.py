from pathlib import Path
import mainDraw

def main():
    mainDraw.daily_refresh()
    divar_root = Path("divar_results")
    root = Path("./")
    if not divar_root.exists():
        print("divar_results directory not found.")
        return

    folders = [f for f in divar_root.iterdir() if f.is_dir()]
    if not folders:
        print("No folders found in divar_results.")
        return

    # --- Generate reports ---
    for folder in folders:
        report_path = f"{folder.name}_report.html"
        print(f"Generating report for {folder.name} -> {report_path}")
        mainDraw.drawer(str(report_path), str(folder))

    # --- Create index.html ---
    index_file = Path("index.html")
    html_lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "  <meta charset='utf-8'>",
        "  <title>Divar Results Index</title>",
        "  <style>",
        "    body { font-family: Arial, sans-serif; padding: 20px; }",
        "    h1 { margin-bottom: 20px; }",
        "    .btn { display: inline-block; margin: 8px; padding: 10px 20px; background: #eee; border-radius: 6px; text-decoration: none; color: black; }",
        "    .btn:hover { background: #ddd; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Reports</h1>",
    ]
    for folder in folders:
        link = f"{folder.name}_report.html"
        html_lines.append(f"  <a class='btn' href='{link}'>{folder.name}</a>")
    html_lines += ["</body>", "</html>"]

    index_file.write_text("\n".join(html_lines), encoding="utf-8")
    print(f"Index created at: {index_file}")

if __name__ == "__main__":
    main()
