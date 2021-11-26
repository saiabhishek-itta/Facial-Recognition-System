<?php

$cred=explode("-",$_GET['id']);
echo $cred[0]." ".$cred[1];
?>




<!DOCTYPE html>
<html>
<head>
  <title>Faculty</title>
</head>
<body>




<form action="fatdv.php" method="post">
<h2><?php echo('Slot - '.$cred[1]." ");?>Attendence Details</h2>
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

include "dbconnect.php"; // Using database connection file here

$records = mysqli_query($conn,"select * from atd where facid='$cred[0]' and slot='$cred[1]'"); // fetch data from database
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
</table>

</body>
</html>