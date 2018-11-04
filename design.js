
var API_BASE_URL = 'https://localhost:5005'

function sendGet(route, cb) {
  var url = API_BASE_URL + route;
  $('#requests-content').append('GET ' + url);
  $('#requests-content').append('<br/>');
  $.get(url, function(data) {
    $('#responses-content').append(JSON.stringify(data) + ' (status 200)');
    $('#responses-content').append('<br/>');
    if (cb) cb(data);
  });
}

function sendPost(route, d, cb) {
  var url = API_BASE_URL + route;
  $('#requests-content').append('POST ' + url + ' ' + JSON.stringify(d));
  $('#requests-content').append('<br/>');
  $.post(url, d, function(data) {
    console.log(data)
    $('#responses-content').append('' + JSON.stringify(data) + ' (status 200)');
    $('#responses-content').append('<br/>');
    if (cb) cb(data);
  });
}


var $form = $("#data");

var $button = $('a');
$form.on('submit', function(event) {
  event.preventDefault();
  var duration = 0.3,
      delay = 0.08;
  // TweenMax.to($button, duration, {scaleY: 1.6, ease: Expo.easeOut});
  // TweenMax.to($button, duration, {scaleX: 1.2, scaleY: 1, ease: Back.easeOut, easeParams: [3], delay: delay});
  // TweenMax.to($button, duration * 1.25, {scaleX: 1, scaleY: 1, ease: Back.easeOut, easeParams: [6], delay: delay * 3 });

  console.log($form.serializeArray());
  sendPost("/save",$form.serializeArray(),function () {
    console.log("got here");
  });
  // $.get("/item",function (data) {
  //   console.log(data);
  // })

  //console.log($form.serializeArray());
  $.post("/save",$form.serializeArray(),function () {
    console.log("got here");
  });
  $.get("/item",function (data) {
    console.log(data);
  })

});



// @app.route('/save', methods='POST')
// def hello():
//     return render_template('greeting.html', say=request.form['say'], to=request.form['to'])
