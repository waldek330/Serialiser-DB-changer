from tkinter.font import BOLD
import pyodbc
from tkinter import *
import tkinter as tk
from tkinter import ttk

def bga_version():
    try:
        driver = "{SQL Server}"
        server = "tpcz01s195\sqlexpress"
        database = "sc_sers"
        username = "sa"
        password = "Bskyb1234$"
        port = "1433"
   
        connection = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+
                ';PWD='+password)
        cursor = connection.cursor()
   
        query = "UPDATE sc_sers.dbo.tbl_db_Version SET DatabaseVersion=N'4.9.5';"
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        print("Udało się zmienić wersję.")
    except Exception:
        print("\nERROR: Unable to connect to the server.")
        exit(-1)

def production_version():
    try:
        driver = "{SQL Server}"
        server = "tpcz01s195\sqlexpress"
        database = "sc_sers"
        username = "sa"
        password = "Bskyb1234$"
        port = "1433"
   
        connection = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+
                ';PWD='+password)
        cursor = connection.cursor()
   
        query = "UPDATE sc_sers.dbo.tbl_db_Version SET DatabaseVersion=N'5.0.0';"
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        print("Udało się zmienić wersję.")
    except Exception:
        print("\nERROR: Unable to connect to the server.")
        exit(-1)

def test_version():
    try:
        driver = "{SQL Server}"
        server = "tpcz01s195\sqlexpress"
        database = "sc_sers"
        username = "sa"
        password = "Bskyb1234$"
        port = "1433"
   
        connection = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+
                ';PWD='+password)
        cursor = connection.cursor()
   
        query = "UPDATE sc_sers.dbo.tbl_db_Version SET DatabaseVersion=N'5.1.0';"
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        print("Udało się zmienić wersję.")
    except Exception:
        print("\nERROR: Unable to connect to the server.")
        exit(-1)

# Creating tkinter window
window = tk.Tk()
window.title('Serialiser version changer v.1')
window.resizable(width=False, height=False)
window.geometry('750x250')
 
# label text for title
ttk.Label(window, text = "Z opcji poniżej wybierz odpowiednią wersję do zmiany:",
          foreground ="black",
          font = ("Times New Roman", 15, BOLD)).grid(row = 0, column = 1)


#buttons for running function to change Serialiser  version
submit_button_1 = Button(window, text="Serialiser 4.9.5", font= BOLD, command=bga_version)
submit_button_1.place(x=25, y=100)

submit_button_2 = Button(window, text="Serialiser 5.0.0", font= BOLD, command=production_version)
submit_button_2.place(x=300, y=100)

submit_button_3 = Button(window, text="Serialiser 5.1.0", font= BOLD, command=test_version)
submit_button_3.place(x=550, y=100)

#credits label
credits = ttk.Label(window, text = "Credits for waldemar.lusiak@reconext.com", font = ("Times New Roman", 10, BOLD))
credits.place(relx=1, rely=1, anchor=SE)

window.mainloop()