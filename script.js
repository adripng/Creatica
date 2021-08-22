var space = $(".space");
var button = $(".btn");
var states = ['Alaska','Arizona','Arkansas','California','Colorado','Florida','Hawaii','Idaho','Kentucky','Michigan','Minnesota','Montana','Nevada','New Mexico','North Carolina','North Dakota','Ohio','Oregon','South Carolina','South Dakota','Tennessee','Texas','Utah','Virginia','Washington','Wyoming'];

button.on("click", message);
function message() {
  var name = $(".name-input").val();
  var state = states[Math.floor(Math.random() * states.length)];
  space.append(`
    <h2> Hi ${name}, thanks for wanting to learn more! <br> You should find ${state} on the map! </h2>
    <img class="logo-result" src="logo.png">
  `)
  event.target.parentNode.remove();
  event.preventDefault();
}