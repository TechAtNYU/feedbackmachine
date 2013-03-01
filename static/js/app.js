var pages = {},
    current_page = null;

function start () {
  var pathname = window.location.pathname;
  var page = pathname.split('/').slice(0,2).join('/');
  if (current_page) current_page.cleanup();
  current_page = pages[page];
  current_page.init();
}

$(window).on('push', start);

$(start);
