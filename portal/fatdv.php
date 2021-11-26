<?php
session_start();
if(isset($_GET['id'])){
$cred=explode("-",$_GET['id']);
$_SESSION['facid']=$cred[0];
$_SESSION['slot']=$cred[1];}

$date=0;
if($_SERVER["REQUEST_METHOD"] == "POST"){
  $date=$_POST['date'];
}
?>




<!DOCTYPE html>
<html>
<head>
  <title>Faculty</title>
</head>
<body>

<form action="fatdv.php" method="post">
<h2><?php echo('Slot - '.$_SESSION['slot']." ");?>Attendence Details</h2>
<label for="username">Choose Date :</label>
		<input type="text" class="form-control" id="date"
			name="date" aria-describedby="emailHelp" style="width:20%;">
            <button type="submit" class="btn btn-primary">
		View
		</button>
</form>

<br>
<table border="2">
  <tr>
    <td>Sr.No.</td>

    <td>Student ID</td>
    <td>Date</td>
    <td>Time</td>

    <td>Action</td>
  </tr>

<?php

include "dbconnect.php";
$facid=$_SESSION['facid'];$slot=$_SESSION['slot'];

$records = mysqli_query($conn,"select * from atd where facid='$facid' and slot='$slot' and date='$date'"); 
$i=1;
while($data = mysqli_fetch_array($records))
{
?>
  <tr>
    <td><?php echo $i++; ?></td>

    <td><?php echo $data['stdid']; ?></td> 
    <td><?php echo $data['date']; ?></td>
    <td><?php echo $data['time']; ?></td>   

    <td><a href="fatdv.php?id=<?php echo $data['facid']."-".$data['slot']; ?>">Delete</a></td>
  </tr>	
<?php
}
?>
</table><br><br>
<a href="faculty.php">Back</a>
</body>
</html>