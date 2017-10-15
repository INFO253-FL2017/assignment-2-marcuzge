function validateUser() {
  var username = document.contact.username.value;
  var subject = document.contact.sub.value;
  var message = document.contact.msg.value;
    if (username == "") {
      validateName();
      validateSub();
      validateMsg();
      return false;
    } else if (subject == "") {
      validateName();
      validateSub();
      validateMsg();
      return false;
    } else if (message == "") {
      validateName();
      validateSub();
      validateMsg();
      return false;
    } else {
      return true;
    } 
}


function validateName() {
  if (document.contact.username.value == "") {
      document.getElementById("alert1").innerHTML="*Please enter a name*";
      document.getElementById("name").className = document.getElementById("name").className + " error";
    }
}

function validateSub() {
  if (document.contact.sub.value == "") {
      document.getElementById("alert2").innerHTML="*Please enter a subject*";
      document.getElementById("subject").className = document.getElementById("subject").className + " error";
    }
}

function validateMsg() {
  if (document.contact.msg.value == "") {
      document.getElementById("alert3").innerHTML="*Please enter a message*";
      document.getElementById("message").className = document.getElementById("message").className + " error";
    }
}

function fnChangeBorder(boxId, id, alertId) {
  if (boxId.value == "") {
    document.getElementById("alert").innerHTML="";
    if (alertId == "alert1") {
      document.getElementById(alertId).innerHTML="*Please enter a name*";
    } else if (alertId == "alert2") {
      document.getElementById(alertId).innerHTML="*Please enter a subject*";
    } else {
      document.getElementById(alertId).innerHTML="*Please enter a message*";
    }
     
    document.getElementById(id).className = document.getElementById(id).className + " error";
  } else {
      document.getElementById(id).className = document.getElementById(id).className.replace(" error", ""); // this removes the error class
    document.getElementById(alertId).innerHTML="";
  }
}
