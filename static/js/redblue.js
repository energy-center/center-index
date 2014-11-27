// JavaScript Document
$(function(){
	$('li').click(function(){
		setYanse(this.id);
});
		$(function(){var my=$.cookie("myskin");
			if(my)
			{ 
			
			setYanse(my);
			};
		});
			function setYanse(idd){
			$('#'+idd).addClass('current').siblings().removeClass('current');
			$('#yanse').attr('href','../css/'+idd+'.css');
			$.cookie("myskin",idd,{ path: '/', expires: 10 });
				}
			});				

