const happy = document.getElementById("happy");
const anger  = document.getElementById("anger");
const disgust = document.getElementById("disgust");
const fear  = document.getElementById("fear");
const sad  = document.getElementById("sad");
const neutral  = document.getElementById("neutral");
const temp = document.getElementById("temp");

function emotion_data(){

  fetch('/d/')
.then(function (response) {
      return response.json();
  })
  .then(function (data) {
      happy.innerHTML = (data.happy).toFixed(2);
      anger.innerHTML = (data.anger).toFixed(2);
      disgust.innerText = (data.disgust).toFixed(2);
      fear.innerText = (data.fear).toFixed(2);
      sad.innerText = (data.sad).toFixed(2);
      neutral.innerText = (data.neutral).toFixed(2);
    
  }).then(function(){
    window.setTimeout(100);
    emotion_data();
  })

}