$(function(){
	//商品详情页 菜单吸顶
	$(window).on("scroll",function(){
		var $scrolltop = $(window).scrollTop();  //滚动条的滚动的距离
		if ($scrolltop>=227) {
			$('#main_nav').addClass('scroll_active');
		}else{
			$('#main_nav').removeClass('scroll_active');
		}
		//商品评论 nav 吸顶
		if($scrolltop>=880){
			$("#pd_conment_right_top").addClass('top_active');
		}else{
			$("#pd_conment_right_top").removeClass('top_active');
		}
	});
	

	//商品详情 侧边栏
	//console.log()
	$('#pd_fixed_nav').find('li').each(function(){
		$(this).hover(function(){
			//console.log($(this))
			$(this).animate({width:94})
			$(this).css('background','#b81c22');
		},
		function(){
			$(this).animate({width:44})
		});
	});
	
	
	//商品详情页 回到顶部
	$('.pd_fixed_nav_li4').on("click",function(){
        $('body,html').animate({scrollTop:0},1000);  
	});
	
	
	//	商品评论nav 点击后样式
	var $conment_btn = $("#pd_conment_right_top>li").not('.pd_top_addcart');
	$conment_btn.on('click',function(){
		$conment_btn.removeClass('top_click');
		$(this).addClass('top_click');
	});
	
	
	
	$(".sell_hot li").each(function(){
		$(this).hover(
			function(){
				
				$(this).find('a').fadeIn()
			},
			function(){
				$(".sell_hot li a").css('display','none')
			}
		);
	});
	
	
	//放大镜  商品详情
	$(".jqzoom").imagezoom();
	$("#thumblist li a").click(function(){
		$(this).parents("li").addClass("tb-selected").siblings().removeClass("tb-selected");
		$(".jqzoom").attr('src',$(this).find("img").attr("mid"));
		$(".jqzoom").attr('rel',$(this).find("img").attr("big"));
	});
	
	
	//商品详情  百分比
	$(function(){
		$('#myStat').circliful();
	})
	
	
	//商品详情 侧边栏 收藏 加入购物车
	$(".pic_a").each(function(index){
		$(this).hover(
			function(){
				$(this).find('span').css('display','block');
			},
			function(){
				$(this).find('span').css('display','none');
			}
		);
	});
	
	
	//商品详情 侧边栏 弹出 隐藏 效果
	$('.Xbtn').on('click',function(){
		$('#pd_right_nav').animate({right:-270},1000);
		$(".fixed_nav").find('span').css('background','');
	});
	$(".fixed_nav").each(function(index){
		$(this).on('click',function(){
			$('#pd_right_nav').animate({right:0},1000);
			
			$(".shop_area").each(function(){
				$(".shop_area").css('display','none');
				$(".shop_area").eq(index).css('display','block');
				
			});
			
			$('.fixed_nav span').css('background','');
			$(this).find('span').css('background','rgb(184, 28, 34)');
		});
	});
	
	
	//加入购物车 移入后侧边栏小效果
	$('.add_btn').hover(
		function(){
			$(".pd_fixed_nav_li1 span").css('background','#b81c22');
			$(".pd_fixed_nav_li1").animate({width:94})
		},
		function(){
			$(".pd_fixed_nav_li1 span").css('background','');
			$(".pd_fixed_nav_li1").animate({width:44})
		}
	);
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	var cart_offset = $(".pd_fixed_nav_li1").offset();
	//var btn_offset = $(".add_btn").offset();
	
	$(".add_btn").click(function(event){
		var $scrolltop = $(window).scrollTop();

		var img = $('.tb-booth').find('img').attr('src');
		var flyer = $('<img class="u-flyer" src="'+img+'">');
		flyer.fly({
			start: {
				left: event.pageX,
				top: event.pageY-$scrolltop-10
			},
			end: {
				left: cart_offset.left,
				top: cart_offset.top,
				width: 0,
				height: 0
			},
			onEnd: function(){
				
			}
		});
	});
	
	
	
	
	
	
	
	
	
	
	
	
});






