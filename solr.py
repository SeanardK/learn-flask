import pysolr

def mysolr():
  return pysolr.Solr("http://localhost:8983/solr/learn_solr",always_commit=True)
