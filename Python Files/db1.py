# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:39:54 2021

@author: Ramya
"""

#import pymysql


from flask import Response
from fpdf import FPDF
import mysql.connector
from mysql.connector import Error


def state(statename):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='states',
                                             user='root',
                                             password='root')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
           
            cursor.execute("select id,name,wind,temperature,humditity,storm,startdate,enddate from "+statename+ " where wind < '64' and humditity < 80")
            
            record = cursor.fetchall()
            
            pdf = FPDF()
            pdf.add_page()
            page_width = pdf.w - 2 * pdf.l_margin
            pdf.set_font('Times','B',14.0) 
            pdf.cell(page_width, 0.0, 'Safe zone Places', align='C')
            pdf.set_font('Times','B',14.0) 
            pdf.cell(page_width, 0.0, 'Safe Zone Places', align='C')
            pdf.ln(10)
            pdf.set_font('Courier', '', 12)
            col_width = page_width/4
            pdf.ln(1)
            th = pdf.font_size
            for row in record:
                pdf.cell(col_width-40, th, str(row[0]), border=1)
                pdf.cell(col_width, th, str(row[1]), border=1)
                pdf.cell(col_width-30, th, str(row[2]), border=1)
                pdf.cell(col_width-33, th, str(row[3]), border=1)
                pdf.cell(col_width-40, th, str(row[4]), border=1)
                pdf.cell(col_width-12, th, str(row[5]), border=1)
                pdf.cell(col_width-25, th, str(row[6]), border=1)
                pdf.cell(col_width-25, th, str(row[7]), border=1)
                pdf.ln(th)
            pdf.ln(10)
            pdf.set_font('Times','',10.0)
            pdf.cell(page_width, 0.0, '- end of report -', align='C')
            pdf.output(statename+' safe.pdf', 'F')
           # return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename='+statename+'.pdf'})
			
	    	
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

