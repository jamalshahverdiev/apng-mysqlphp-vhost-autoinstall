<?php
ini_set('display_errors', 1); //Cixan sehvlerin ekrana cap edilmesini ishe saliriq
$dblocation = "localhost"; //bazanin IP unvani
$dbname = "yenidb"; //qoshulacaq olduqumuz verilenler bazasinin adi
$dbuser = "yeniuser"; //yenidb database ucun username
$dbpasswd = "yenipass"; //sayddb ucun shifre

$dbcnx = @mysql_connect($dblocation, $dbuser, $dbpasswd);
if (!$dbcnx){
    echo "<p>Cox heyif MySQL server ishlemir</p>";
    exit();
}
if (!@mysql_select_db($dbname,$dbcnx)){
    echo "<p>Teesufler olsun ki, verilenler bazasina qoshulmaq mumkun deyil</p>";
    exit();
}
$ver = mysql_query("SELECT VERSION()");
if(!$ver){
    echo "<p>Muraciet sehvi</p>";
    exit();
}
echo mysql_result($ver, 0);
?>
