var imglist = new Array(
    "images/Huku.jpg",
    "images/Ajisai.jpg",
);
    
var selectnum = Math.floor(Math.random() * imglist.length);
var output = "<img src=" + imglist[selectnum] + ">";
document.write(output);