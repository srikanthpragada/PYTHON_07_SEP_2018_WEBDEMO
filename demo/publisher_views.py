from django.shortcuts import render
import sqlite3
from . forms import AddPublisherForm


def list(request):
    con = sqlite3.connect(r"e:\classroom\python\sep7\catalog.db")
    cur = con.cursor()
    cur.execute("select * from publishers order by pubid")
    return render(request, 'publisher/list.html',
                  {'publishers': cur.fetchall()})


def add(request):
    f = AddPublisherForm()
    return render(request, 'publisher/add.html', {'form' : f})
