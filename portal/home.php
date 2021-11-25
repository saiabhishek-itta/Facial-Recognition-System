<?php
session_start();
echo"home page ".$_SESSION["userid"]." ".$_SESSION['category'];
?>