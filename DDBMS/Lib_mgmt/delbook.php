<?php
require_once "login.php";
session_start();
if(isset($_SESSION['id'])&&isset($_SESSION['pass']))
{
if(isset($_POST['bid']))
{
	$boid=$_POST['bid'];
    $conn=new mysqli($hn,$un,$pw,$db);
    $conn1=new mysqli($hn2,$un2,$pw2,$db);
    if($conn->connect_error) die($conn->connect_error);
    $query="select * from books where id='$boid' ";
    $query1="delete from books where id='$boid' ";
    $result=$conn->query($query);
    $query2="delete from author where id=(select a_id from authorbook where b_id='$boid')";
    
    if(!$result) die($conn->error);
    $rows=$result->num_rows;
    if($rows>0)
    {
        $result1=$conn->query($query1);
        $result=$conn1->query($query2);
        // $conn1->query("commit");
        $conn->query("delete from author where id=(select a_id from authorbook where b_id='$boid')");
        $conn1->query("delete from authorbook where b_id = '$boid'");
        $conn1->query("commit");
        $conn->query("delete from authorbook where b_id = '$boid'");
        echo<<<_end
        <meta http-equiv="refresh" content="0; URL='booklist.php'"/>
_end;
  	}
    else
    {
    	echo"No book with such id is present.";
    	echo"<br> <a href='booklist.php'>Go back</a>";
    }
}
}
?>