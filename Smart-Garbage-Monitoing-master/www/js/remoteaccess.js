function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
$(document).ready(function () {
    console.log("ready");

    $("#front").click(function () {
        console.log("front");
        obj = JSON.parse('{"a":"w"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/front"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });   
    });
    $("#back").click(function () {
        console.log("back");
        obj = JSON.parse('{"a":"s"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/back"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
    $("#left").click(function () {
        console.log("left");
        obj = JSON.parse('{"a":"a"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/left"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
    $("#right").click(function () {
        console.log("right");
        obj = JSON.parse('{"a":"d"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/right"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
    $("#stop").click(function () {
        console.log("right");
       obj = JSON.parse('{"a":"x"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/stop"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
    $("#pick").click(function () {
        console.log("right");
        obj = JSON.parse('{"a":"x"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/pick"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
    $("#drop").click(function () {
        console.log("right");
        obj = JSON.parse('{"a":"x"}');
        console.log(obj);
        $.ajax({
            data: obj,
            type: 'POST',
            crossDomain: true,
            dataType: "json",
            crossOrigin: null,
            url: "http://54.160.238.67:5000/drop"
        })
            .done(function (data) {
                if (data.error) {
                    console.log(data.Outcome);
                }
                else {
                    console.log(data);
                }
            });
    });
});