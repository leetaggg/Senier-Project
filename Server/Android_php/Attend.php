<?php
    $con = mysqli_connect("localhost", "ahard", "1234", "student");
    mysqli_query($con,'SET NAMES utf8');

    $userID = $_POST["userID"];

    $statement = mysqli_prepare($con, "SELECT * FROM attend WHERE userID = ?");
    mysqli_stmt_bind_param($statement, "s", $userID);
    mysqli_stmt_execute($statement);

    mysqli_stmt_store_result($statement);
    mysqli_stmt_bind_result($statement, $userID, $weekone, $weektwo, $weekthree, $weekfour, $weekfive);


    $response = array();
    $response["success"] = false;

    while(mysqli_stmt_fetch($statement)) {
        $response["success"] = true;
        $response["userID"] = $userID;
        $response["weekone"] = $weekone;
        $response["weektwo"] = $weektwo;
        $response["weekthree"] = $weekthree;
        $response["weekfour"] = $weekfour;
        $response["weekfive"] = $weekfive;
        
    }

    echo json_encode($response);
