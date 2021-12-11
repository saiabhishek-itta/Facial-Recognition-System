
<?php
session_start();
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
  <title>Student</title>
</head>
<body>
<div id="head">
  <a style{align:left;} href="logout.php">Logout</a>
</div>
<center>
<h2>Your Course Details</h2>

<table border="2">
  <tr>
    <td>Sr.No.</td>

    <td>course title</td>

    <td>Slot</td>
    <td>Action</td>
  </tr>

<?php
$id=$_SESSION["userid"];
include "dbconnect.php"; // Using database connection file here

$records = mysqli_query($conn,"select * from std_registration where stdid='$id'"); // fetch data from database
$i=1;
while($data = mysqli_fetch_array($records))
{
  $clsid=$data['classid'];
  $records1 = mysqli_query($conn,"select * from faculty_slot where classid='$clsid'");

  while($data1 = mysqli_fetch_array($records1)){
?>
  <tr>
    <td><?php echo $i++; ?></td>
    <td><?php echo $data1['coursename'];?></td>    
    <td><?php echo $data1['slot']; ?></td>
    <td><a href="satdv.php?id=<?php echo $data1['facid']."-".$data1['slot']; ?>">View Attendance</a></td>
  </tr>	
<?php
  }
}
?>
</table>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>


<canvas id="myChart" style="width:100%;max-width:600px"></canvas>

<script>
/*var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["red", "green","blue","orange","brown"];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
     // backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Attendence Percentage"
    }
  }
});*/
</script>

</body>
</html>