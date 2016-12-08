<html>
<title>UPDATE</title>
<p><h1>Update a location</h1></p>
<form method="POST">
<table border='1'>
<tr>
<td>Location</td>
<td>Name</td>

<tr>
<tr>
	<td><input type="text" name="location" value=""></td>
	<td><input type="text" name="name" value=""></td>
	<td><input type="submit" value="Update"></td>

</tr>
</table>
</form>

</html>
<?php
if(!empty($_POST['location']) && !empty($_POST['name']) ){
	$location = $_POST['location'];
	$input = array();
	$name = $_POST['name'];
	
	
	if(!empty($name)) $input["name"] = $name;
	//print_r($input);
	
	$url = "http://localhost:1314/locations/".$location;
	$ch = curl_init();
	$input_j = json_encode($input);
	print $input_j;
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($input_j))); 
	curl_setopt($ch, CURLOPT_POSTFIELDS, $input_j);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_URL, $url);
	$response = curl_exec($ch);
	echo '<h2> Return Value </h2><br>';
	if(isset($response)) print('Update Success!');
	else print('Update Failed!');
	curl_close($ch);
	
}
echo("<h4><a href='index.php'>BACK</a></h4>");
?>