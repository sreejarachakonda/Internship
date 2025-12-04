fetch("http://127.0.0.1:8000/characters")
    .then(res => res.json())
    .then(data => {
        let ul = document.getElementById("characters");

        data.forEach(c => {
            let li = document.createElement("li");
            li.innerHTML = `<strong>${c.name}</strong> - ${c.role}`;
            ul.appendChild(li);
        });
    })
    .catch(err => console.log(err));
