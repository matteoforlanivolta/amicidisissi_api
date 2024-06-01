"use strict";

var __adsServerAddr__ = "";

let ADSServer = {
    // Query di tutte le places nel DB.
    getPlaces: function() {
        let data = JSON.stringify({"key": "6258a5e0eb772911d4f92be5b5db0e14511edbe01d1d0ddd1d5a2cb9db9a56ba"});

        fetch("http://192.168.178.133:5001/api/getplaces", {
            method: "POST",
            body: data,
            headers: {
                'Accept': 'application/json',
                "Content-Type": "application/json"
            },
        }).then(resp => {
            document.body.innerHTML = "<h1>" + resp.status + " " + resp.statusText + "</h1>";

            return resp.json();
        }).then(resp => {
            document.body.innerHTML += "<p>" + JSON.stringify(resp) + "</p>";
        });
    }
};