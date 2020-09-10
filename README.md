# Creating a Website Portfolio using Pelican

Using Pelican, a static site generator, I began to create a personal website from scratch. This is my first attempt at creating a website so everything I have managed to build so far was, effectively, learning on the job. After much stress, research and time, this is where I have got to currently. I am yet to push the website via GitHub actions, in order to automate the workflow of the website but, that is my next goal.

#Workflow
1. Firstly I installed Pelican using,
<p><code>python -m pip install "pelican[markdown]"</code></p>
2. Executed pelican-quickstart. I made sure to host on GitHub.
3. I created a page for the About Me section, while also creating articles to describe my projects with Bash and Python.
4. After creating these pages and articles, I created the *images* directory in the *content* directory. In the pelicanconfig.py, I edited STATIC_PATHS = [ 'IMAGES' ].
5. Then, I linked the images required into the repective, pages and articles.
6. The website was, then, ready to be published. Within the output directory,
<p><code>git init
<br>git add .
<br>git commit -m "first commit"
<br>git remote add origin remote repository URL
<br>git remote -v
<br>git push origin master</code></p>
7. Then push output to GitHub Pages after creating gh-pages branch,
<p><code>git checkout -b gh-pages
<br>git push origin gh-pages</code></p>
8. Finally I decided to create a source branch so the code/content could be viewed also. Within the portfolio directory,
<p><code>git checkout -b source
<br>git init
<br>git add .
<br>git commit -m "source"
<br>git push origin source</code></p>


