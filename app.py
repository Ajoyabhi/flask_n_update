from flask import Flask, request, render_template,send_file,make_response,url_for, Response, redirect, request,send_from_directory,send_file,after_this_request
import pandas as pd
# import audit_analyzer
import joblib
import os
import re
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import xlrd
import zipfile
from multiprocessing import *
import shutil

UPLOAD_FOLDER = './'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template('index.html')
   
    # If a form is submitted
    if request.method ==  "POST":
       
        zip_file=request.files['zip_']
        zip_file.save(os.path.join('./', zip_file.filename))
       
        day, result = 12, 24
        return render_template('download.html', filename = zip_file.filename)
   
@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    print(filename)
    print('hello')
#     @after_this_request
#     def remove_file(response):
#         os.remove(filename)
# #         for e_f in glob.glob('*.zip'):
# #             os.remove(e_f)
#         return response
#     def remove_file(response):
#         try:
#             print("REMOVE FILE Function")
#             os.remove(filename)
#             print("File REmoved")
#             for e_f in glob.glob('*.zip'):
#                 os.remove(e_f)

#         except Exception as error:
#             app.logger.error("Error removing or closing downloaded file handle", error)
#         return response
   
   
    return send_from_directory('./', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug = True, port=5353)