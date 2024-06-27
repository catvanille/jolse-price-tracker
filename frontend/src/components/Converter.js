const axios = require('axios');

const options = {
    "method": "GET",
    "url": "https://api.fxratesapi.com/latest?api_key=fxr_live_1326320655e918db649b4587f44de77b339c"
};

axios.request(options).then(function (response) {
    console.log(response.data);
}).catch(function (error) {
    console.error(error);
});