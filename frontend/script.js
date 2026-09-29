const BACKEND_URL = "https://pocket-smart-ai-3m6l.onrender.com";

async function testBackend() {
    try {
        const response = await fetch(BACKEND_URL);
        const data = await response.json();

        console.log(data);
        alert(data.message);
    } catch (error) {
        console.error(error);
        alert("Backend connection failed!");
    }
}