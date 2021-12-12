// // 轮播图start

$(function(){
    var index = 0;
    setInterval(function(){
        if(index == $(".imgs").length-1){
        index = 0;
        $(".imgs").css("opacity",0);
        $(".imgs").eq(index).css("opacity",1);
        $(".button").css("background-color","#ccc");
        $(".button").eq(index).css("background-color","#fff");
    }
    else{
        index ++;
        $(".imgs").css("opacity",0);
        $(".imgs").eq(index).css("opacity",1);
        $(".button").css("background-color","#ccc");
        $(".button").eq(index).css("background-color","#fff");
    }
    },4000)

$(".prev").click(function(){
    if(index == 0){
        index = $("imgs").length-1;
        $(".imgs").css("opacity",0);
        $(".imgs").eq(index).css("opacity",1);
        $(".button").css("background-color","#ccc");
        $(".button").eq(index).css("background-color","#fff");
    }
    else{
        index--;
        $(".imgs").css("opacity",0);
        $(".imgs").eq(index).css("opacity",1);
        $(".button").css("background-color","#ccc");
        $(".button").eq(index).css("background-color","#fff");
    }
  })
  $(".next").click(function(){
      if(index ==$(".imgs").length-1){
          index = 0;
          $(".imgs").css("opacity",0);
          $(".imgs").eq(index).css("opacity",1);
          $(".button").css("background-color","#ccc");
          $(".button").eq(index).css("background-color","#fff");
      }
      else{
          index++;
          $(".imgs").css("opacity",0);
          $(".imgs").eq(index).css("opacity",1);
          $(".button").css("background-color","#ccc");
          $(".button").eq(index).css("background-color","#fff");
      }
  })
  $(".button").click(function(){
      var indexx =$(this).index();
      index = indexx;
      $(".imgs").css("opacity",0);
      $(".imgs").eq(index).css("opacity",1);
      $(".button").css("background-color","#ccc");
      $(".button").eq(index).css("background-color","#fff");
  })

})
// 轮播图end