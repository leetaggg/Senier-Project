<?php
    $con = mysqli_connect("localhost", "ahard", "1234", "student");
    mysqli_query($con,'SET NAMES utf8');

    $userID = $_POST["userID"];
    $userPassword = $_POST["userPassword"];

    $statement = mysqli_prepare($con, "SELECT * FROM user WHERE userID = ? AND userPassword = ?");
    mysqli_stmt_bind_param($statement, "ss", $userID, $userPassword);
    mysqli_stmt_execute($statement);
   
    

    mysqli_stmt_store_result($statement);
    mysqli_stmt_bind_result($statement, $userID, $userPassword, $name, $grade, $renewal);
    
    

    $response = array();
    $response["success"] = 0;


    $statement0 = mysqli_query($con, "SELECT userID FROM user WHERE userID = '$userID' AND userPassword = '$userPassword' AND renewal = 0");
    if(mysqli_num_rows($statement0)){
        $response["success"] = 1;
    }

    $statement1 = mysqli_query($con, "SELECT userID FROM user WHERE userID = '$userID' AND userPassword = '$userPassword' AND renewal = 1");
    if(mysqli_num_rows($statement1)){
        $response["success"] = 2;
    }

    $statement2 = mysqli_query($con, "SELECT userID FROM user WHERE userID = '$userID' AND userPassword = '$userPassword' AND renewal = 2");
    if(mysqli_num_rows($statement2)){
        $response["success"] = 3;
    }

    $statement3 = mysqli_query($con, "SELECT userID FROM user WHERE userID = '$userID' AND userPassword = '$userPassword' AND renewal = 3");
    if(mysqli_num_rows($statement3)){
        while(mysqli_stmt_fetch($statement)) {
            $response["success"] = 4;
            $response["userID"] = $userID;
            $response["userPassword"] = $userPassword;
            $response["name"] = $name;
            $response["grade"] = $grade;
            $response["renewal"] = $renewal;   
        }
    }

    $statement4 = mysqli_query($con, "SELECT userID FROM user WHERE userID = '$userID' AND userPassword = '$userPassword' AND renewal = 4");
    if(mysqli_num_rows($statement4)){
        $response["success"] = 5;
    }
    
    
    echo json_encode($response);



?>