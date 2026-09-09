<b>(9/9) Background:</b> <br>
1) Uses https://hub.docker.com/r/selenium/standalone-docker image (Selenium Grid Standalone with Dynamic capabilities) <br>
2) Utilizes pytest to test http://www.cnn.com and https://www.cnn.com/world via 3 different browsers <br>
3) Has logic to store individual test results into MySQL DB <br>
4) Also stores the run_id (entire SeleniumGrid execution) and worker_id (which pytest-xdist handled the test)
5) Test name, test script, run location (manual vs jenkins) are also stored in MySQL DB <br>
6) PyCharm Dev Environment is on Ubuntu 26.04 - Jenkins(1) <br>
7Jenkins Instance is running on Ubuntu 26.04 - Jenkins(1) <br>
