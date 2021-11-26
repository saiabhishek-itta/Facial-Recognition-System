<?php
	
$showAlert = false;
$showError = false;
$exists=false;
	
if($_SERVER["REQUEST_METHOD"] == "POST") {
	
	include 'dbconnect.php';
	
	$username = $_POST["username"];
	$password = $_POST["password"];
	$category = $_POST["category"];
			
	#$num=0;

	if($category=='student'){
	$sql = "Select * from studentlogin where dbstudentid='$username'and dbstdpassword='$password'";	
	$result = mysqli_query($conn, $sql);
	$num = mysqli_num_rows($result);
	}

	if($category=='admin'){
		$sql = "Select * from adminlogin where dbadminid='$username' and dbadmpassword='$password'";	
		$result = mysqli_query($conn, $sql);
		$num = mysqli_num_rows($result);
	}

	if($category=='faculty'){
		$sql = "Select * from facultylogin where dbfacultyid='$username'and dbfacpassword='$password'";	
		$result = mysqli_query($conn, $sql);
		$num = mysqli_num_rows($result);
	}



	if($num == 0) {
			echo"Credentials Not Found!";
	}
	
if($num>0)
{
	session_start();
	$exists="Username not available";
	$_SESSION['userid']=$username;
	$_SESSION['category']=$category;
	$_SESSION['password']=$password;
	if($category=='admin')
    header("Location: http://localhost/attend%20-%20Copy/portal/admin.php", true, 301);
	if($category=='faculty')
    header("Location: http://localhost/attend%20-%20Copy/portal/faculty.php", true, 301);
	if($category=='student')
    header("Location: http://localhost/attend%20-%20Copy/portal/student.php", true, 301);
    exit();
}
	
}
	
?>
	
<!doctype html>
	
<html lang="en">

<head>

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
	
<body>
	
<?php
	
	if($showAlert) {
	
		echo ' <div class="alert alert-success
			alert-dismissible fade show" role="alert">
	
			<strong>Success!</strong> Your account is
			now created and you can login.
			<button type="button" class="close"
				data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">×</span>
			</button>
		</div> ';
	}
	
	if($showError) {
	
		echo ' <div class="alert alert-danger
			alert-dismissible fade show" role="alert">
		<strong>Error!</strong> '. $showError.'
	
	<button type="button" class="close"
			data-dismiss="alert aria-label="Close">
			<span aria-hidden="true">×</span>
	</button>
	</div> ';
}
		
	if($exists) {
		echo ' <div class="alert alert-danger
			alert-dismissible fade show" role="alert">
	
		<strong>Error!</strong> '. $exists.'
		<button type="button" class="close"
			data-dismiss="alert" aria-label="Close">
			<span aria-hidden="true">×</span>
		</button>
	</div> ';
	}

?>
	
<div class="container my-2 ">
	
	<h1 class="text-center">Online Attendence Portal</h1>
	<form action="signin.php" method="post">

		<div class="form-group">
			<label for="username">User ID :</label>
		<input type="text" class="form-control" id="username"
			name="username" aria-describedby="emailHelp" style="width:20%;">	
		</div>
	
		<div class="form-group">
			<label for="password">Password :</label>
			<input type="password" class="form-control"
			id="password" name="password" style="width:20%;">
		</div>
	
		<div class="form-group">
			<label for="category">Login As :</label><br>
			<input type="radio" id="category1" name="category" value="admin">
			<label for="category1">Admin&nbsp&nbsp</label>
			<input type="radio" id="category2" name="category" value="faculty">
			<label for="category2">Faculty&nbsp&nbsp</label>
			<input type="radio" id="category3" name="category" value="student">
			<label for="category3">Student</label><br>
		 </div>	
	
		<button type="submit" class="btn btn-primary">
		Login In
		</button>

	</form>
</div>
	

	
<script src="
https://code.jquery.com/jquery-3.5.1.slim.min.js"
	integrity="
sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
	crossorigin="anonymous">
</script>
	
<script src="
https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
	integrity=
"sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
	crossorigin="anonymous">
</script>
	
<script src="
https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
	integrity=
"sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
	crossorigin="anonymous">
</script>
</body>
</html>
