from flask import Flask, render_template, send_file
from datetime import datetime
import pdfkit
import io

################################################################################################################## 

app = Flask(__name__)

##################################################################################################################
# DUMMY DATA
################################################################################################################## 

TODAYS_DATE = datetime.today().strftime("%B %d, %Y")
DUE_DATE = "November 21, 2030"

COMPANY = {
    'name': "Fictional Inc.",
    'addr1': "12345 Rocky Road",
    'addr2': "Sunny Shores, CA 56789"
}

CLIENT = {
    'name': "John Doe",
    'email': "doejohn@example.com"
}

ITEMS = [
    {
        'title': 'website design',
        'price': 300.00
    },
    {
        'title': 'Hosting (3 months)',
        'price': 75.00
    },
    {
        'title': 'Domain name (1 year)',
        'price': 10.00
    }
]

TOTAL = sum([item['price'] for item in ITEMS])

##################################################################################################################
# SIMPLE SERVER
##################################################################################################################

@app.route('/')
def main():
    rendered = render_template(
        'invoice-template.html',
        date_today=TODAYS_DATE,
        date_due=DUE_DATE,
        company=COMPANY,
        client=CLIENT,
        items=ITEMS,
        total=TOTAL
    )

    # generates a PDF file from the filled template
    pdf = pdfkit.from_string(rendered, False)

    # returns the file for the client
    return send_file(io.BytesIO(pdf), download_name='invoice.pdf', mimetype='application/pdf')

##################################################################################################################

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)