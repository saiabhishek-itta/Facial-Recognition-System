
<?php
session_start();
if(!isset($_SESSION["userid"]))
header("Location: http://localhost/attend%20-%20Copy/portal/signin.php", true, 301);
#echo"home page ".$_SESSION["userid"]." ".$_SESSION['category'];
?>

<!DOCTYPE html>
<html>
<head>
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
  <title>Faculty</title>
</head>



















<body>
<div id="head">
  <a style{align:left;} href="logout.php">Logout</a>
</div>

<div id="cont">
<center>
<h2>Your Courses</h2>

<table border="4">
  <tr>
    <th><b>Sr.No.</b></td>

    <th><b>Slot</b></td>
    <th><b>Course Name</b></td>
    <th><b>Action</b></td>
  </tr>

<?php

include "dbconnect.php"; // Using database connection file here
$id=$_SESSION["userid"];
$records = mysqli_query($conn,"select * from faculty_slot where facid='$id'"); // fetch data from database
$i=1;
while($data = mysqli_fetch_array($records))
{
?>
  <tr>
    <td><?php echo $i++; ?></td>

    <td><?php echo $data['slot']; ?></td>    
    <td><?php echo $data['coursename']; ?></td> 
 
    <td><a href="fatdv.php?id=<?php echo $data['facid']."-".$data['slot']; ?>">Process</a></td>

  </tr>	
<?php
}
?>
</table>


</div>

</body>
</html>