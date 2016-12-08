<html>
<title>TRIPS</title>
<p><h1>Creat a new trip</h1></p>
<form method="POST">
<table border='1'>
<tr>
<td>Start</td>
<td>Mid 1</td>
<td>Mid 2</td>
<td>Mid 3</td>
<td>Mid 4</td>
<td>Mid 5</td>
<td>Mid 6</td>
<td>End</td>
</tr>
<tr>

	<td><input type="text" name="start" value=""></td>
	<td><input type="text" name="mid1" value=""></td>
	<td><input type="text" name="mid2" value=""></td>
	<td><input type="text" name="mid3" value=""></td>
	<td><input type="text" name="mid4" value=""></td>
	<td><input type="text" name="mid5" value=""></td>
	<td><input type="text" name="mid6" value=""></td>
	<td><input type="text" name="end" value=""></td>
	<tr><input type="submit" value="Add"></tr>

</tr>
</table>
</form>

</html>
<?php
	
if(!empty($_POST['start']) && !empty($_POST['end']) && (!empty($_POST['mid1']) || !empty($_POST['mid2']) || !empty($_POST['mid3']) || !empty($_POST['mid4']) || !empty($_POST['mid5']) ||  !empty($_POST['mid6']))){
	
	$start = $_POST['start'];
	$end = $_POST['end'];
	$mid1 = $_POST['mid1'];
	$mid2 = $_POST['mid2'];
	$mid3 = $_POST['mid3'];
	$mid4 = $_POST['mid4'];
	$mid5 = $_POST['mid5'];
	$mid6 = $_POST['mid6'];
		
	
	$url = "http://localhost:1314/trips";
	$ch = curl_init();
	$mid = array();
	if(!empty($mid1)) array_push($mid, '/locations/'.$mid1);
	if(!empty($mid2)) array_push($mid, '/locations/'.$mid2);
	if(!empty($mid3)) array_push($mid, '/locations/'.$mid3);
	if(!empty($mid4)) array_push($mid, '/locations/'.$mid4);
	if(!empty($mid5)) array_push($mid, '/locations/'.$mid5);
	if(!empty($mid6)) array_push($mid, '/locations/'.$mid6);
	
	$input = array('start' => ('/locations/'.$start), 'others' => $mid, 'end' => ('/locations/'.$end));
	//print($input);
	$input_j = json_encode($input);
	//print($input_j);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $input_j);	
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($input_j)));  
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_URL, $url);
	$response = curl_exec($ch);
	echo '<h2> Return Value </h2><br>';
	print($response);
	curl_close($ch);

	$result = json_decode($response, true);
	var_dump($result);
	$result = $result['provider'];
	//var_dump($result);
	$uber = $result[0];
	echo("<h3>UBER</h3>");
	echo("<table border='1'>
<tr>
<td>Duration</td>
<td>Distance</td>
<td>Cost</td>
</tr>
<tr>
<td>".$uber['total_duration']." ".$uber['duration_unit']."</td>
<td>".$uber['total_distance']." ".$uber['distance_unit']."</td>
<td>".$uber['total_costs_by_cheapest_car_type']." ".$uber['currency_code']."</td>

</tr>

</table>");
	
	
	$lyft = $result[1];
	echo("<h3>LYFT</h3>");
	echo("<table border='1'>
<tr>
<td>Duration</td>
<td>Distance</td>
<td>Cost</td>
</tr>
<tr>
<td>".$lyft['total_duration']." ".$lyft['duration_unit']."</td>
<td>".$lyft['total_distance']." ".$lyft['distance_unit']."</td>
<td>".$lyft['total_costs_by_cheapest_car_type']." ".$lyft['current_code']."</td>

</tr>

</table>
<h4><a href='index.php'>BACK</a></h4>
");
	
	
	
	
	
}
else{
	//print('DSDFSDFSDF');
}
	
	
	
	
	
	
	
	

?>