<?php

$server_dir = 'C:/Server/Apache24/htdocs/';
$user_dir = $_POST['user_dir'];
$upload_dir = $server_dir.$user_dir;
$allowed_ext = array('jpg', 'jpeg', 'png', 'gif');

$error = $_FILES['myfile']['error'];
$name = $_FILES['myfile']['name'];
$ext = array_pop(explode('.', $name));

if( $error != UPLOAD_ERR_OK ) {
	switch( $error ) {
		case UPLOAD_ERR_INI_SIZE:
		case UPLOAD_ERR_FORM_SIZE:
			echo "파일 용량 초과 . ($error)";
			break;
		case UPLOAD_ERR_NO_FILE:
			echo "파일 첨부 오류. ($error)";
			break;
		default:
			echo "파일 업로드 오류. ($error)";
	}
	exit;
}

if( !in_array($ext, $allowed_ext) ) {
	echo "허용되지 않는 확장자입니다.";
	exit;
}
if(!is_dir($upload_dir)){
	mkdir($upload_dir, 0777, true);
}
move_uploaded_file( $_FILES['myfile']['tmp_name'], "$upload_dir/$name");

?>
