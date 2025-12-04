fetch("http://127.0.0.1:8000/battles")
    .then(res => res.json())
    .then(data => {
        let ul = document.getElementById("battles");
        data.forEach(b => {
            let li = document.createElement("li");
            li.textContent = b.name;
            ul.appendChild(li);
        });
    });
