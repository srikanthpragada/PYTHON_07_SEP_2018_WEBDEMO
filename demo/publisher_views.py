from django.shortcuts import render, redirect

import sqlite3
from . forms import AddPublisherForm

db_filename = r"e:\classroom\python\sep7\catalog.db"

def list(request):
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
    else:
        message = ''

    print("Received : " , message)
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    cur.execute("select * from publishers order by pubid")
    return render(request, 'publisher/list.html',
                  {'publishers': cur.fetchall(), 'message' : message})


def add(request):
    message = ""
    if request.method == "POST":
        f = AddPublisherForm(request.POST)
        if f.is_valid():
            pubname = f.cleaned_data["pubname"]
            website = f.cleaned_data["website"]
            # Insert row into PUBLISHERS table
            con = sqlite3.connect(db_filename)
            cur = con.cursor()
            try:
                cur.execute("insert into publishers(pubname,website) values (?,?)",
                        (pubname,website))
                if cur.rowcount == 1:
                    con.commit()
                    message = "Publisher has been added successfully"
            except Exception as ex:
                message = "Sorry! Could not add publisher!"
                print("Error : " + ex)
    else:
        f = AddPublisherForm()

    return render(request, 'publisher/add.html',
                  {'form' : f, 'message' : message})


def delete(request,pubid):
    print(pubid)
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    try:
        cur.execute("delete from publishers where pubid = ?",(pubid,))
        if cur.rowcount == 1:
            message = f"Publisher {pubid} deleted!"
            con.commit()
    except Exception as ex:
        print("Error : ", ex)
        message = f"Could not delete publisher {pubid}"
    request.session["message"] = message
    return redirect("/demo/list_publishers")