$(document).ready(function () {
  $('.collapsible').collapsible();


 /* HOME PAGE   */
  function fixDivIndex() {
    var $cache = $('.menu_flutua');
    if ($(window).scrollTop() > 200)
      $cache.css({
        'position': 'fixed',
        'top': '60px'

      });
    else
      $cache.css({
        'position': 'fixed',
        'top': '400px'
      });
  }
  $(window).scroll(fixDivIndex);
  fixDivIndex();


  /* PÁGINAS INTERNAS  */
    function fixDiv() {
    var $cache = $('.box_portlet_pagina');
    if ($(window).scrollTop() > 200)
      $cache.css({
        'position': 'fixed',
        'top': '90px'

      });
    else
      $cache.css({
        'position': 'fixed',
        'top': '90px'
      });
  }
  $(window).scroll(fixDiv);
  fixDiv();




});


function sim() {

  $('#feedback-nao').prop('disabled', true);
  $('#feedback-sim').text('Sim. Obrigado!').css('color', '#444444');
  $('#feedback-sim').css({'background-color': '#EAF1DF', 'border': '3px solid #444444'});
  $('#feedback-text-agradecimento').show();

}

function nao() {

      $('#feedback-sim').prop('disabled', true);
      $('#feedback-nao').css({
        'background-color': '#EAF1DF',
        'color': '#444444', 'border': '3px solid #444444'});
      $('#feedback-text').show();


  }

