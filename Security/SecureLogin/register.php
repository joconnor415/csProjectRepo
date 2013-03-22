<?php

include '/Applications/XAMPP/database/database.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST'){
	$user = $_POST['u'];
	$ct = $_POST['p'];
	$ts = $_POST['ts'];

	$priv_key_content = file_get_contents("/Applications/XAMPP/keypairs/privatekey.pem");
	$private_key = openssl_get_privatekey($content);
	openssl_private_decrypt(base64_decode($ct), $pt, $private_key);

	$curr_ts = substr($pt, 0, 13);
	$pass = substr($pt, 13);

	if ($curr_ts == $ts){
		$db_conn = new Database();
		if ($db_conn->connect()){
			$isValid = $db_conn->register($user, $pass, $ts);
			if ($isValid){
				$db_conn->disconnect();
				header("location: login.php");
			}
			else{
				$db_conn->disconnect();
				echo "Sorry there was a registration error, please try again";
			}
		}
		else{
			echo "Error when connecting, please reload page";
		}
	}

}

?>

<html>
<body>

	<script type="text/javascript" src="jsbn.js"></script>
	<script type="text/javascript" src="rsa.js"></script>
	<script type="text/javascript" src="sha1.js"></script>
	<script type="text/javascript" src="register.js"></script>

	Username:
	<input id="user" type="text" name="user" /> Password:
	<input id="pwd" type="password" name="pwd" /> Confirm Password:
	<input id="cpwd" type="password" name="cpwd" />
	<input type="button" onclick="matcher(event)" value="submit" />
	<br />

	<div id="encryption" style="display: none;"></div>

</body>
</html>
