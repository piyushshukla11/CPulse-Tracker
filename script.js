function addUser() {
    fetch("http://127.0.0.1:5000/add_user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: document.getElementById("name").value,
            codeforces: document.getElementById("cf").value,
            codechef: document.getElementById("cc").value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message || data.error));
}

fetch("http://127.0.0.1:5000/leaderboard")
.then(res => res.json())
.then(data => {
    const list = document.getElementById("leaderboard");
    const labels = [];
    const ratings = [];

    data.forEach(u => {
        labels.push(u.name);
        ratings.push(u.codeforces.rating);

        const li = document.createElement("li");
        li.innerText = `${u.name} | CF: ${u.codeforces.rating} | CC: ${u.codechef.rating}`;
        list.appendChild(li);
    });

    new Chart(document.getElementById("chart"), {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Codeforces Rating",
                data: ratings
            }]
        }
    });
});
