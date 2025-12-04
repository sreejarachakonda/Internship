fetch("http://127.0.0.1:8000/kingdoms")
    .then(res => res.json())
    .then(data => {
        let ul = document.getElementById("kingdoms");
        data.forEach(k => {
            let li = document.createElement("li");
            li.textContent = k.name;
            ul.appendChild(li);
        });
    });
