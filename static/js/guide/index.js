// 获取添加模态框、添加按钮和关闭按钮
var modal = document.getElementById("add-website-modal");
var addButton = document.getElementById("add-website-button");
var closeButton1 = document.getElementById("close-modal1");
// 获取删除模态框、添加按钮和关闭按钮
var dmodal = document.getElementById("delete-website-modal");
var deleteButton = document.getElementById("delete-website-button");
var closeButton2 = document.getElementById("close-modal2");

// 当用户点击添加按钮时显示模态框
addButton.onclick = function() {
    console.log("0");
    modal.style.display = "block";
}


// 当用户点击关闭按钮或模态框外部时隐藏模态框
closeButton1.onclick = function() {
    console.log("1");
    modal.style.display = "none";
}

closeButton2.onclick = function() {
    console.log("2");
    dmodal.style.display = "none";
}


// 当用户点击添加按钮时显示模态框
deleteButton.onclick = function() {
    console.log("3");
    dmodal.style.display = "block";
}

