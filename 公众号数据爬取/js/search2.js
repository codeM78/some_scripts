
//(这里是可以直接请求接口取到数据，就和直接调用一个testcode.js是一样的)
var test_list = test_list;
var old_value = "";
var highlightindex = -1;   //高亮
//自动完成
function AutoComplete(auto, search, mylist) {
    if ($("#" + search).val() != old_value || old_value == "") {
        var autoNode = $("#" + auto);   //缓存对象（弹出框）
        var carlist = new Array();
        var n = 0;
        old_value = $("#" + search).val();
        for (i in mylist) {
            if (mylist[i].indexOf(old_value) >= 0) {
                carlist[n++] = mylist[i];
            }
        }
        if (carlist.length == 0) {
            autoNode.hide();
            return;
        }
        autoNode.empty();  //清空上次的记录
        for (i in carlist) {
            /* 控制一下显示的个数 */
            if(i>5){
                return;
            }
            var wordNode = carlist[i];   //弹出框里的每一条内容
            var newDivNode = $("<div>").attr("id", i);    //设置每个节点的id值
            newDivNode.attr("style", "font:14px/25px arial;height:25px;padding:0 8px;cursor: pointer;");
            newDivNode.html(wordNode).appendTo(autoNode);  //追加到弹出框
            //鼠标移入高亮，移开不高亮
            newDivNode.mouseover(function () {
                if (highlightindex != -1) {        //原来高亮的节点要取消高亮（是-1就不需要了）
                    autoNode.children("div").eq(highlightindex).css("background-color", "white");
                }
                //记录新的高亮节点索引
                highlightindex = $(this).attr("id");
                $(this).css("background-color", "#ebebeb");
            });
            newDivNode.mouseout(function () {
                $(this).css("background-color", "white");
            });
            //鼠标点击文字上屏
            newDivNode.click(function () {
                //取出高亮节点的文本内容
                var comText = autoNode.hide().children("div").eq(highlightindex).text();
                highlightindex = -1;
                //文本框中的内容变成高亮节点的内容
                $("#" + search).val(comText);
            })
            if (carlist.length > 0) {    //如果返回值有内容就显示出来
                autoNode.show();
            } else {               //服务器端无内容返回 那么隐藏弹出框
                autoNode.hide();
                //弹出框隐藏的同时，高亮节点索引值也变成-1
                highlightindex = -1;
            }
        }
    }
    //点击页面隐藏自动补全提示框
    document.onclick = function (e) {
        var e = e ? e : window.event;
        var tar = e.srcElement || e.target;
        if (tar.id != search) {
            if ($("#" + auto).is(":visible")) {
                $("#" + auto).css("display", "none")
            }
        }
    }
}
$(function () {
    old_value = $("#search_text").val();
    $("#search_text").focus(function () {
        if ($("#search_text").val() == "") {
            AutoComplete("auto_div", "search_text", test_list);
        }
    });
    $("#search_text").keyup(function () {
        AutoComplete("auto_div", "search_text", test_list);
    });
});


// /* 搜索的函数 */
// function _searchfun(params){
//     var search_text = $("#search_text").val();
//     /* 执行ajax调用接口，接口实现的功能是完成搜索和将数据存储到备选的数据库里面 */
//     if (params.componentType === 'series'){
//         if(params.seriesType === 'tree'){
//             var patt = /\d+/ //查找数字
//             if(search_text === patt.exec(params.name) ){
//                 alert(search_text)
//
//
//             }
//
//         }
//     }
// }

