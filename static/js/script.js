$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.timepicker').timepicker({});
    $(".datepicker").datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }

    })
    
  });