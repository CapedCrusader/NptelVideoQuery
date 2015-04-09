<?php
  
if (isset($_GET['term'])){
    $return_arr = array();
	$stmt = $conn->prepare('SELECT distinct keyword FROM keyword_search WHERE keyword LIKE :term');
	$stmt->execute(array('term' => '%'.$_GET['term'].'%'));
	while($row = $stmt->fetch(){
		$return_array[] = $row['keyword'];
						
		    		}
  			
    /* Toss back results as json encoded array. */
    echo json_encode($return_arr);
}
?>