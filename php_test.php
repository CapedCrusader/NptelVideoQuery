<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title> FIND LECTURES BY KEYWORDS </title>
	<link rel="stylesheet" href="js/jquery-ui.min.css" type="text/css" />
	<script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
	<script type="text/javascript" src="js/jquery-ui.min.js"></script>
</head>

<form method=post id=searchForm name=searchForm action="query.php" method="get">

<tr><td align="right">Enter Keyword :</td><td align="left"><input type="text" name="keyword" class="auto"/></td></tr>

<tr><td colspan=2 align="center"> <input type="submit" value="Find Lectures"  /></td></tr>
                            
</form>

<script type="text/javascript">
	$(function() {
    //autocomplete
    	$(".auto").autocomplete({
        	source: "search_test.php",
        	minLength: 1
    	});                
 	});
</script>




 
