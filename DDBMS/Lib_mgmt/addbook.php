<?php
session_start();
if(isset($_SESSION['id'])&&isset($_SESSION['pass']))
{
require_once "login.php";
if(isset($_POST['bpubn'])&&isset($_POST['bid'])&&isset($_POST['bname'])&&isset($_POST['baun'])&&isset($_POST['bau1'])&&isset($_POST['bpub'])&&isset($_POST['bgen'])&&isset($_POST['bedi'])&&isset($_POST['bpag'])&&isset($_POST['bpr'])&&isset($_POST['bisbn']))
{
    $id=$_POST['bid'];
    $nam=$_POST['bname'];
    $aut=$_POST['bau1'];
    $pub=$_POST['bpub'];
    $gen=$_POST['bgen'];
    $edi=$_POST['bedi'];
    $pag=$_POST['bpag'];
    $bpr=$_POST['bpr'];
    $isbn=$_POST['bisbn'];
    $aname=$_POST['baun'];
    $pname=$_POST['bpubn'];
    $conn1=new mysqli($hn2,$un2,$pw2,$db);
	$conn=new mysqli($hn,$un,$pw,$db);
    if($conn->connect_error) die($conn->connect_error);

    $ch="select * from books where id='$id' ";
    $r=$conn->query($ch);
    $n=$r->num_rows;    
    if($n==0)
    {
        $query="insert into books values('$id','$nam','$pub','$gen','$edi','$pag','$bpr','$isbn')";
        $result=$conn->query($query);
        $query="insert into authorbook values('$aut','$id')";
        $result=$conn1->query($query);
        $result=$conn->query($query);
        $query="insert into author values('$aut','$aname')";
        $result=$conn1->query($query);
        $query="insert into publisher values('$pub','$pname')";
        $result=$conn1->query($query);
        $query = "commit";
        $conn1->query($query);
            echo<<<_end
        <meta http-equiv="refresh" content="0; URL='booklist.php'"/>
_end;
  }
    else
    {
    	echo"There is some error in the inputs.<br> Book with given details may be already present or author or publisher data may not be present";
    	echo"<br> <a href='booklist.php'>Try Again</a>";
    }
}
}
?>