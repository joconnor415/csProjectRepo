<?php

class Database{

	private $host = 'localhost';
	private $user = 'root';
	private $pw = '';
	private $database_name = 'my_database';

	public function connect(){
		$db_conn = mysql_connect($this->host, $this->user, $this->pw);

		if (!$db_conn){
			return FALSE;
		}

		$database = mysql_select_db($this->database_name, $db_conn);

		if ($database){
			return TRUE;
		}
		else{
			return FALSE;
		}
	}

	public function login($username){
		$result = mysql_query("SELECT pw, timestamp FROM users WHERE uname='$username';");
		$pass_result = mysql_fetch_object($result);
		return $pass_result;
	}

	public function register($username, $password, $timestamp){
		$result = mysql_query("SELECT pw FROM users WHERE uname='$username';");
		$pass_result = mysql_fetch_object($result);

		if ($pass_result->pw){
			return FALSE;
		}
		else{
			$isValid = mysql_query("INSERT INTO users (uname, pw, timestamp) VALUES ('$username','$password', '$timestamp')");
			return $isValid;
		}
	}
	
	public function updateTs($username, $ts){
		$isValid = mysql_query("UPDATE users SET timestamp='$ts' WHERE uname='$username';");
		return $isValid;
	}

	public function disconnect(){
		mysql_close();
	}
}
?>