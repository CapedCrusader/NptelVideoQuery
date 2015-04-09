<div id="contentContainer" style="margin-left:0px">
<div style="float:left;">
<div id="slide">
<div style="padding-top:1px;padding-left:3px">
<div id="sideMenuId" style="width:250px;overflow:hidden;height:100%;">
<div id="menuiframe" style="height: 484px;">
<ul id="ul_nav">
<li class="first">
	<a class="header" style="border: medium none; outline: medium none;">Matched Lectures</a>
<ul style="display: block;">
<?php 
 	// Connecting to the database
	mysql_connect("localhost", "root", "") or die(mysql_error()); 
	mysql_select_db("slashroot") or die(mysql_error()); 
	$column = 0;

	if(isset($_REQUEST['keyword'])){
    		$keyword = $_REQUEST['keyword'];
    		if($keyword!=""){  		
    			$query = "SELECT Youtube_Query FROM keyword_search k1 WHERE k1.keyword LIKE '$keyword'";
	    		$sqlHandle=mysql_query($query);
	    	
	    		while($row = mysql_fetch_array($sqlHandle)){		   
	    			  	$Youtube_Query = $row['Youtube_Query'];
						$column++;
						echo '<li><a href="' . $row['Youtube_Query'] . '. target="frame_player"">' . "Result ". $column. '</a></li>';  
						echo '</br>';
		    		}
    		}	
  			else {
  			    echo "Please enter a keyword";
  			}
	}
?>
</ul>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>

<div id="myiframe" style="height: 514px;">
<ul class="tabsvid" style="width:608px"></ul>
<div class="tab_container_small" align="center" style="float:left">
<div id="tab1" class="tab_content" align="left" style="display: block;">
<?php
if($keyword!=""){ 
  echo '<iframe width="570" height="380" name="frame_player" src="' .$Youtube_Query . '"></iframe>';
}
?>
</div>
</div>
</div>