document.getElementById("distanceForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const lat1 = document.getElementById("lat1").value;
    const lon1 = document.getElementById("lon1").value;
    const lat2 = document.getElementById("lat2").value;
    const lon2 = document.getElementById("lon2").value;

    fetch("/calcular_distancia/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({ lat1, lon1, lat2, lon2 })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent = `Distância: ${data.distancia} km`;
    });
});

// Função para pegar o CSRF token do cookie
function getCSRFToken() {
    const name = "csrftoken";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.startsWith(name + '=')) {
            return c.substring(name.length + 1);
        }
    }
    return "";
}