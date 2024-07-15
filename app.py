from flask import Flask, render_template, request, redirect
import solr
import view

# Define Flask App
app = Flask(__name__)

# HOMEPAGE
@app.route("/", methods=["GET"])
def hello():
  data = solr.mysolr().search("*:*", rows=6)
  return render_template("/home/index.html", data=data)

# POSTS
@app.route("/posts")
def page_posts_index():
  page = request.args.get("page", default=1, type=int)
  return view.post_page(page=page)

@app.route("/posts/create", methods=["GET", "POST"])
def page_posts_create():
  if request.method == "POST":
    print(request.form)

    title = request.form.get("title")

    tags = request.form.get("tags")
    splitted_tags = tags.split(",")

    content = request.form.get("content")

    data = [{
        "title": title,
        "tags": splitted_tags,
        "content": content
      }]
    
    solr.mysolr().add(data) 
    
    return redirect("/posts")
  else :
    return view.post_create_page()

@app.route("/posts/<id>")
def page_posts_content(id):
  return view.post_content_page(id)

# ERROR
@app.errorhandler(404)
def not_found(e):
  return render_template("/404.html")

# Running Flask App
if __name__ == '__main__':
  app.run(debug=True)
