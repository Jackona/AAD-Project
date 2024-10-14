from reportlab.pdfgen import canvas
import datetime
import os
import subprocess


def generate_pdf(file_name):
    # if the file exists it will be deleted
    if os.path.exists(file_name):
        os.remove(file_name)
    # Create a canvas object
    pdf_file = canvas.Canvas(file_name)
    # Write "Hello" to the PDF file
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    # Create a canvas object
    pdf_file = canvas.Canvas(file_name)
    # title
    pdf_file.drawString(250, 720, "Health and Safety Report")
    # Write the current date to the PDF file
    pdf_file.drawString(72, 680, "Date: " + date_str)
    # ------------------------------------make current user variable which will get the current user------------------------------------------
    # ------------------------------------current user will go here
    pdf_file.drawString(72, 660, "Inspector Name: " + "CURRENTUSER")
    # write the observations
    pdf_file.drawString(72, 640, "Observations: " + "Ok")

    # ------------------------------------current user will go here
    pdf_file.drawString(450, 500, "Signed: " + "currentuser")
    # Save the file
    pdf_file.save()
    # open the pdf
    os.startfile(file_name)


# get the current date-time
now = datetime.datetime.now()
# get only the date
current_date_str = now.strftime("%Y-%m-%d")
# Prepare the filename
filename = current_date_str + "#HS.pdf"
# Generate the PDF file
generate_pdf(filename)
# endoffunction