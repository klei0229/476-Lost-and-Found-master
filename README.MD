CSc 47300 Fall 2017 Project: Improv-Chatroom-master

Front-End: Html/CSS
Server: FLASK
Back-end: Python

To Run The App:
First: install flask, and flask-wtf (may need create a venv mode)
Second: python application.py

To Run the Test:
First: Install pytest
second: run pytest to see all the test cases
        or run pytest *****.py to verify on each individual test files
(notes: someone may received error of version problem of flask that related to blinker.
Solution is install blinker by using pip)
The totals cases: 51 unit tests. However, this is the total numbers because
51 represents 51 functions. However, some cases I used for loops.
test_exsitance_css has 9
test_existance_templates has 12
test_existance has 14
test_home has 40
test_routes has 8
Total assertions we had is 83 assertions.

Deploy Using Heroku:
http://improvproject.herokuapp.com/ --- main
http://improvproject2.herokuapp.com/ --- node.js for video and chatroom

Video and Chatroom Repository:
https://github.com/klei0229/improv_video


Contributor github:
https://github.com/LiuYuHao/476-Improv-Chatroom-master
https://github.com/yejack/476-Improv-Chatroom-master

Warning: to add/change new style in external file, don't be worried about if the page
didn't make any change. You need to refresh the css file in website in order make it work in html,
if this still didn't work, you need to inspect element -> source -> find the css file -> fresh.
For exmaple, if you change/add something in chatroom.css. Refresh the page of 127.../static/css/chatroom.css
make sure the change/addition you made is in there, refresh the html page.
