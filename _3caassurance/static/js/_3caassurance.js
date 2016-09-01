function submitForm(form, onEnd) {
    var url = form.action;
    var method = form.method;
    try {
        var data = Array.prototype.reduce.call(form.querySelectorAll('input[name], textarea[name]'), setFormData, {});
        var request;
        if ("post" === method) {
            request = superagent.post(url).set('X-CSRFToken', data['csrfmiddlewaretoken']);
        }
        if (request) {
            request.send(data)
                   .withCredentials()
                   .end(onEndDecorated);
        } else {
            console.error('Method ' + method + 'is not supported');
        }
    } catch (err) {
        console.error(err);
    }

    function setFormData(data, element) {
        if (element.name) {
            data[element.name] = element.value
        }
        return data;
    }

    function onEndDecorated(err, res) {
        if (err) {
            console.error(err);
        }
        onEnd(err, res);
    }
}

// Thanks to http://stackoverflow.com/questions/6121203/how-to-do-fade-in-and-fade-out-with-javascript-and-css
function fadeHiddenElement(element) {
    var op = 1;  // initial opacity
    element.style.visibility = 'visible';
    var timer = setInterval(function () {
        if (op <= 0.05){
            clearInterval(timer);
            element.style.visibility = 'hidden';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.05;
    }, 50);
}