<b>(9/26) Background:</b> <br>
<b>1)</b> Uses https://hub.docker.com/r/selenium/standalone-docker image (Selenium Grid Standalone with Dynamic capabilities) <br>
<b>2)</b> Utilizes pytest to test http://www.cnn.com and https://www.cnn.com/world via 3 different browsers <br>
<b>3)</b> Has logic to store individual test results into MySQL DB <br>
<b>4)</b> Also stores the run_id (entire SeleniumGrid execution) and worker_id (which pytest-xdist handled the test)
<b>5)</b> Test name, test script, run location (manual vs jenkins) are also stored in MySQL DB <br>
<b>6)</b> PyCharm Dev Environment is on Ubuntu 26.04 - Jenkins(1) <br>
<b>7)</b> Jenkins Instance is running on Ubuntu 26.04 - Jenkins(1) <br>
