function locate() 
{
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation Is Not Supported By This Browser.");
    }
}

function showPosition(position) 
{
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    document.getElementById('latitudeInput').value = latitude;
    document.getElementById('longitudeInput').value = longitude;
}

function showError(error) 
{
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

function passon()
{
    document.getElementById('myForm').submit();
}