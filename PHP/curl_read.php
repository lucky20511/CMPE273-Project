<html>
<title>VIEW</title>
<p><h1>View a location</h1></p>
<form method="POST">
<table border='1'>
<tr>
<td>Location</td>

<tr>
<tr>
	<td><input type="text" name="location" value=""></td>

	<td><input type="submit" value="View"></td>

</tr>
</table>
</form>

</html>
 <?php
	if(!empty($_POST['location'])){
		$location = $_POST['location'];
		$url = "http://localhost:1314/locations/".$location;
		$ch = curl_init();
		/*$mid = array('/locations/2', '/locations/3');
		$input = array('start' => '/locations/1', 'others' => $mid, 'end' => '/locations/4');
		$input_j = json_encode($input);
		//print($input_j);
		/*($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $input_j);	
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
		'Content-Type: application/json',                                                                                
		'Content-Length: ' . strlen($input_j)));  */
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_URL, $url);
		$response = curl_exec($ch);
		echo '<h2> Return Value </h2><br>';
		print($response);
		curl_close($ch);
	}
	
	echo("<h4><a href='index.php'>BACK</a></h4>");
?>