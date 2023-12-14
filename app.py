from flask import Flask, render_template_string
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_csv():
    # Get the current date
   # Get the current date in the format 'DD-MM-YYYY'
    current_date = datetime.now().strftime("%d-%B-%Y")

# Create the file path using the current date
    file_path = f"Attendance/Attendance_{current_date}.csv"

    try:
        df = pd.read_csv(file_path)

        # Convert the DataFrame to HTML table
        table_html = df.to_html(index=False)

        # Render the HTML template with the table data
        html_content = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Attendance CSV</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                h1 {{
                    text-align: center;
                }}
                table {{
                    border-collapse: collapse;
                    width: 80%;
                    margin: auto;
                }}
                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Attendance Data</h1>
            {table_html}
        </body>
        </html>
        '''

        return render_template_string(html_content)
    except FileNotFoundError:
        return f"No attendance data available for {current_date}"

if __name__ == '__main__':
    app.run(debug=True)