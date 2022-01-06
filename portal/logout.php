<?php
session_start();
session_destroy();
header("Location: http://localhost/attend%20-%20Copy/portal/signin.php", true, 301);
?>


