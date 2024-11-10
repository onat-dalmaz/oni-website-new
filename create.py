import os
# Create a basic 'baseof.html' file in 'layouts/_default'
layout_default_path = 'layouts/_default'
baseof_html_path = os.path.join(layout_default_path, 'baseof.html')
os.makedirs(layout_default_path, exist_ok=True)

baseof_html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    {{ partial "head.html" . }}
    <link rel="stylesheet" href="{{ "themes/blue.css" | relURL }}">
</head>
<body>
    {{ block "main" . }}{{ end }}
</body>
</html>
"""

# Write the template to 'baseof.html'
with open(baseof_html_path, 'w') as file:
    file.write(baseof_html_template)

"baseof.html created with a basic template including the blue.css stylesheet."
