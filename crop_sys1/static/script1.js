// Function to parse query parameters from URL
function getQueryParams() {
    // Get the query string portion of the URL
    const queryString = window.location.search;

    // Create an empty object to store the parameters
    const params = {};

    // Check if there are any query parameters
    if (queryString) {
        // Split the query string into individual parameters
        const queryParams = queryString.substring(1).split('&');

        // Iterate over each parameter
        queryParams.forEach(param => {
            // Split the parameter into key and value
            const [key, value] = param.split('=');
            // Decode the key and value (URL decoding)
            const decodedKey = decodeURIComponent(key);
            const decodedValue = decodeURIComponent(value);
            // Add the key-value pair to the params object
            params[decodedKey] = decodedValue;
        });
    }

    // Return the object containing the query parameters
    lat=params['latitude']
    lon=params['longitude']

    const baseUrl = 'http://127.0.0.1:8000/result';

    // Construct the URL
    const searchParams = new URLSearchParams(params);
    const url = `${baseUrl}?${searchParams.toString()}`;
    
    fetch(url)
    .then(response => {
        // Check if response is ok
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Return HTML content of the response
        return response.text();
    })
    .then(htmlContent => {
        // Update the DOM with the received HTML content
        document.body.innerHTML = htmlContent;
    })
}

// Example usage:
window.onload = getQueryParams();
