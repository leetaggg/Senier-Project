<?php

$dir_path = 'C:/Server/Apache24/htdocs/user_img/';
$user_name = $_POST['uname'];
$path = $dir_path.$user_name;

$dir_count = 0;
$file_count = 0;
$valid_formats = array("jpg", "png", "jpeg", "gif");

$result = opendir($path);

while($file = readdir($result)){
    if($file === "." || $file === "..") continue;
    $getExt = pathinfo($file, PATHINFO_EXTENSION);

    if(empty($getExt)){
        $dir_count++;
    } else{
        if(in_array($getExt, $valid_formats)){
            $file_count++;
        }
    }
}

echo "$file_count";
?>