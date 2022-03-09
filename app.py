#!/usr/bin/env python
# coding: utf-8

# In[72]:


from flask import Flask, render_template, request


# In[73]:


import speech_recognition as sr
from werkzeug.utils import secure_filename


# In[74]:


app = Flask(__name__)


# In[75]:


#@app.route("/", methods = ["GET", "POST"])
#def index():
#    if request.method == "POST":
#        return(render_template("index.html", result = "1"))
#    else: 
#        return(render_template("index.html", result = "2"))


# In[76]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        print("File Received")
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source: 
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result = s))
    else: 
        return(render_template("index.html", result = "result"))


# In[77]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




