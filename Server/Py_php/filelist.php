<?php   

$dir = "../user_img/";
 
// Open a directory, and read its contents      
if (is_dir($dir)){                              
  if ($dh = opendir($dir)){                     
    while (($file = readdir($dh)) !== false){   
      echo $file . " ";        
    }                                           
    closedir($dh);                              
  }                                             
}           
?>