from flask import render_template
import solr

def post_page(page):
  data = solr.mysolr().search("*:*", rows=12, start=page-1)

  return render_template("/posts/index/index.html", posts=data)

def post_create_page():
  return render_template("/posts/create/index.html")

def post_content_page(id):
  print(id)

  data = solr.mysolr().search("id:{0}".format(id), rows=12)
  for item in data:
    print(item)

  return render_template("/posts/content/index.html", post=data)