function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getFormData(){
    formData = Object.fromEntries(new FormData(document.querySelector('form')).entries());
    return formData
}

function updatePage(response){
    document.getElementById('overwrite').innerHTML = response;
}

function fetchData(){

    formData = getFormData();
    console.log(formData)
    fetch("/", {
    method: "POST",
    body: JSON.stringify({formData}),
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-type": "application/json; charset=UTF-8"
    }
})
  .then(response => {
    return response.json();
  })
  .then((data) => updatePage(data.replace(/\"/g, "")))
}

document.addEventListener('submit', function () { fetchData(); });