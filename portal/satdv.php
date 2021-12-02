<?php
session_start();
if(isset($_GET['id'])){
$cred=explode("-",$_GET['id']);
$_SESSION['facid']=$cred[0];
$_SESSION['slot']=$cred[1];}

?>




<!DOCTYPE html>
<html>
<head>
  <title>Faculty</title>
</head>
<body>


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