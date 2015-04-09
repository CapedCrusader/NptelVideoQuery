<?php 

$conn = mysql_connect($dbhost, $dbuser, $dbpass) 
    or die("Connection Failure to Database");

mysql_select_db($dbname, $conn) or die ($dbname . " Database not found." . $dbuser);

?>