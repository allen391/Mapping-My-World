/**
 * Created by chent on 1/04/2017.
 */
var setheight = function() {
        document.getElementById("app").style.height = window.innerHeight + 'px';
    }
var init = function() {
        setInterval(setheight, 100);
    }
