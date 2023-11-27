// Init the Notify Module
Notiflix.Notify.Init({});


// Demos
var mainDiv = document.querySelectorAll('.notify');
for (var i = 0; i < mainDiv.length; i++) {
  var self = mainDiv[i];   
  var divClass = self.classList[1];
  var button = document.getElementsByClassName('button-'+divClass)[0];
  
  button.addEventListener('click', function () {  
    
  var thisType = this.getAttribute('data-type');
  var input = document.getElementsByClassName('input-'+thisType)[0];
    
  if (thisType == 'success')
  {
    Notiflix.Notify.Success(input.value); 
  } else if (thisType == 'failure') {
    Notiflix.Notify.Failure(input.value);
  } else if (thisType == 'warning') {
    Notiflix.Notify.Warning(input.value);
  } else if (thisType == 'info') {
    Notiflix.Notify.Info(input.value);
  }

  }, false);

}
