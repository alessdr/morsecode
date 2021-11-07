# heroku login
# heroku container:login
heroku apps:destroy -a morse-code-interpreter --confirm morse-code-interpreter
heroku create morse-code-interpreter
heroku container:push web -a morse-code-interpreter
heroku container:release web -a morse-code-interpreter
heroku open -a morse-code-interpreter
