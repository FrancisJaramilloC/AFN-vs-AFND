const API_BASE_URL = 'http://127.0.0.1:8000/api/automata';

async function evaluarCadena(ejercicioId, cadena) {
    try {
        const response = await fetch(`${API_BASE_URL}/ejercicio${ejercicioId}/evaluar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cadena })
        });
        
        if (!response.ok) {
            throw new Error('Error en la respuesta de la API');
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error al evaluar la cadena:', error);
        return { error: 'Error de conexión con el servidor.' };
    }
}
