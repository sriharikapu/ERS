<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<link rel="icon" type="image/png" href="assets/img/favicon.ico">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<title>TNB REWARD SYSTEM</title>

	<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="assets/css/light-bootstrap-dashboard.css?v=1.4.0" rel="stylesheet"/>


    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet" />


    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/pe-icon-7-stroke.css" rel="stylesheet" />
	<link href="assets/css/leave_management.css" rel="stylesheet" />

</head>
<body onload="bodyLoad();">

<div class="wrapper">
    <div class="sidebar" data-color="orange" data-image="assets/img/sidebar-5.jpg">
    <!--   you can change the color of the sidebar using: data-color="blue | azure | green | orange | red | purple" -->
    	<div class="sidebar-wrapper">
            <div class="logo">
                <a href="http://www.creative-tim.com" class="simple-text">
                    Creative Tim
                </a>
            </div>
            <ul class="nav">
                <li>
                    <a href="dashboard.html">
                        <i class="pe-7s-graph"></i>
                        <p>Dashboard</p>
                    </a>
                </li>
                <li>
                    <a href="user.html">
                        <i class="pe-7s-user"></i>
                        <p>User Profile</p>
                    </a>
                </li>
                <li>
                    <a href="table.html">
                        <i class="pe-7s-note2"></i>
                        <p>Tranasaction List</p>
                    </a>
                </li>
                <li>
                    <a href="typography.html">
                        <i class="pe-7s-news-paper"></i>
                        <p>Reward System</p>
                    </a>
                </li>
                <li>
                    <a href="market.html">
                        <i class="pe-7s-science"></i>
                        <p>HR</p>
                    </a>
                </li>
                <li class="active">
                    <a href="maps.html">
                        <i class="pe-7s-map-marker"></i>
                        <p>Leave Management</p>
                    </a>
                </li>
                <li>
                    <a href="notifications.html">
                        <i class="pe-7s-bell"></i>
                        <p>Notifications</p>
                    </a>
                </li>
				<li class="active-pro">
					<a href="upgrade.html">
						<i class="pe-7s-rocket"></i>
						<p>Marketplace</p>
					</a>
				</li>	
        </div>
	</div>	
    <div class="main-panel">
		<nav class="navbar navbar-default navbar-fixed ">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navigation-example-2">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Leave System</a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav navbar-left">
                        <li>
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-dashboard"></i>
								<p class="hidden-lg hidden-md">Dashboard</p>
                            </a>
                        </li>
                        <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                    <i class="fa fa-globe"></i>
                                    <b class="caret hidden-sm hidden-xs"></b>
                                    <span class="notification hidden-sm hidden-xs">5</span>
									<p class="hidden-lg hidden-md">
										5 Notifications
										<b class="caret"></b>
									</p>
                              </a>
                              <ul class="dropdown-menu">
                                <li><a href="#">Notification 1</a></li>
                                <li><a href="#">Notification 2</a></li>
                                <li><a href="#">Notification 3</a></li>
                                <li><a href="#">Notification 4</a></li>
                                <li><a href="#">Another notification</a></li>
                              </ul>
                        </li>
                        <li>
                           <a href="">
                                <i class="fa fa-search"></i>
								<p class="hidden-lg hidden-md">Search</p>
                            </a>
                        </li>
                    </ul>

                    <ul class="nav navbar-nav navbar-right" id="value_reward">
                        <li>
                           <a href="">
                               <p>Account</p>
                            </a>
                        </li>
                        <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                    <p>
										Dropdown
										<b class="caret"></b>
									</p>

                              </a>
                              <ul class="dropdown-menu">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something</a></li>
                                <li class="divider"></li>
                                <li><a href="#">Separated link</a></li>
                              </ul>
                        </li>
                        <li>
                            <a href="#">
                                <p>Log out</p>
                            </a>
                        </li>
						<li class="separator hidden-lg hidden-md"></li>
                    </ul>
                </div>
            </div>
        </nav>
		<br/>		
		<div class="container">
			<ul class="nav nav-tabs" style="margin-left:-58px">
				<li class="nav-item">
				  <a class="nav-link active" href="#" id="color_change">Main</a>
				</li>
				<li class="nav-item">
				  <a class="nav-link" href="#">Actions</a>
				</li>
				<li class="nav-item">
				  <a class="nav-link" href="#">Activity</a>
				</li>
			  </ul>
		</div>
				<!--<div class="hr_border">
					<h4 class="heading_emp">Employee Leave</h4>
					<!--<img src="assets/img/emp.jpg" class="rounded emp_img" alt="Employee">
					<div class="row">
						<div class="col-md-8">
							<div class="col-md-3">
								<img src="assets/img/emp.jpg" class="rounded emp_img" alt="Employee">
							</div>
							<div class="col-md-5 ">
								<br/>
								<br/>
								<h6>Employee Name-</h6>
								<br/>
								<h6>Employee Designation-</h6>
							</div>
						</div>
					</div>
				</div>
				-->
				<br/>
				<br/>
				<div style="margin-left:10px" >
					<table class="table" align="center">
					  <thead>
						<tr>
						  <th>Code</th>
						  <th>Leave Type</th>
						  <th>No of leaves</th>
						</tr>
					  </thead>
					  <tbody>
						<tr>
						  <th>AL</th>
						  <td>Annual Leave</td>
						  <td>14</td>
						</tr>
						<tr>
						  <th>CO</th>
						  <td>Comp Off</td>
						  <td>1</td>
						</tr>
						<tr>
						  <th>SL</th>
						  <td>Sick Leave</td>
						  <td>8</td>
						</tr>
					  </tbody>
					</table>
				</div>
    </div>
</div>


</body>

        <!--   Core JS Files   -->
    <script src="assets/js/jquery.3.2.1.min.js" type="text/javascript"></script>
	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<!--  Charts Plugin -->
	<script src="assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="assets/js/bootstrap-notify.js"></script>

    <!--  Google Maps Plugin    -->
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>

    <!-- Light Bootstrap Table Core javascript and methods for Demo purpose -->
	<script src="assets/js/light-bootstrap-dashboard.js?v=1.4.0"></script>

	<!-- Light Bootstrap Table DEMO methods, don't include it in your project! -->
	<script src="assets/js/demo.js"></script>
	<!-- <script src="assets/js/leave_management.js"></script> -->
	<script>
		function bodyLoad(){
			colorChange();
			reward_details();
		}
		function colorChange() {
			var color = $("#color_change").css("color")
			if (color == "rgb(29, 199, 234)"){
				$("#color_change").addClass("myLabel")
			}
		}
		function reward_details(){
			$.getJSON("https://api.etherscan.io/api?module=account&action=balance&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&tag=latest&apikey=Y5FHVYEZRBH3VHB263GQ3IIIBM1CQRAYWK",function(result){
				$.each(result,function(i,field){
					if (i == "result") {
							var value = field/1000000000000000000 
							var n = value.toFixed(2);
							$("#value_reward").append('<li><a href="typography.html"><p>Balance -'+n+'</p></a></li>')
					}
					
				});
			});
		}
	</script>
	
</html>
