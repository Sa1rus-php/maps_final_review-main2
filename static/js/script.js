nav_main = document.getElementById("nav_main");
nav_files = document.getElementById("nav_files");

main = document.getElementById("main");
files = document.getElementById("files");

form = document.getElementById("form");

delete_button = document.getElementById("delete_button"); 

nav_main.addEventListener("click", (event) => {
    event.preventDefault();

    main.classList.remove("disable");
    files.classList.add("disable");
} )

nav_files.addEventListener("click", (event) => {
    event.preventDefault();

    main.classList.add("disable");
    files.classList.remove("disable");
} )

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

form.addEventListener("submit", (event) => {
    event.preventDefault()

    let button = document.getElementById("submit");

    button.setAttribute("disabled", "");

    let input_data = document.getElementById("input_data").value;

    let data = {
        business_type: input_data,
    }

    let csrf_token = getCookie('csrftoken');

    axios.post("/",
                data,
                {
                    headers: {
                       'Content-Type': 'application/json',
                        "X-CSRFToken": csrf_token,
                    }
                },
    ).then((response) => {
        button.removeAttribute("disabled", "");
    }).catch((error) => {
        console.log(error);
    })
})

delete_button.addEventListener("click", (event) => {
    event.preventDefault()

    let csrf_token = getCookie('csrftoken');

    axios.post(
        "/delete_all/",
        null,
        {
            headers: {
               'Content-Type': 'application/json',
                "X-CSRFToken": csrf_token,
            }
        }
    ).then((response) => {
        console.log(response);
    }).catch((error) => {
        console.log(error);
    })
})