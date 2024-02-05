
function myfun() {
    let a = document.getElementById("two").value;
    let b = document.getElementById("two").value;
    let c = document.getElementById("two").value;
    let d = document.getElementById("two").value;
    let e = document.getElementById("two").value;
    //for emails verfication
    let pat1 = /[a-z][@][a-z][.com]/;
    if (pat1.test(a))
        alert("Pass")
    else
        alert("Fail")
    //for first name and last name verification
    let pat2 = /[a-zA-Z]/;
    if (pat2.test(b))
        alert("Pass")
    else
        alert("Fail")
    if (pat2.test(c))
        alert("Pass")
    else
        alert("Fail")
    //for prn validation
    let pat3 = /[a-zA-Z0-9]/;
    if (pat3.test(d))
        alert("Pass")
    else
        alert("Fail")

    //for feedback
    pat4=/[a-zA-Z]/
    if (pat4.test(e))
        alert("Pass")
    else
        alert("Fail")
}
