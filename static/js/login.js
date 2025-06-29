document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const response = await fetch("http://127.0.0.1:8000/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            sessionStorage.setItem("access_token", data.access_token);
            window.location.href = '/home';
        } else {
            document.getElementById("msg").textContent = "Error: " + data.detail;
        }
    } catch (error) {
        document.getElementById("msg").textContent = "Error de conexión";
    }
});