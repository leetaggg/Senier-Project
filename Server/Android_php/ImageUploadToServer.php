<?php
$con = mysqli_connect("localhost", "ahard", "1234", "student");
mysqli_query($con, "SET NAMES utf8");

$data = $_POST["data1"];
$file_path = "../user_img/".$data."/";
$ispath = "../user_img/".$data;


echo $file_path;
    if(is_dir($ispath)){
        echo "폴더 존재 O"; // pass
    } else {
        echo "폴더 존재 X";
        @mkdir($ispath, 0777);
        @chmod($ispath, 0777); 
    }
   
    $file_path = $file_path . basename( $_FILES['uploaded_file']['name']);

    if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $file_path)) {
        echo "file upload success";
        mysqli_query($con, "UPDATE user SET renewal = 1 WHERE userID = '$data");
        mysqli_close($con);

    } else{
        echo "file upload fail";
    }

    
?>