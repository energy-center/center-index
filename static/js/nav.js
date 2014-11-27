// JavaScript Document
$(function(){
//$('.nav li').find("dl").hide();
$('.nav li').hover(function(){$(this).find("dl").show()},function(){$(this).find("dl").hide()});
$('.nav dl').hover(function(){$(this).parent().css("color",".fff")},function(){$(this).parent().css("color",".f00")});
//$('.nav li').hover(function(){$(this).find("dl").attr("display","block")},function(){$(this).find("dl").attt("display","none")});
})