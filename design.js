
var API_BASE_URL = 'http://localhost:5005'

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

  console.log($form.serializeArray());
  sendPost("/save",$form.serializeArray(),function () {
    console.log("got here");
  });
  //document.getElementById("button").onclick = function () {
    //    location.href = "output.html";
    //};
  // $.get("/item",function (data) {
  //   console.log(data);
  // })

  //console.log($form.serializeArray());
  // $.post("/save",$form.serializeArray(),function () {
  //   console.log("got here");
  // });



});



// @app.route('/save', methods='POST')
// def hello():
//     return render_template('greeting.html', say=request.form['say'], to=request.form['to'])
