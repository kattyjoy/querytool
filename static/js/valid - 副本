
var MMSIArray = new Array(0);

function DMSToDec(degree,minute,second){
  return degree+(minute/60.0)+(second/3600.0);
}
 
function DecToDMS(num){
  value = Math.abs(num);  
  var v1 = Math.floor(value);//度  
  var v2 = Math.floor((value - v1) * 60);//分  
  var v3 = Math.floor(((value - v1) * 60 - v2) * 60) ;//秒  
       
  return new Array(v1,v2,v3);
}

function showError(obj,msg){ 
  obj.closest(".wrapdiv").find(".errorinfo").text(msg);
  obj.closest(".wrapdiv").find(".errorinfo").show();
  obj.closest(".wrapdiv").addClass("has-error");
}
function hideError(obj){
  obj.closest(".wrapdiv").find(".errorinfo").hide();
  obj.closest(".wrapdiv").removeClass("has-error");
}

function deleteButtonBind(){
	$(this).parent().parent().remove();
	var length = String($("#timelisttable").find("tr").length);
	if(length == "0"){
		length = ""
	}
	$("#timeindexcount").text(length);


	var length = String($("#regionlisttable").find("tr").length);
	if(length == "0"){
		length = ""
	}
	$("#regionindexcount").text(length);
}

function makeupPoint(lngcmp,latcmp){
  var degstr = $(lngcmp).val();
  if(Number(degstr) < 0){
    degstr +="° W , ";
  }else
  degstr +="° E , ";
  content = degstr;
  degstr = $(latcmp).val();
  if(Number(degstr) < 0){
    degstr +="° S";
  }else
  degstr +="° N";
  content += degstr;
  return content;
}

function makeupType0Row(trobj){
  var x1 = $("#l0lngcmp").val();
  var y1 = $("#l0latcmp").val();
  var x2 = $("#vertical").val();
  var y2 = $("#horizontal").val();
  var tdstr = "<td style='vertical-align:middle'></td>";
  trobj.append($(tdstr).html("左上:"+makeupPoint("#l0lngcmp","#l0latcmp")));
  trobj.append($(tdstr).html("长: "+$("#vertical").val()+"km"));
  trobj.append($(tdstr).html("宽: "+$("#horizontal").val()+"km"));
  trobj.data("ptfirst",x1+","+y1);
  trobj.data("ptsecond",x2+","+y2);
}
function makeupType1Row(trobj){
  var x1 = $("#l1lngcmp").val();
  var y1 = $("#l1latcmp").val();
  var x2 = $("#r1lngcmp").val();
  var y2 = $("#r1latcmp").val();
  var tdstr = "<td style='vertical-align:middle'></td>";
  trobj.append($(tdstr).html("左上:"+makeupPoint("#l1lngcmp","#l1latcmp")));
  trobj.append($(tdstr).html("右下:"+makeupPoint("#r1lngcmp","#r1latcmp")));
  trobj.data("ptfirst",x1+","+y1);
  trobj.data("ptsecond",x2+","+y2);
}
function makeupType2Row(trobj){
  var x1 = $("#c2lngcmp").val();
  var y1 = $("#c2latcmp").val();
  var x2 = $("#radiuscircle").val();
  var tdstr = "<td style='vertical-align:middle'></td>";
  trobj.append($(tdstr).html("圆心:"+makeupPoint("#c2lngcmp","#c2latcmp")));
  trobj.append($(tdstr).html("半径: "+$("#radiuscircle").val()+"km"));
  trobj.data("ptfirst",x1+","+y1);
  trobj.data("ptsecond",x2+",0");
}




function validDate(){
	starttime = Date.parse($("input#start").val());
	endtime = Date.parse($("input#end").val());
	if(starttime > endtime){
	  showError($("input#start"),"开始时间应早于结束时间");
	  return false;
	}
	hideError($("input#start"));
	return true;
}

function validPosition(){
  $("#positionset").find(".wrapdiv").find(":input:visible:enabled").triggerHandler("blur");
  if($("#positionset").find(".wrapdiv.has-error:visible").length){
    return false;
   }
  var count = 0;
  $("#positionset").find(".wrapdiv").find(":input:visible:enabled").each(function(){
    if($(this).val() == ""){
  	  showError($(this),"不应为空");
	  count++;
	}
  });
  if(count){
    return false;
  }
  return true;
}

function validShip(){
  $("#shipmmsi").triggerHandler("blur");
  if($("#shipset").find(".wrapdiv.has-error:visible").length){
    return false;
  }
  if($("#shipmmsi").attr("disabled") != "disabled"){
    if((MMSIArray.length == 0) && ($("#shipmmsi").val() == "")){
      showError($("#shipmmsi"),"应至少输入一个MMSI");
      return false;
    }
  }
  if($("#shipset").find(".wrapdiv.has-error:visible").length){
    return false;
  }
  //  $("#shipset").find(".wrapdiv").find(":input:visible:enabled").triggerHandler("blur");
 //  if($("#shipset").find(".wrapdiv.has-error:visible").length){
 //    return false;
 //  }
 //  var count = 0;
 //  $("#shipset").find(".wrapdiv").find(":input:visible:enabled").each(function(){
 //    if($(this).val() == ""){
 //  	  showError($(this),"不应为空");
	//   count++;
	// }
 //  });
 //  if(count){
 //    return false;
 //  }
  
 //  if(!("#loadmmsi").attr("disabled")){
 //    alert("");
 //  }


  return true;
}

function makeupDateJSON(){
  
  var datejsonstr = '[';
  $("#timelisttable").find("tr").each(function(){
  	datejsonstr += '"'+$(this).data("starttime")+',';
  	datejsonstr += ''+$(this).data("endtime")+'"';
  	datejsonstr += ','
  });
  if(datejsonstr != '[')
    //去掉末尾多余的,
    datejsonstr = datejsonstr.slice(0,-1);
  datejsonstr += ']';
  return datejsonstr;
}
function makeupPositionJSON(){
  var posjsonstr = '[';
  $("#regionlisttable").find("tr").each(function(){
  	posjsonstr += '{';
  	posjsonstr += '"postype":"'+$(this).data("postype");
  	if($(this).data("postype") == 'geo'){
      posjsonstr += '","tp":'+$(this).data("tp")+',';
      posjsonstr += '"pt1":"'+$(this).data("ptfirst")+'",';
      posjsonstr += '"pt2":"'+$(this).data("ptsecond")+'"';
  	}else if($(this).data("postype") == 'port'){
      posjsonstr += '","name":"'+$(this).data("portname")+'"';
  	}
  	posjsonstr += '}';
  	posjsonstr += ',';

  });
  //去掉末尾多余的,
  if(posjsonstr != '[')
    posjsonstr = posjsonstr.slice(0,-1);
  posjsonstr+=']';
  return posjsonstr;	
}
function makeupShipMMSIJSON(){
  var mmsijsonstr = '[';
  if($("#shipmmsi").attr("disabled") != "disabled"){
    if($("#shipmmsi").val()!= ""){
      inputarray = $("#shipmmsi").val().split(",");
      for(var i= 0;i < inputarray.length;i++){
        if(inputarray[i] !="")
          mmsijsonstr +='"'+inputarray[i]+'",';
      }
    }
  	//  mmsijsonstr += '"'+$("#shipmmsi").val()+'",';
    for (var i = 0;i < MMSIArray.length;i++){
      mmsijsonstr += '"'+MMSIArray[i]+'",';
    }
  }
  if(mmsijsonstr != "[")
    //去掉末尾多余的,
    mmsijsonstr = mmsijsonstr.slice(0,-1);
  mmsijsonstr+=']';
  return mmsijsonstr;
}
function makeupShipCountryJSON(){
  var countryjsonstr = '['
  if($("#shipcountry").attr("disabled") != "disabled"){
 //  countryarray =  $('shipcountry').find("option[selected='selected']").val()
    countryarray = $('#shipcountry').selectpicker('val');
    for (var i=0;i< countryarray.length;i++)
  	  countryjsonstr += '"'+countryarray[i]+'",';
  };
  if(countryjsonstr != "[")
    //去掉末尾多余的,
    countryjsonstr = countryjsonstr.slice(0,-1);
  countryjsonstr+=']';
  return countryjsonstr;
}
function makeupJSONArray(){
	var jsonstr = '{';
	jsonstr +='"date":'+makeupDateJSON()+ ',';
	jsonstr += '"position":'+makeupPositionJSON()+',';
	jsonstr += '"mmsi":'+makeupShipMMSIJSON()+',';
	jsonstr += '"country":'+makeupShipCountryJSON()+',';
	jsonstr += '"source":"'+$("#datasource").val()+'",';
	jsonstr += '"output":"'+$("#filetype").val()+'"';
	jsonstr += '}';
  console.log(jsonstr);
	return jsonstr;

}


function resetDateSet(){
  var date = new Date();
  var today =String(date.getFullYear()+"/"+(date.getMonth()+1)+"/"+date.getDate())
  $("#timeset").find(".seltime").val(today);
}

function resetPositionSet(){
  $("#geo").addClass("active");
  $("#port").removeClass("active");
  
  $("#positiontab").addClass("active");
  $("#porttab").removeClass("active");

  $("#zonesel").find("li").removeClass("active");
  $("#tp0").addClass("active");

  $("#recgroup1field").addClass("active in");
  $("#recgroup2field").removeClass("active in");
  $("#circlegroupfield").removeClass("active in");

  $("#positionset").find(".realdeg").removeAttr("disabled").val("");
  $("#positionset").find(".length").removeAttr("disabled").val("");
  $("#positionset").find(".intdeg").attr("disabled","disabled").val("");
  $("#positionset").find(".degtoggle").each(function(){
  	$(this).val($(this).data("positive"));
  });
  $("#positionset").find(".dectoggle").each(function(){
  	$(this).html('切换为度分秒输入<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>');
  	$(this).removeClass("active");
  });

  $("#portname").val("");


}
function resetShipSet(){
  $("#mmsitoggle").removeClass("active");
  $("#mmsitoggle").val("不指定MMSI");

  $("#shipmmsi").attr("disabled","disabled").val("");

  $("#loadmmsi").fileinput('disable');
  $("#loadmmsi").fileinput('clear');
  $('#loadmmsi').fileinput('refresh');

  $("#countrytoggle").removeClass("active");
  $("#countrytoggle").val("不指定国籍");
  $('#shipcountry').prop('disabled',true);
  $('#shipcountry').selectpicker('deselectAll');
  $('#shipcountry').selectpicker('refresh');
}

function resetDatabaseSet(){

  $('#datasource').selectpicker('val','hive');
  $('#datasource').selectpicker('refresh');
  $('#filetype').selectpicker('val','csv');
  $('#filetype').selectpicker('refresh');
}

function resetAllSet(){
  resetDateSet();
  resetPositionSet();
  resetShipSet();
  resetDatabaseSet();



  $("#timelisttable").empty();
  $("#regionlisttable").empty();

  $("#timeindexcount").text("");
  $("#regionindexcount").text("");

}

function createMessage(type,title,content,firstbutton,secondbutton){
  var titlespan = $("<span>"+title+"</span>");
  var contentspan = $("<span>"+content+"</span>");
  if(type == "success"){
    titlespan.addClass("text-success");
    contentspan.addClass("text-success");
  }
  else if(type == "info"){
    titlespan.addClass("text-info");
    contentspan.addClass("text-info");
  }
  else if(type == "error"){
    titlespan.addClass("text-danger");
    contentspan.addClass("text-danger");
  }
  $("#msgtitle").empty().append(titlespan);
  $("#msgbody").empty().append(contentspan);
  $("#msgbutton").empty();
  if(firstbutton){
    firstbutton.attr("id","firstb");
    $("#msgbutton").append(firstbutton);
  }
  if(secondbutton ){
    secondbutton.attr("id","secondb");
    $("#msgbutton").append(secondbutton);
  }

}



$(function(){
  $(":radio").click(function(){
    var val=$('input:radio[name="tp"]:checked').val();
    if(val== "0"){
      $("fieldset.recgroup1").slideDown();
	  $("fieldset.recgroup2").hide();
	  $("fieldset.circlegroup").hide();
    }
	else if(val=="1"){
	  $("fieldset.recgroup1").hide();
	  $("fieldset.recgroup2").slideDown();
	  $("fieldset.circlegroup").hide();
	}
	else if(val == "2"){
	  $("fieldset.recgroup1").hide();
	  $("fieldset.recgroup2").hide();
	  $("fieldset.circlegroup").slideDown();
	}

  });         


  $('input.intdeg').blur(function(){
  	if($(this).attr("disabled") =="disabled")
  		return;
  	var thisstr = "#"+$(this).attr("id");
    var prestr = '#'+$(this).attr("id").substr(0,5);
	var degstr = prestr + "deg";
	var minstr = prestr + "min";
	var secstr = prestr + "sec";
	var cmpstr = prestr + "cmp";
	var togstr = prestr + "tog";
	var max = new Number($(this).data("max"));
	if(prestr.substr(3,3) == "lng"){
	  dirstr = prestr + "ewt";
	}
	else {
	  dirstr = prestr + "nst";
	}
	if($(this).val()==""){
	  hideError($(this));
	  return;
  	}
	var inputnum = new Number($(this).val());

	if(isNaN(inputnum) ||  (Math.floor(inputnum) != inputnum)){
	  showError($(this),"请输入整数");
	  $(cmpstr).val("");
	  return;
	}
	if((inputnum > max) || (inputnum < 0)){
	  showError($(this),"应输入0~"+max+"之间的整数");
	  $(cmpstr).val("");
	  return;
	}

	if(($(degstr).val()=="")||($(minstr).val()=="")||($(secstr).val()=="")){
	  $(cmpstr).val("");
	  hideError($(this));
	  return;
	}

	
	if(($(degstr).val() == $(degstr).data("max")) && (thisstr != degstr)){
	  if(inputnum > 0){
	    showError($(this),"度数不应大于"+$(degstr).data("max")+"°");
	    return;
	  }
	}


	var degree = Math.floor(new Number($(degstr).val()));
	var minute = Math.floor(new Number($(minstr).val()));
	var second = Math.floor(new Number($(secstr).val()));
    var value = DMSToDec(degree,minute,second);	
	
	if(($(dirstr).val() == "S") || ($(dirstr).val() == "W")){
	  value = value* -1;
	}
	$(cmpstr).val(value);
  }).keyup(function(){
    $(this).triggerHandler("blur");
  }).focus(function(){
    $(this).triggerHandler("blur");
  });  		
  

  $(".realdeg").blur(function(){
  	if($(this).attr("disabled") =="disabled")
  		return;
  	if($(this).val()==""){
	  hideError($(this));
	  return;
  	}
    var thisstr = "#"+$(this).attr("id");
    var prestr = '#'+$(this).attr("id").substr(0,5);
	var degstr = prestr + "deg";
	var minstr = prestr + "min";
	var secstr = prestr + "sec";
	var cmpstr = prestr + "cmp";
	var togstr = prestr + "tog";
	var max = new Number($(this).data("max"));
	if(prestr.substr(3,3) == "lng"){
	  dirstr = prestr + "ewt";
	}
	else {
	  dirstr = prestr + "nst";
	  lngflag = false;
	}
	var inputnum = new Number($(this).val());

    if(isNaN(inputnum) && ($(this).val()!= '-')){
	  showError($(this),"请输入数字");	
	  $(degstr).val("");
	  $(minstr).val("");
	  $(secstr).val("");
	  return;
	}
	if((inputnum > max) || (inputnum < -max)){
	  showError($(this),"应输入"+-max+"~"+max+"之间的数字");
	  $(degstr).val("");
	  $(minstr).val("");
	  $(secstr).val("");
	  return;
	}
	var vals = DecToDMS(inputnum);
	$(degstr).val(vals[0]);
	$(minstr).val(vals[1]);
	$(secstr).val(vals[2]);
	if(inputnum < 0){
      $(dirstr).val($(dirstr).data("negative"));
	}
	else{
		$(dirstr).val($(dirstr).data("positive"));
	}
	hideError($(this));
	return;

  }).keyup(function(){
    $(this).triggerHandler("blur");
  }).focus(function(){
    $(this).triggerHandler("blur");
  });   

  $('input.directiontoggle').click(function(){
    if($(this).val() == $(this).data("positive")){
      $(this).val($(this).data("negative"));
	}
	else if($(this).val() == $(this).data("negative")){
	  $(this).val($(this).data("positive"));
	}
	var cmpstr = '#'+$(this).attr("id").substr(0,5) + "cmp";
	if($(cmpstr).val() == "")
	  return;
	var presentnum = new Number($(cmpstr).val());
	if(isNaN(presentnum))
	  return;
	$(cmpstr).val(-1*presentnum);
  });


  $('a.dectoggle').click(function(){
	prestr = '#'+$(this).attr("id").substr(0,5);
	degstr = prestr + "deg";
	minstr = prestr + "min";
	secstr = prestr + "sec";
	cmpstr = prestr + "cmp";
	if(prestr.substr(3,3) == "lng")
      dirstr = prestr + "ewt";
	else 
	  dirstr = prestr + "nst"
	
	togstr = prestr + "tog";
	if($(this).html() == '<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>切换为十进制输入'){
	  $(degstr).attr("disabled","disabled").val("");
	  $(minstr).attr("disabled","disabled").val("");				
	  $(secstr).attr("disabled","disabled").val("");
	  $(dirstr).attr("disabled","disabled").val("");
	  $(cmpstr).removeAttr("disabled");
    
    hideError($(degstr));
    hideError($(minstr));
    hideError($(secstr));
	  $(this).html('切换为度分秒输入<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>');
	}
			
	else if($(this).html() == '切换为度分秒输入<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>'){
	  $(degstr).removeAttr("disabled");
	  $(minstr).removeAttr("disabled");				
	  $(secstr).removeAttr("disabled");
	  $(dirstr).removeAttr("disabled");
	  $(cmpstr).attr('disabled','disabled').val("");
    hideError($(cmpstr));
	  $(this).html('<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>切换为十进制输入');
	}

  });


  $("#mmsitoggle").click(function(){
    if($("#shipmmsi").attr("disabled") == "disabled"){
	  $("#shipmmsi").removeAttr("disabled");
	  $(this).text("输入特定MMSI");
	  $(this).removeClass("nommsi");
    $("#loadmmsi").fileinput('enable');
	}
	else{
	  $("#shipmmsi").attr("disabled","disabled");
    $(this).text("不指定MMSI");
	  $("#shipmmsi").val(""); 
	  $(this).addClass("nommsi");
    $("#loadmmsi").fileinput('disable');
	  hideError($("#shipmmsi"));
	}
  });


  $("#countrytoggle").click(function(){
    if($("#shipcountry").attr("disabled") == "disabled"){
	  $("#shipcountry").removeAttr("disabled");
	  $(this).text("选择指定国籍");    
    $('#shipcountry').prop('disabled',false);
    
    $('#shipcountry').selectpicker('refresh');

	}
	else{
	  $("#shipcountry").attr("disabled","disabled");
      $(this).text("不指定国籍"); 
	  hideError($("#shipcountry"));

     $('#shipcountry').prop('disabled',true);
     $('#shipcountry').selectpicker('deselectAll');
     $('#shipcountry').selectpicker('refresh');
	}
  });


  $("#shipmmsi").blur(function(){
  	if($(this).attr("disabled") =="disabled")
  		return;
  	if($(this).val()==""){
  	  hideError($(this));
  	  return;
  	}
    inputarray = $(this).val().split(",");
    for (var i=0;i < inputarray.length;i++){
    if(inputarray[i] == "0"){
      showError($(this),"MMSI编号不应为0");
      return;
    }
    if(inputarray[i] == "" && i != (inputarray.length-1)){
      showError($(this),"MMSI编号不应为空");
      return;
      
    }
    if(inputarray[i].match(/[0-9]*/) != inputarray[i]){
      showError($(this),"请输入字符0~9");
      return;
    }
    if(inputarray[i].length > 10){
      showError($(this),"MMSI编号不应大于10位");
      return;
    }
  
    }
  	  	hideError($(this));
  }).keyup(function(){
    $(this).triggerHandler("blur");
  }).focus(function(){
    $(this).triggerHandler("blur");
  });
		
		
  $("input.length").blur(function(){
  	if($(this).attr("disabled") =="disabled")
  		return;
	len = new Number($(this).val());
    if(isNaN(len)){
      showError($(this),"请输入数字");
      return;
    }
    else if(len < 0){
      showError($(this),"请输入正数");
      return;
    }
    hideError($(this));
  }).keyup(function(){
    $(this).triggerHandler("blur");
  }).focus(function(){
    $(this).triggerHandler("blur");
  });
	
  $("#loadmmsi").on('fileloaded', function(event, file, previewId, index){
    var reader = new FileReader();  
    reader.readAsText(file);
    reader.onload =function(f){
      MMSIArray = this.result.split(/\r?\n/);
    }
  });
  $("#loadmmsi").on('filecleared', function(event){
    MMSIArray.splice(0,MMSIArray.length);

  });




  $("#datebutton").click(function(){
	$("#timepanel").fadeToggle("normal");
  });
  $("#regionbutton").click(function(){
	$("#regionpanel").fadeToggle("normal");
  });

  $(window).bind("resize",function(){
  	$("#timepanelbody,#regionpanelbody").height($(window).height()*0.5);
  	var panelheight = $(".collpanel").height();
	$(".collpanel").css("top",-1*panelheight);
  });
  $("#submitsearch").click(function(){
  	
  	if(!validShip()){
  		//验证船舶信息不通过
      createMessage("error","表单验证不通过","船舶信息输入不正确，请返回检查",
        $('<button class="btn btn-primary" data-dismiss="modal">关闭</button>'),null);
      $("#messagedialog").modal('show');
      window.location.href="#shipset";
      return;
  	}
  	// if($("#timelisttable").find("tr").size() == 0){
  	// 	//没有选定任何时间
   //    createMessage("error","表单验证不通过","应至少选定一个时间",
   //      $('<button class="btn btn-primary" data-dismiss="modal">关闭</button>'),null);
   //    $("#messagedialog").modal('show');
   //    window.location.href="#timeset";
   //    return;
  	// }
  	// if($("#regionlisttable").find("tr").size() == 0){
  	// 	//没有选定任何位置
   //    createMessage("error","表单验证不通过","应至少选定一个位置",
   //      $('<button class="btn btn-primary" data-dismiss="modal">关闭</button>'),null);
   //    $("#messagedialog").modal('show');
   //    window.location.href="#positionset";
  	// 	return;
  	// }
    $(this).text("查询中...");
    $(this).attr("disabled","disabled");
  	var request = $.ajax({
   	  url: "/validquery",
      type: "POST",
      dataType: "json",
      async:false,
      content:"#submitsearch",
      contentType: "application/json", 
      charset:"utf-8",
      timeout:8000,
	    data:makeupJSONArray(),
      success:function (responseText) {
      	//alert(responseText);

        $("#submitsearch").removeAttr("disabled");
        $("#submitsearch").text("提交查询");
        createMessage("success","提交成功","已提交查询，预计N分钟",
        $('<button class="btn btn-default" data-dismiss="modal">关闭</button>'),
        $('<a href="/tasklist"  class="btn btn-primary">查看任务列表</a>'));
        $("#messagedialog").modal('show');

        resetAllSet();
        return;
 	    },
 	    error:function (request,error,event){
        createMessage("error","查询失败","提交失败，服务器返回"+request.responseText,
        $('<button class="btn btn-primary" data-dismiss="modal">关闭</button>'),null);
 		    
        $("#submitsearch").removeAttr("disabled");
        $("#submitsearch").text("提交查询");
 	    }
	});
  	//document.write(makeupJSONArray());
 //    var str = "";
	// $("#timelisttable").find("tr").each(function(){
	// str += "start:"+$(this).data("starttime")+"|end:"+$(this).data("endtime")+"\n"
 //    });
  });


  $("#addtimebutton").click(function(){
  	var starttime = String(Date.parse($("input#start").val())/1000);
  	var endtime = String(Date.parse($("input#end").val())/1000);
  	if(!validDate()){
  	  return;
  	}
	var tr = $("<tr></tr>");
	tr.append("<td style='vertical-align:middle' >"+$("input#start").val()+"~"+$("input#end").val()+"</td>");
	var td = $("<td style='text-align:right'></td>");
	var button = $("<button class='btn btn-danger timeindexbutton' type='button'>删除</button>");
	button.bind("click",deleteButtonBind);
	td.append(button);
	tr.append(td);
	tr.data("starttime",starttime);
	tr.data("endtime",endtime);
	$("#timelisttable").append(tr);

  	$("#datebutton").triggerHandler("click");

	var length = String($("#timelisttable").find("tr").length);
	if(length == "0"){
		length = "";
	}
	$("#timeindexcount").text(length);
	resetDateSet();
  });

  $("#addregionbutton").click(function(){
  	//false means not pass
  	if(!validPosition()){
	  return;
  	}
  	var tr = $("<tr></tr>");
  	var td = $("<td style='text-align:left'></td>");
	var button = $("<button class='btn btn-danger regionindexbutton' type='button'>删除</button>");
	button.bind("click",deleteButtonBind);
	td.append(button);
	tr.append(td);

  	var tdstr = "<td style='vertical-align:middle'></td>";
	tr.data("postype",$("#positiontablist").find("li.active").attr("id"));
  	if(tr.data("postype") == "geo"){
      tr.append($("<th style='vertical-align:middle'></th>").html("按地理区域"));
	  tr.data("tp",$("#zonesel").find("li.active").attr("id").charAt(2));
	  tr.append($(tdstr).html($("#zonesel").find("li.active").text()))
	  if(tr.data("tp") == "0"){
	  	makeupType0Row(tr);
	  }else if(tr.data("tp") == "1"){
	  	makeupType1Row(tr);
	  }else if(tr.data("tp") == "2"){
	  	makeupType2Row(tr);
	  }
  	}
  	else if(tr.data("postype") == "port"){
      tr.append($("<th style='vertical-align:middle'></th>").html("按港口名称"));
      tr.append($(tdstr).html($("#portname").val()));
      tr.data("portname",$("#portname").val());
  	}
	

  	$("#regionlisttable").append(tr);

  	$("#regionbutton").triggerHandler("click");
    var length = String($("#regionlisttable").find("tr").length);
	if(length == "0"){
	  length = ""
	}
	$("#regionindexcount").text(length);
	resetPositionSet();
  });



  $("#fadebutton").click(function(){
    if($("#fadebutton").hasClass("fail")){
 	  $("#queryform").ajaxSubmit(options); 
	  $("#fadebutton").removeClass("fail");
	}
	else if($("#fadebutton").hasClass("success")){
  	  $("#fadebutton").removeClass("success");
	  location.href = "/tasklist";
	}
  });


});

