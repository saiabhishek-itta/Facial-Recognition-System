
<?php
session_start();
echo"home page ".$_SESSION["userid"]." ".$_SESSION['category'];
?>

<!DOCTYPE html>
<html>
<head>
  <title>Student</title>
</head>
<body>

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

    <td><?php echo $data1['coursename']; ?></td>    
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
var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
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
});
</script>

</body>
</html>