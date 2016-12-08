<html>
<title>ADD</title>
<p><h1>Creat a new location</h1></p>
<form method="POST">
<table border='1'>
<tr>
<td>Name</td>
<td>Address</td>
<td>City</td>
<td>State</td>
<td>Zip</td>
<tr>
<tr>

	<td><input type="text" name="name" value=""></td>
	<td><input type="text" name="address" value=""></td>
	<td><input type="text" name="city" value=""></td>
	<td><input type="text" name="state" value=""></td>
	<td><input type="text" name="zip" value=""></td>
	<td><input type="submit" value="Add"></td>

</tr>
</table>
</form>

</html>
<?php
if(isset($_POST['name']) && !empty($_POST['address'])){
		$name = $_POST['name'];
		$address = $_POST['address'];
		$city = $_POST['city'];
		$state = $_POST['state'];
		$zip = $_POST['zip'];
	$input = array("name" => $name, "address" => $address, "city" => $city, "state" => $state, "zip" => $zip);
		
		
	$url = "http://localhost:1314/locations";
	$ch = curl_init();
	//$mid = array('/locations/2', '/locations/3');
	//$input = array('start' => '/locations/1', 'others' => $mid, 'end' => '/locations/4');
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
}
echo("<h4><a href='index.php'>BACK</a></h4>");
?>