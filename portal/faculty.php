
<?php
session_start();
echo"home page ".$_SESSION["userid"]." ".$_SESSION['category'];
?>

<!DOCTYPE html>
<html>
<head>
  <title>Faculty</title>
</head>
<body>

<h2>Slot Details</h2>

<table border="2">
  <tr>
    <td>Sr.No.</td>

    <td>Slot</td>

    <td>Action</td>
  </tr>

<?php

include "dbconnect.php"; // Using database connection file here

$records = mysqli_query($conn,"select * from faculty_slot"); // fetch data from database
$i=1;
while($data = mysqli_fetch_array($records))
{
?>
  <tr>
    <td><?php echo $i++; ?></td>

    <td><?php echo $data['slot']; ?></td>    
  
 
    <td><a href="fatdv.php?id=<?php echo $data['facid']."-".$data['slot']; ?>">Process</a></td>

  </tr>	
<?php
}
?>
</table>

</body>
</html>