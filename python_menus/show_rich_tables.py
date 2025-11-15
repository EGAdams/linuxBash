import subprocess
from rich.console import Console
from rich.table import Table
from rich import box

def run_mysql_command(command):
    try:
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return ""

def parse_mysql_output(output):
    # Split the output into lines and filter out empty lines
    lines = [line for line in output.split('\n') if line.strip()]
    # Assuming the first line contains headers
    headers = [header.strip() for header in lines[0].split('|') if header.strip()]
    # Extract rows
    rows = [
        [cell.strip() for cell in line.split('|') if cell.strip()]
        for line in lines[1:]
    ]
    return headers, rows

def truncate_string(s, max_length=30):
    return (s[:max_length-3] + '...') if len(s) > max_length else s

def display_table(headers, rows):
    table = Table(show_header=True, header_style="bold magenta", box=box.SQUARE)

    # Define fixed widths for each column
    WIDTH = 240
    column_widths = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH]  # Example widths

    # Add columns with fixed widths
    for header, width in zip(headers, column_widths):
        table.add_column(header, width=width, overflow="fold")

    # Add rows to the table
    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)

# MySQL commands using .my.cnf (no inline password)
commands = [
    "mysql -D visionte_8 -e \"SELECT ID, pushid, first_name, last_name, rewards, device, email, uid, isAdmin FROM wp_mcba_users;\"",
    "mysql -D visionte_8 -e \"SELECT * FROM wp_mcba_chat_messages;\"",
    "mysql -D visionte_8 -e \"SELECT * FROM wp_mcba_chat_conversations;\""
]


for command in commands:
    output = run_mysql_command(command)
    headers, rows = parse_mysql_output(output)
    display_table(headers, rows)
