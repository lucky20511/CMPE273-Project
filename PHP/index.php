<html>
<title>Users List </title>
<h1><b>LOCATION</b></h1>

<h2><a href="curl_read.php">VIEW</a></h2>
<h2><a href="curl_add.php">ADD</a></h2>
<h2><a href="curl_update.php">UPDATE</a></h2>
<h2><a href="curl_delete.php">DELETE</a></h2>
<?php
	
	/*$url = "http://localhost:1314/locations/1";
	$ch = curl_init();
	$mid = array('/locations/2', '/locations/3');
	$input = array('start' => '/locations/1', 'others' => $mid, 'end' => '/locations/4');
	$input_j = json_encode($input);
	//print($input_j);
	/*($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $input_j);	
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($input_j)));  
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_URL, $url);
	$response = curl_exec($ch);
	print($response);
	curl_close($ch);*/
	
?>
<br><br><br>

<h1><b>TRIPS</b></h1>
<h2><a href="curl_trips.php">ADD</a></h2>
</div>
</html>