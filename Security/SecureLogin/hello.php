<?php

if (isset($_COOKIE['user']) && isset($_COOKIE['signature'])){
	$public_key = openssl_get_publickey(file_get_contents("/Applications/XAMPP/keypairs/publickey.pem"));
	$isValid = openssl_verify(sha1((string)session_id() + $_COOKIE['user']), $_COOKIE['signature'], $public_key);
	if ($isValid == 1){
		echo "Welcome ".$_COOKIE['user'];
	}
	else{
		header("location: login.php");
	}
}
else{
	header("location: login.php");
}
?>

<html>
<body>
	<script type="text/javascript">
	function logout() {
    	document.cookie = "user=deleted; expires="+ new Date(0).toUTCString();
    	document.cookie = "signature=deleted; expires="+ new Date(0).toUTCString();
    	window.location = "login.php";
	}
</script>

	<p>
		<input type="button" onclick="logout()" value="Logout" />
	</p>
</body>
</html>
