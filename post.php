<?php
session_start();
if(isset($_SESSION['name'])){
    $text = $_POST['text'];
    exec("python backend.py \"".$text."\"", $output);
    $fp = fopen("log.html", 'a');
    fwrite($fp, "<div class='msgln'>(".gmdate("H:i", time() + 3600*7).") <b>".$_SESSION['name']."</b>: ".stripslashes(htmlspecialchars($text))."<br></div>");
    fwrite($fp, "<div class='msgln'>(".gmdate("H:i", time() + 3600*7).") <b>"."Alice"."</b>: ".stripslashes($output[0])."<br></div>");
    fclose($fp);
}
?>