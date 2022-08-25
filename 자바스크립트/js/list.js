function add(){
    const reset=document.getElementById('addlist');
    const newAddr=document.getElementsByName("name")[0].value+' , '+document.getElementsByName('tel')[0].value;
    const item=document.createElement('li');
    const txt=document.createTextNode(newAddr);

    item.appendChild(txt);
    reset.appendChild(item);
}

function reset(){
    document.getElementById('addlist').innerHTML="";
}

function chane(){
    body=document.querySelector('body');
    body.setAttribute('style','background-color:yellow');
 //   body.className="bgyellow";
}
