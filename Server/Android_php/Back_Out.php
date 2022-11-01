<?php
//DB 시작
    $con = mysqli_connect("localhost", "ahard", "1234", "student");
    mysqli_query($con,'SET NAMES utf8');

    $userID = $_POST["userID"];
    $userPassword = $_POST["userPassword"];
    $file_path = "../delete/".$userID."/";
    $ispath = "../delete/".$userID;

    $response = array();
    $response["success"] = FALSE;  

    $statement = mysqli_query($con, "SELECT * FROM user WHERE userID = '$userID' AND userPassword = '$userPassword'");
    if(mysqli_num_rows($statement)){
        mysqli_query($con,"DELETE FROM user WHERE userID = '$userID'");
        mysqli_query($con,"DELETE FROM Attend WHERE userID = '$userID'");

        mysqli_close($con);

        $response["success"] = TRUE;
        
        if(!is_dir($ispath)){
            @mkdir($ispath, 0777);
            @chmod($ispath, 0777); 
        }
    
        
    }
    echo json_encode($response);
    

?>