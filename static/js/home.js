async function verificarToken() {
    const token = sessionStorage.getItem("access_token");

    // Si no hay token, redirigir
    if (!token) {
        window.location.href = "/";
        return;
    }

    try {
        const response = await fetch("/api/protected/", {
            method: "GET",
            headers: {
                "Authorization": "Bearer " + token
            }
        });

        if (!response.ok) {
            // Token inválido o expirado
            window.location.href = "/";
        }

        // Si todo está bien, no hacer nada
    } catch (error) {
        // Error de red o servidor
        console.error("Error verificando el token:", error);
        window.location.href = "/";
    }
}