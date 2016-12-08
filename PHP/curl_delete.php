<html>
<title>DELETE</title>
<p><h1>Delete a location</h1></p>
<form method="POST">
<table border='1'>
<tr>
<td>Location</td>

<tr>
<tr>
	<td><input type="text" name="location" value=""></td>

	<td><input type="submit" value="Delete"></td>

</tr>
</table>
</form>

</html>
<?php
if(!empty($_POST['location'])){
	$location = $_POST['location'];
	
	
	//print_r($input);
	
	$url = "http://localhost:1314/locations/".$location;
	$ch = curl_init();
	
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");

	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_URL, $url);
	$response = curl_exec($ch);
	echo '<h2> Return Value </h2><br>';
	print($response);
	curl_close($ch);
	
}
echo("<h4><a href='index.php'>BACK</a></h4>");
?>