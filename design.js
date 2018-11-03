var $form = $("#data");

var $button = $('a');
$form.on('submit', function(event) {
  event.preventDefault();
  var duration = 0.3,
      delay = 0.08;
  // TweenMax.to($button, duration, {scaleY: 1.6, ease: Expo.easeOut});
  // TweenMax.to($button, duration, {scaleX: 1.2, scaleY: 1, ease: Back.easeOut, easeParams: [3], delay: delay});
  // TweenMax.to($button, duration * 1.25, {scaleX: 1, scaleY: 1, ease: Back.easeOut, easeParams: [6], delay: delay * 3 });
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
