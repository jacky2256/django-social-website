(function(){
  console.log('I am here 1');
  if(!window.bookmarklet) {
    console.log('I am here 2');
    let bookmarklet_js = document.body.appendChild(document.createElement('script'));
    bookmarklet_js.src = 'https://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*9999999999999999);
    window.bookmarklet = true;
  }
  else {
    bookmarkletLaunch();
  }
})();