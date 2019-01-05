$(function(){
	
	$('input').each(function(){
		$(this).focus(function(){
			
			$(this).css('borderColor','#7ABD54');
		});
		$(this).blur(function(){
			$('input').css('borderColor','');
		});
	});

	
	//******************************* 	登录页面		*******************************
  	// 账号的验证
    $("#account").blur(function(){  
        reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//验证手机正则(输入前7位至11位)  
  
            if( $(this).val()==""|| $(this).val()=="请输入手机号"){  
        	
            $(this).next().next().find('.error_Prompt').text("请输入手机号");  
            $(this).next().next().css("display","block"); 
            $(this).next().css("display","none"); 
            
        }else if( $(this).val().length<11){ 
        	
            $(this).next().next().find('.error_Prompt').text("手机号码长度有误！");  
            $(this).next().next().css("display","block");
            $(this).next().css("display","none");
            
        } else if(!reg.test($("#account").val())){   
        	
            $(this).next().next().find('.error_Prompt').text("手机号不存在!");  
           	$(this).next().next().css("display","block");
           	$(this).next().css("display","none");
           	
        }else{  
        	
        	$(this).next().next().css("display","none");
            $(this).next().css("display","block");    
        }   
    }); 
  	
  	//密码的验证
 	$("#passWord").blur(function(){
 		reg=/^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,22}$/;  
 		
 		 if( $(this).val()==""|| $(this).val()=="请输入密码"){
 		 	$(this).next().next().find('.error_Prompt').text("密码不能为空！");  
           	$(this).next().next().css("display","block");
           	$(this).next().css("display","none");
           	
 		 } else if(!reg.test($("#passWord").val())){  
        	
        	$(this).next().next().find('.error_Prompt').text("密码格式有误，支持6~12位的数字、字母或特殊字符！");  
            $(this).next().next().css("display","block"); 
            $(this).next().css("display","none"); 

        }else{  
        	
            $(this).next().next().css("display","none");
            $(this).next().css("display","block");   
        } 
 	});
 	
 	 //验证码栏失去焦点  
    $("#verification").blur(function(){  

		//var code1=$('#img_code').text().toLowerCase();  
        var code1 =$("#verification").val().toLowerCase(); 
		
		var code2 = $('#img_code img').attr('code').toLowerCase(); 

        if(code1!=code2){  

        	$(this).next().next().find('.error_Prompt').text("验证码输入错误！");  
            $(this).next().next().css("display","block"); 
            $(this).next().css("display","none"); 
 
	        }else{  
	        	
	            $(this).next().next().css("display","none");
            	$(this).next().css("display","block"); 
        }
        if( $(this).val()=="" || $(this).val()=="请输入验证码")  
                {  
                    $(this).next().next().find('.error_Prompt').text("验证码为空！");  
	                $(this).next().next().css("display","block"); 
	                $(this).next().css("display","none");  
                } 

    }); 
 	
  	function changeCodeimg(){
  		var arr=[
  			'<img src="../../images/login/yanZhengCodeNew1.ashx.png" code="1t3z" />',
  			'<img src="../../images/login/yanZhengCodeNew2.ashx.png" code="ax9r" />',
  			'<img src="../../images/login/yanZhengCodeNew3.ashx.png" code="zpcr" />',
  			'<img src="../../images/login/yanZhengCodeNew4.ashx.png" code="pbnf" />',
  			'<img src="../../images/login/yanZhengCodeNew5.ashx.png" code="uz3j" />',
  			'<img src="../../images/login/yanZhengCodeNew6.ashx.png" code="wilr" />',
  			'<img src="../../images/login/yanZhengCodeNew7.ashx.png" code="ub1s" />',
  			'<img src="../../images/login/yanZhengCodeNew8.ashx.png" code="4bpm" />',
  			'<img src="../../images/login/yanZhengCodeNew9.ashx.png" code="16kc" />',
  			'<img src="../../images/login/yanZhengCodeNew10.ashx.png" code="x3bb" />',
  			'<img src="../../images/login/yanZhengCodeNew11.ashx.png" code="t2mm" />',
  			'<img src="../../images/login/yanZhengCodeNew12.ashx.png" code="mjwz" />',
  			'<img src="../../images/login/yanZhengCodeNew13.ashx.png" code="4ksb" />',
  			'<img src="../../images/login/yanZhengCodeNew14.ashx.png" code="zn44" />',
  			'<img src="../../images/login/yanZhengCodeNew15.ashx.png" code="9lms" />'
  		
  		];
  		var i = parseInt(Math.random()*15+1)
  		$("#img_code").html(arr[i]);
  	}
  	changeCodeimg();
  	 
    $(".changeImg").click(function(){  
        changeCodeimg(); 
    });
  	

	
	//*******************************	注册页面		**********************************

	//其他与上面相同	

	//确认密码失去焦点  
    $("#passWord2").blur(function(){  
        var pwd1=$('#passWord').val();  
        var pwd2=$(this).val();  
        if(($(this).val() == '请再次输入密码' || $(this).val() == "") && (pwd1 == "请输入密码" || pwd1 == "") ){                      
                return;  
        }else if(pwd1!=pwd2){    
            $(this).next().next().find('.error_Prompt').text("两次密码输入不一致！");  
            $(this).next().next().css("display","block"); 
            $(this).next().css("display","none");   
        }  
        else{  
            $(this).next().next().css("display","none");
            $(this).next().css("display","block"); 
        }  
    }); 





	
	
});
	
	
	