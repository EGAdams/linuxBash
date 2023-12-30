import os
import subprocess

def clean_mysql_output(text):
    lines = text.split('\n')
    cleaned_lines = []

    for line in lines:
        cells = line.split('|')
        cleaned_cells = [cell.strip()[:20] + "..." if len(cell.strip()) > 20 else cell.strip() for cell in cells]
        cleaned_line = " | ".join(cleaned_cells)
        cleaned_lines.append(cleaned_line)

    return '\n'.join(cleaned_lines)

# Use subprocess to capture the output of the shell script
result = subprocess.run(["/home/adamsl/linuxBash/menu_shell_scripts/show_all_tables.sh"], stdout=subprocess.PIPE, text=True)

# Apply the filter to the captured output
filtered_output = clean_mysql_output(result.stdout)

# Print the filtered output
print(filtered_output)