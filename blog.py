 <!DOCTYPE html>
 <html>

<head>
<link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
<link rel="stylesheet" href="/css/grid.css" type="text/css" media="screen">
<link rel="stylesheet" href="/css/style.css" type="text/css" media="screen">

<title>
Blog Signup Page
</title>
</head>

<H2> Login</H2>
<br>
<fieldset class="grid_10" >
<table cellpadding="8px"  >
<form method="post">
<br>
<tr>
<label>
<h1>DO NOT ENTER Password/register -database not yet safe-</h1>

    <td align="right">User Name</td>
    <td><input type="text" name="username" value="{{username}}"></td>
     <td style="color: red">{{username_error}} </td>
    </tr>

</label>

<tr>
<label>
    <td align="right">Password</td>
    <td><input type="password" name="password" value="{{password}}"></td>
     <td style="color: red">{{password_error}} </td>
</label>
</tr>

</table>
<input type="submit">


</form>
</fieldset>
<HTML>
