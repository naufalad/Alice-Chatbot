<html>
<head>
<title>ChatBot Alice</title>
<link type="text/css" rel="stylesheet" href="style.css" />
</head>

<?php
    session_start();
    
    
    function loginForm(){
        echo'
        <div id="loginform">
        <form action="index.php" method="post">
            <p>Masukkan Namamu :</p>
            <label for="name">Nama :</label>
            <input type="text" name="name" id="name" />
            <input type="submit" name="enter" id="enter" value="Enter" />
        </form>
        </div>
        ';
    }
    if(isset($_POST['enter'])){
        if($_POST['name'] != ""){
            $_SESSION['name'] = stripslashes(htmlspecialchars($_POST['name']));
            exec("python backend.py", $output);
            $fp = fopen("log.html", 'a');
            fwrite($fp, "<div class='msgln'>(".gmdate("H:i", time() + 3600*7).") <b>"."Alice"."</b>: ".stripslashes($output[0])."<br></div>");
            fclose($fp);
        }
        else{
            echo '<span class="error">Please type in a name</span>';
        }
    }
    if(isset($_GET['logout'])){ 
        session_destroy();
        file_put_contents("log.html", "");
        header("Location: index.php"); //Redirect the user
    }
    if(!isset($_SESSION['name'])){
        loginForm();
    }
    else{
    ?>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div id="wrapper">
        <div id="header">
            <p class="title"><b> ChatBot Alice </b></p>
        </div>
        <div id="profpict">
            <img src = "photo.jpg" id = "photo" alt = "profile picture" height = 270 width = 270>
        </div>
        <div id="menu">
            <p class="welcome">Selamat datang, <b><?php echo $_SESSION['name']; ?></b></p>
            <p class="logout"><a id="exit" href="#">Exit Chat</a></p>
            <div style="clear:both"></div>
        </div>    
        <div id="chatbox"><?php
        if(file_exists("log.html") && filesize("log.html") > 0){
            $handle = fopen("log.html", "r");
            $contents = fread($handle, filesize("log.html"));
            fclose($handle);
            
            echo $contents;
        }
        ?></div>
        <form name="message" action="">
            <input name="usermsg" type="text" id="usermsg" size="63" />
            <input name="submitmsg" type="submit"  id="submitmsg" value="Send" />
        </form>
    </div>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
    <script type="text/javascript">
    // jQuery Document
    $(document).ready(function(){
        //If user wants to end session
        $("#exit").click(function(){
            var exit = confirm("Are you sure you want to end the session?");
            if(exit==true){window.location = 'index.php?logout=true';}		
        });
    });
        //If user submits the form
        $("#submitmsg").click(function(){	
            var clientmsg = $("#usermsg").val();
            if (clientmsg != ""){
                $.post("post.php", {text: clientmsg});				
                $("#usermsg").attr("value", "");
                loadlog;
                return false;
            }
        });
        //Load the file containing the chat log
        function loadLog(){		
            var oldscrollHeight = $("#chatbox").attr("scrollHeight") - 20; //Scroll height before the request
            $.ajax({
                url: "log.html",
                cache: false,
                success: function(html){		
                    $("#chatbox").html(html); //Insert chat log into the #chatbox div	
                }				
            });                  
            //Auto-scroll			
            var elem = window.document.getElementById('chatbox');
            elem.scrollTop = elem.scrollHeight;
        }
        window.setInterval(function(){
            
        }, 1000);
    </script>
    <?php
    }
    ?>
</body>
</html>