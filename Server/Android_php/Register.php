<?php
    $con = mysqli_connect("localhost", "ahard", "1234", "student");
    mysqli_query($con,'SET NAMES utf8');
    
    $userID = $_POST["userID"];
    $userPassword = $_POST["userPassword"];
    $name = $_POST["name"];
    $grade = $_POST["grade"];
    
    
    $statement = mysqli_prepare($con, "INSERT INTO user VALUES (?, ?, ?, ?, 0)");
    mysqli_stmt_bind_param($statement, "ssss", $userID, $userPassword, $name, $grade);
    mysqli_stmt_execute($statement);

    $statement = mysqli_query($con, "INSERT INTO attend(userID) VALUES($userID)");

    mysqli_close($con);

    $response = array();
    $response["success"] = true;


    echo json_encode($response);



?>