// 获取模态框、添加按钮和关闭按钮
var modal = document.getElementById("add-website-modal");
var addButton = document.getElementById("add-website-button");
var closeButton = document.getElementById("close-modal");

// 当用户点击添加按钮时显示模态框
addButton.onclick = function() {
    modal.style.display = "block";
}

// 当用户点击关闭按钮或模态框外部时隐藏模态框
closeButton.onclick = function() {
    modal.style.display = "none";
}

