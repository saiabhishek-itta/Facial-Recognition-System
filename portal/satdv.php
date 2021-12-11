<?php
session_start();
if(isset($_GET['id'])){
$cred=explode("-",$_GET['id']);
$_SESSION['facid']=$cred[0];
$_SESSION['slot']=$cred[1];}

?>

<?php

if(!isset($_SESSION["userid"]))
header("Location: http://localhost/attend%20-%20Copy/portal/signin.php", true, 301);
echo"Logged in ".$_SESSION["userid"];
?>


<!DOCTYPE html>
<html>
<style>
table {
  border-collapse: collapse;
  width: 60%;
  padding: 10%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color: #157DEC;
  color: white;
}

#head{
  background-color: red;
}
#formid{
  
  padding:20px;
}

  </style>
  <meta charset="utf-8">
	<meta name="viewport" content=
		"width=device-width, initial-scale=1,
		shrink-to-fit=no">
	<link rel="stylesheet" href=
"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
		integrity=
"sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
		crossorigin="anonymous">



<head>
<div id="head">
  <a style{align:left;} href="logout.php">Logout</a>
</div>
  <title>Attendance Details</title>
</head>
<body>

<center>
<h2><?php echo('Slot - '.$_SESSION['slot']." ");?>Attendence Details</h2>






<br>
<table border="2">
  <tr>
    <td>Sr.No.</td>
    <td>Date</td>
    <td>Time</td>
  </tr>

<?php

include "dbconnect.php";
$facid=$_SESSION['facid'];$slot=$_SESSION['slot'];
$stdid=$_SESSION["userid"];
$records = mysqli_query($conn,"select * from atd where facid='$facid' and slot='$slot' and stdid='$stdid'"); 
$i=1;
while($data = mysqli_fetch_array($records))
{
?>
  <tr>
    <td><?php echo $i++; ?></td>

    <td><?php echo $data['date']; ?></td>
    <td><?php echo $data['time']; ?></td>   

  </tr>	
<?php
}
?>
</table><br><br>
<a href="student.php">Back</a>









</body>
</html>