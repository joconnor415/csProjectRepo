<?php

include '/Applications/XAMPP/database/database.php';

if (isset($_COOKIE['user']) && isset($_COOKIE['signature'])){
	header("location: hello.php");
}

if ($_SERVER['REQUEST_METHOD'] == 'POST'){
	$user = $_POST['u'];
	$ct = $_POST['p'];
	$ts = $_POST['ts'];

	$priv_key_content = file_get_contents("/Applications/XAMPP/keypairs/privatekey.pem");
	$private_key = openssl_get_privatekey($priv_key_content);
	openssl_private_decrypt(base64_decode($ct), $pt, $private_key);

	$curr_ts = substr($pt, 0, 13);
	$pass = substr($pt, 13);

	$db_connection = new Database();
	if ($db_connection->connect()){
		$passts = $db_connection->login($user);
		$p = $passts->pwd;
		$t = $passts->timestamp;

		if (($ts == $curr_ts) && ($pass == $p) && (floatval($curr_ts) > floatval($t))){
			$isValid = $db_connection->updateTs($user, $ts);
			if ($isValid){
				openssl_sign(sha1(((string)session_id()) + $user), $signature, $private_key);
				setcookie("user", $user);
				setcookie("signature", $signature);
				$db_connection->disconnect();
				header("location: hello.php");
			}
			else {
				echo "Please refresh page and try again";
			}
		}
		else{
			$db_connection->disconnect();
			echo "Please enter your username and password"."</br>";
		}
	}
	else {
		$db_connection->disconnect();
		echo "Please refresh page and retry";
	}
}
?>


<html>
<body>

	<script type="text/javascript" src="jsbn.js"></script>
	<script type="text/javascript" src="rsa.js"></script>
	<script type="text/javascript" src="sha1.js"></script>
	<script type="text/javascript" src="login.js"></script>

	Username:<input id="user" type="text" name="user" /> 
	Password:<input id="pwd" type="password" name="pwd" />
	<input type="button" onclick="matcher(event)" value="submit" />
	<br />

	<div id="encryption" style="display: none;"></div>
	
	<p><a href="register.php">New User? Register Here</a></p>
</body>
</html>
