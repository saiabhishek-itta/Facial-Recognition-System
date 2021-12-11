<?php
session_start();
if(!isset($_SESSION["userid"]))
header("Location: http://localhost/attend%20-%20Copy/portal/signin.php", true, 301);
if(isset($_GET['id'])){
$cred=explode("-",$_GET['id']);
$_SESSION['facid']=$cred[0];
$_SESSION['slot']=$cred[1];}

$date=0;
if($_SERVER["REQUEST_METHOD"] == "POST"){


  if(isset($_POST['viewbtn'])){
  $date=$_POST['date'];
  $cred=explode("-",$date);
  $date=$cred[2]."-".$cred[1]."-".$cred[0];}


  if(isset($_POST['addbtn']) && isset($_POST['date']) ){
    include "dbconnect.php";
  $facid=$_SESSION['facid'];$slot=$_SESSION['slot'];
  $date=$_POST['date'];$stdid=$_POST['stdid'];
  $cred=explode("-",$date);
  $date=$cred[2]."-".$cred[1]."-".$cred[0];

  $sql = "INSERT INTO atd (facid, slot, stdid,date,time)
            VALUES ('$facid', '$slot', '$stdid','$date','-')";
  if ($conn->query($sql) === TRUE) {
    #echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }
  }
}
?>




<!DOCTYPE html>
<html>
<head>
  <title>Faculty</title>
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
</head>

<div id="head">
  <a style{align:left;} href="logout.php">Logout</a>
</div>

<body>
<div id='formid'>
<form action="fatdv.php" method="post">
<h2><?php echo('Slot - '.$_SESSION['slot']." ");?>Attendence Details</h2>

<label for="username">Choose Date :</label>
		<input type="date" class="form-control" id="date"name="date" style="width:20%;"><br>
    <input type="submit" name="viewbtn" value="View Attendence" class="btn btn-primary"><br><br>
<label for="username">Student ID &nbsp&nbsp :</label>
    <input type="text" class="form-control" id="stdid"name="stdid" style="width:20%;"><br>
        <input type="submit" name="addbtn" value="Add Record" class="btn btn-primary">
 
</form>
</div>
<center>
<br>
<table border="2">
  <tr>
    <th>Sr.No.</td>

    <th>Student ID</td>
    <th>Date</td>
    <th>Time</td>

    <th>Action</td>
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