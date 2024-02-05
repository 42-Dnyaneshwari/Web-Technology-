function myfun_create()
{
    let t=document.createElement("h2");
    //creating h2 tag
    t.innerHTML="Welcome to the WT CIA-test";
    let o=document.getElementById("one");
    o.appendChild(t);
    //to modify aggrement
    t.setAttribute("id","head1");
    alert(document.getElementById("head1"));
    //changning background color of the text having id 
    t.style.backgroundColor="green";
    t.style.color="white";
    

}

function myfun_remove()
{
    //removing button
    let p=document.getElementById("head1");
    p.parentNode.removeChild(p);
}

