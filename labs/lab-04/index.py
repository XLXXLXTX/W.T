#  Web Technologies Lab 4 | Author: Javier Pardos | javier.pardos10@e-uvt.ro 
import xml.etree.ElementTree as ET

from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/')
def display_content(content=None):
    xml_tree = ET.parse('queue.xml').getroot()

    #recover each record tag
    list_records = xml_tree.findall('record')

    #recover each field of the record
    #to save them in a list of dictionaries
    records_dict = []
    for r in list_records:
        #Recovers the main fields of the record tag
        n = r.get('name')
        d = r.get('date')
        u = r.get('uri')
        t = r.get('type')
        
        #Recovers the subrecords
        s1 = r.find('subrecord1').text
        s2 = r.find('subrecord2').text
        s3 = r.find('subrecord3').text
        records_dict.append({'name': n, 'date': d, 'uri': u, 'type': t,
                             'subrecord1': s1, 'subrecord2': s2, 'subrecord3': s3})
    
    #Pass the list of dictionaries to the template
    return render_template('template.html', content=records_dict)