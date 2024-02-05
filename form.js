function myfun()
{
let fname=document.getElementById('fname').value;
let lname=document.getElementById('lname').value;
let email=document.getElementById('email').value;
let phone=document.getElementById('phone').value;
let password=document.getElementById('password').value;
let cpass=document.getElementById('cpass').value;
let abc=/^[a-zA-z]+$/;
let checklast=/^[a-zA-z]+$/;
let remail=/^[a-zA-z]+[@][a-zA-z]+[.][a-zA-z]+$/;
let rmob=/^[789][0-9]{9}+$/;
let rpass=/^[a-zA-Z0-9!@#$%^&*]$/;
if(abc.test(fname))
{
    document.getElementById('usererror').innerHTML=" ";
}
else
{
     document.getElementById('usererror').innerHTML="Invalid Name ";
     return false;
}
if(checklast.test(lname))
{
    document.getElementById('uerror').innerHTML=" ";
}
else
{
     document.getElementById('uerror').innerHTML="Invalid Name ";
     return false;
}
if(remail.test(email))
{
    document.getElementById('eerror').innerHTML=" ";
}
else
{
     document.getElementById('eerror').innerHTML="Invalid email ";
     return false;
}
if(rmob.test(phone))
{
    document.getElementById('merror').innerHTML=" ";
}
else
{
     document.getElementById('merror').innerHTML="Invalid Mobile Number ";
     return false;
}
if(rpass.test(password))
{
    document.getElementById('perror').innerHTML=" ";
}
else
{
     document.getElementById('perror').innerHTML="Invalid Password ";
     return false;
}
if(password.match(cpass))
{
    document.getElementById('cerror').innerHTML=" ";
}
else
{
     document.getElementById('cerror').innerHTML="Password Doesn't match";
     return false;
}
alert("Submitted Successfully");
}