### This is a test task for a sample API.

First of all, pull the docker image to your local machine: 
`docker pull azshoo/alaska`

Then run the image on your local machine using the 80th port: 
`docker run -d -p 80:8091 azshoo/alaska`

Then open `http://localhost/info` in your browser.

When running tests, you can use parameter `--bear_id=X` (where X is an integer) in the command line - thus, you can run the tests for a specific bear ID.

Test cases can be found below: 
https://docs.google.com/spreadsheets/d/1LuSYvZfpxcArIlg4sWxpLzrl37Fo3vIgC8ODPSc1qU0/edit?usp=sharing
