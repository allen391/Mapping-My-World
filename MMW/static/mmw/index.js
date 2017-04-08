var init = function() {
  body = document.getElementsByTagName("body")[0]
  console.log(window.innerHeight);
  body.style.setProperty("height", window.innerHeight + "px");
  // 初始化选择时间的控件
  // $("#date-input").datetimepicker({
  //   format: 'dd-mm-yyyy',
  //   startView: 'year',
  //   minView: 'month',
  // })
}

var login = function() {
	event.target.form.action = "/MMW/login/";
	event.target.form.submit();
}